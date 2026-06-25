What is the difference between a client and a server?
    The difference between a client and a server is that the client makes a request and the server is responsible for processing the request and replying with a response.

Why does a frontend usually communicate with an API instead of directly with the database?
    This is because the API acts as a middleman, processes the request, validates it, and determines if this request needs a resource from the database, if yes, the API runs the required process responsible for getting the resource and then sends the resource to the frontend as a response in a format that the frontend can understand.

Explain the purpose of each of these HTTP methods:
    GET: This is used to retrieve data from the server.
    POST: This is used to tell the server to create a new resource using the information provided in the body of the request.
    PUT: This is used to replace an already existing resource.
    PATCH: This is used to replace parts of an existing resource.
    DELETE: This is used to remove a resource.

What is JSON, and why is it commonly used?
    JSON means JavaScript Object Notation, it is commonly used because most programming languages support it.

What does a 404 Not Found response mean? What about 500 Internal Server Error?
    A 404 response means that the requested resource does not exist or could not be found by the server.
    A 500 response means that the server encountered an error while trying to process the request.