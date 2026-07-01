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