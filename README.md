# Flask-KubeProxy

Middleware to fix flask-restplus swagger behavior behind kubernetes proxy.

### Problem

When accessing a kubernetes service via the `kubectl proxy`, the path of the
 swagger.json file and the url's used by the 'try it out' feature are mapped
  without taking the context path into account.
Instead of 

`http://localhost:xxxx/api/v1/namespaces/<namespace>/services/<service_name>/proxy/swagger.json`

the swagger.json file will be fetched from

`http://localhost:xxxx/swagger.json`

and all requests sent out by the 'try it out' feature will use the 
same wrong mapping.

### Fix

The Flask-KubeProxy fixes this behavior by using the 
`HTTP_X_FORWARDED_URI` header added by the proxy to set the `SCRIPT_NAME` 
variable in the WSGI environment. This variable is used by swagger to 
build the problematic paths. See [PEP-0333](https://www.python.org/dev/peps/pep-0333/#environ-variables).


### Installation

You can pip install this package straight from this github repo by running

`pip install https://github.com/ml6team/Flask-KubeProxy/archive/v0.1.zip`

### Usage

```python
from flask import Flask
from flask_restplus import Api
from flask_kubeproxy.middleware import KubeProxy
 
app = Flask(__name__)
app.wsgi_app = KubeProxy(app.wsgi_app)
api = Api(app)
 
@api.route("/")
def hello_world():
  return "Hello, world!"
  ```