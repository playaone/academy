Answer these questions:

Why is the Application Factory pattern preferred over creating app = Flask(__name__) globally?
    The Application Factory Pattern sets up the app, configures it, pulls in extentions, initializes core components, and returns the app as a callable object.

What problem do Blueprints solve?
    Blueprints solve the problem of organization and separation of concerns whereby routes are organized according to the feature they are responsible for, and one file for one feature/concern.

Why is it beneficial to organize routes by feature instead of placing them all in one file?
    This is beneficial especially to the developers as it makes debugging really easy and makes the app scallable.

What is the responsibility of create_app()?
    The responsibility of create_app() is to configure the app and return a callable object instead of a global app variable.

Explain the lifecycle of your Flask application from python run.py to handling a request to /health.
    run.py creates the app and starts the server. 
    The server serves the app at the specified ip address and port.
    The client makes a request for the "/health" endpoint.
    The app receives the request, processes it with the health() request handler and then issues an appropriate response.
    This response is received by the client and transformed into a human-friendly format.

---

## Academy Review

Score:

- Technical correctness: 31/40
- Understanding: 24/30
- Completeness: 16/20
- Engineering practices: 8/10
- Overall: 79/100

What is correct:

- You understand that `create_app()` builds and returns the Flask app.
- You understand that Blueprints organize routes by feature.
- Your request lifecycle explanation has the right broad order: run server, receive request, route to handler, return response.

Corrections:

- The main reason the Application Factory pattern is preferred is that it lets the app be configured differently for development, testing, and production. It also avoids import-time global app setup and makes tests easier.
- "Pulls in extensions" is part of what the factory does, but it does not fully explain why it is preferred over a global `app = Flask(__name__)`.
- Blueprints do not create one file per feature by themselves; they provide a registration mechanism for grouping related routes.
- The client does not usually transform JSON into a "human-friendly format" unless the client application chooses to render it.

Improved answer:

```text
The Application Factory pattern is preferred because it creates the Flask app inside a function, allowing different configurations for development, testing, and production. It also makes tests easier because each test can create a fresh app instance.

Blueprints group related routes and let the application register those route groups cleanly.

`create_app()` creates the Flask app, loads configuration, initializes extensions, registers blueprints, registers error handlers, and returns the configured app.

When `python run.py` runs, it creates the app, starts the development server, receives a request to `/health`, matches that URL to the health route, runs the handler, and returns a JSON response.
```

Additional practice:

- Explain how `create_app(TestConfig)` helps your tests.
- Trace one request through `run.py`, `create_app()`, blueprint registration, and the route handler.
