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

---

## Academy Review

Score:

- Technical correctness: 34/40
- Understanding: 26/30
- Completeness: 17/20
- Engineering practices: 8/10
- Overall: 85/100

What is correct:

- You clearly explain client/server roles.
- Your HTTP method definitions are mostly correct.
- Your 404 and 500 explanations are correct.
- You understand that APIs mediate frontend access to data.

Corrections:

- A frontend should not talk directly to a database not only because of formatting, but because of security, authentication, authorization, validation, business rules, and keeping database credentials private.
- JSON is a text data format, not just something supported by many languages.
- `PUT` usually replaces a whole resource, while `PATCH` partially updates a resource. Your answer captures this.

Improved answer:

```text
A client sends requests. A server receives requests, processes them, and sends responses.

A frontend communicates with an API instead of the database because the API protects database credentials, validates input, applies business rules, checks authentication and authorization, and returns data in a frontend-friendly format.

GET retrieves data. POST creates a new resource. PUT replaces a resource. PATCH updates part of a resource. DELETE removes a resource.

JSON is a text format for representing structured data with objects, arrays, strings, numbers, booleans, and null. It is common because it is lightweight and widely supported.

404 means the requested resource was not found. 500 means the server failed unexpectedly while processing the request.
```

Additional practice:

- For each project route, identify the HTTP method, expected status code, and response body.
- Explain why APIs should validate input before touching the database.
