Why do we use a virtual environment?
    We use a virtual enviroment to isolate dependencies for a project.

What does requirements.txt do?
    Requirements.txt is used to record the dependencies used in the project so that they can be reinstalled when necessary.

What is the purpose of debug=True?
    This tell flask to run on debug mode which makes development faster and outputs detailed errors.

What is the difference between the / and /health endpoints?
    The / endpoint points to the home function, while the /health endpoint points to the health function/handler.

Explain, in your own words, what happens from the moment you run python run.py until your browser displays the JSON response.
    Python reads the file and runs the app as instructed, which starts a local server. When the browser make a request to this server, the server handles the request and returns a JSON response.