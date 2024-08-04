
![gitnotion](https://github.com/user-attachments/assets/079fdd2e-ba20-4a5b-9801-58448e81d8b9)




# Dependency Visualizer
 The Dependency Visualizer is a web-based tool designed to help developers and teams understand the dependency structure of their GitHub repositories. By analyzing dependency files such as 'package.json' for Node.js projects or 'requirements.txt' for Python projects, the application generates a visual graph of dependencies, making it easier to grasp how different packages or modules interact within a project. This tool can be particularly useful for debugging, optimizing dependency management, or simply gaining a clearer understanding of a project's architecture.
## Team members
1. [Anirudh Kannan](https://github.com/slothrulez)
2. [Anshika Mariyam George](https://github.com/anshikageorge)
3. [Britto Lionel Francis](https://github.com/britto18)
## Link to product walkthrough
[click here for product walkthrough](https://youtu.be/zYDdMZ0uVAs)
## How it Works ?
1. User Input:  Users provide details through the web form, including the GitHub repository owner, repository name, and the path to the dependency file ('package.json' or 'requirements.txt').
2. Data Retrieval:  The application retrieves the specified file from the GitHub repository using the GitHub API.
3. Dependency Analysis:  The contents of the dependency file are parsed to identify dependencies and their relationships.
4. Graph Generation:  A visual representation of the dependencies is created using 'networkx' and 'matplotlib', and is then displayed on the webpage.
5. Visualization:  The generated graph is shown as an image, allowing users to interact with and analyze their project's dependency structure.
## Libraries used
- requests - Version 2.32.3:  For making HTTP requests to the GitHub API.
- flask - Version 3.0.3:  The web framework used for building the application.
- networkx - Version 3.3:  Used for creating and manipulating complex networks and graphs.
- matplotlib - Version 3.9.1:  For generating and rendering the dependency graph as an image.
## How to configure
1. Clone the Repository:  Clone this repository to your local machine using the following command:
    ```bash
        git clone <repository-url>
    ```
2. Navigate to Project Directory:  Change into the project directory:
    ```bash
    cd <project-directory>
    ```
3. Create a Virtual Environment:  Set up a virtual environment to manage dependencies:
    ```bash
        python -m venv venv
    ```
4. Activate the Virtual Environment:
   ```bash
       venv\Scripts\activate.bat
   ```
5. Install Dependencies:  Install the required Python packages:
  ```bash
      pip install requests flask networkx matplotlib
  ```
## Important Note
Update the 'ACCESS_TOKEN' variable in 'app.py' with your own GitHub access token. This is required to authenticate API requests to GitHub. Do not share this token publicly.
 ```bash
    ACCESS_TOKEN = 'your_github_access_token_here'
 ```
    
## How to Run
1. Ensure Virtual Environment is Active:  Make sure your virtual environment is activated.
2. Start the Flask Application:  Run the Flask app using the following command:
   ```bash
        python app.py
   ```
3. Access the Application:  Open a web browser and navigate to 'http://127.0.0.1:5000' to use the Dependency Visualizer.
   
