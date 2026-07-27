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

---

## Academy Review

Score:

- Technical correctness: 32/40
- Understanding: 25/30
- Completeness: 17/20
- Engineering practices: 8/10
- Overall: 82/100

What is correct:

- You understand virtual environments isolate dependencies.
- You understand `requirements.txt` records dependencies.
- You understand that Flask starts a local server and responds to browser requests.

Corrections:

- `debug=True` does more than make development faster. It enables the debugger and auto-reloader, but it must not be used in production because detailed errors can leak sensitive information.
- The difference between `/` and `/health` is not just which function handles them; each route represents a different API resource or purpose.
- The lifecycle answer should mention URL matching, route handlers, and Flask converting returned dictionaries into JSON responses.

Improved answer:

```text
A virtual environment isolates one project's Python packages from the system Python and from other projects.

`requirements.txt` lists the packages needed to recreate the environment.

`debug=True` enables development features such as auto-reload and detailed error pages. It should not be used in production.

`/` is the home endpoint. `/health` is a health-check endpoint used to confirm the backend is running.

When `python run.py` runs, Python executes the file, creates the Flask app, starts the local server, receives the browser request, matches the URL to a route, runs the handler, and returns a JSON response.
```

Additional practice:

- Explain why `/health` is useful for deployment monitoring.
- Add one more simple route and describe its request flow.
