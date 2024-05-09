"""
Step 1: import FastAPI

FastAPI is a Python class that provides all the functionality for your API.

FastAPI is a class that inherits directly from Startlette.
You can use all the Startlette functionality with FastAPI too.
"""
from fastapi import FastAPI

"""
Step 2: create a FastAPI "instance"

Here the app variable will be an instance of the class FastAPI.
This wil be the main point of interaction to create all your API.

Here the app variable will be an instance of the class FastAPI.
"""
app = FastAPI()

"""
Step 3: create a path operation

Path here refers to the last part of the URL starting from the first /.

So, in a URL like:
https://example.com/items/foo

the path would be:
/items/foo

A path is also commonly called an endpoint or a route.

While building an API, the path is the main way to seperate concerns and resources.

Operation here refers to one of the HTTP methods.

One of:
- POST
- GET
- PUT
- DELETE

and more exotic ones:
- OPTIONS
- HEAD
- PATCH
- TRACE

In the HTTP protocol, you can communicate to each path using one (or more) of these "methods".

When building APIds, you normally use these specific HTTP methods to perform a specific action.

Normally you use:
- POST: to create data.
- GET: to read data.
- PUT: to update data.
- DELETE: to delete data.

So, In OpenAPI, each of the HTTP methods is called an "operation".

We are going to call them "operations" too.

Define a path operation decorator

The @app.get("/") teels FastAPI that the function right below is in charge of handling requests that go to:
- the path /
- using a get operation

That @something syntax in Python is called a "decorator".

You put it on top of a function.
Like a pretty decorative hat (I guess that's where the term came from).

A "decorator" takes the function below and does something with it.

In our case, this decorator tells FastAPI that the function below corresponds to the path / with an operation get.

It is the "path operation decorator".

You can also use the other operations:
- @app.post()
- @app.put()
- @app.delete()

And the more exotic ones:
- @app.options()
- @app.head()
- @app.patch()
- @app.trace()

You are free to use each operation (HTTP method) as you wish.

FastAPI doesn't enforce any specific meaning.

The information here is presented as a guideline, not a requirement.

For example, when using GraphQL you normally perform all the actions using only POST operations.

Step 4: define the path operation function

This is our "path operation function":

- path is /.
- operation is get.
- function: is the function below the "decorator"

This is a Python function.

It will be called by FastAPI whenever it receives a request to the URL "/" using a GET operation.

In this case, it is an async function.

You could also define it as a normal function instead of async def:
"""

@app.get("/")
async def hello_world():
  """
  Step 5: return the content

  You can return a dict, list, singular values as str, int, etc.

  You can also return Pydantic models (you'll see more about that later).

  There are many other objects and models that will be automatically converted to JSON (including ORM, etc,).
  Try using your favorite ones, it's highly probable that they are already supported.
  """
  return {
    "message": "Hello World"
  }
