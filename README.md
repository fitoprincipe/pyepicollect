# PyEpiCollect

## Read EpiCollect 5 data from python

### Install

> pip install pyepicollect

### Use
#### Search for a given project

``` python
import pyepicollect as pyep

# Public Project
result = pyep.api.search_project(name)

# Private Project
token = pyep.auth.request_token(client_id, client_secret)
token = token['access_token']

result = pyep.api.search_project(name, token=token)
```

### Test

1. Make a virtual environment:
> virtualenv env --python=python3

2. install requirments
> pip install -r requirements.txt

3. run test
> python -m pytest -v
