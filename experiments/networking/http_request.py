from urllib.request import urlopen
import json

url = "https://jsonplaceholder.typicode.com/posts/1"

with urlopen(url) as response:
    data = json.load(response)
    
print(data)

# Who is the client?
    # The client is this application calling the url.
# Who is the server?
    # The server is the url handler at jsonplaceholder.typicode.com
# What was requested?
    # The post with the id of 1
# What format was returned?
    # The returned format is JSON