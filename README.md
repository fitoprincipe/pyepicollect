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

### Unit Test

1. Make a virtual environment: (see https://docs.python-guide.org/dev/virtualenvs/#lower-level-virtualenv)
> virtualenv env --python=python3

Make sure to name the environment `env` so it's ignored by git. Do not do:
> virtualenv venv --python=python3

2. install requirments
> pip install -r requirements.txt

3. run test
> python -m pytest -v
