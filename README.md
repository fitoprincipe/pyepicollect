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
