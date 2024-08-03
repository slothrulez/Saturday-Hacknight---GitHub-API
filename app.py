import os
from flask import Flask, request, render_template
import requests
import base64
import networkx as nx
import matplotlib.pyplot as plt
import io
import json

app = Flask(__name__)

ACCESS_TOKEN = 'your_github_access_token_here'
HEADERS = {'Authorization': f'token {ACCESS_TOKEN}'}

def get_file_contents(owner, repo, path):
    url = f'https://api.github.com/repos/{owner}/{repo}/contents/{path}'
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def parse_package_json(content):
    data = json.loads(content)
    dependencies = data.get('dependencies', {})
    return dependencies

def parse_requirements_txt(content):
    dependencies = {}
    lines = content.splitlines()
    for line in lines:
        if line and not line.startswith('#'):
            package = line.split('==')[0]
            dependencies[package] = None
    return dependencies

def create_dependency_graph(dependencies):
    G = nx.Graph()
    for dep in dependencies:
        G.add_node(dep)
        for subdep in dependencies:
            if dep != subdep:
                G.add_edge(dep, subdep)
    return G

def visualize_graph(G):
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G, k=0.5)
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=12, font_weight='bold')
    plt.title('Dependency Graph')
    
    
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    img_str = base64.b64encode(img.getvalue()).decode('utf-8')
    plt.close()
    return img_str

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        owner = request.form['owner']
        repo = request.form['repo']
        path = request.form['path']
        
        file_data = get_file_contents(owner, repo, path)
        if file_data and 'content' in file_data:
            content = base64.b64decode(file_data['content']).decode('utf-8')
            
            if path.endswith('package.json'):
                dependencies = parse_package_json(content)
            elif path.endswith('requirements.txt'):
                dependencies = parse_requirements_txt(content)
            else:
                return "Unsupported file format", 400
            
            G = create_dependency_graph(dependencies)
            img_str = visualize_graph(G)
            
            return render_template('index.html', img_data=img_str)
        else:
            return "Error fetching file contents or file not found", 400
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
