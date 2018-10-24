[![Build Status](https://travis-ci.com/vmuthabuku/Store-Manager.svg?branch=ch-codeclimate-badge-161416503)
[![Coverage Status](https://coveralls.io/repos/github/vmuthabuku/Store-Manager/badge.svg?branch=ch-codeclimate-badge-161416503
)](https://coveralls.io/github/vmuthabuku/Store-Manager?branch=ch-codeclimate-badge-161416503
)
[![Maintainability](https://api.codeclimate.com/v1/badges/94de1a36b60b36afe112/maintainability)](https://codeclimate.com/github/vmuthabuku/Store-Manager/maintainability)


# Store-Manager
Store Manager is a web application that helps store owners manage sales and product inventory records. This application is meant for use in a single store.

### Running the app
1. git clone the repo `https://github.com/vmuthabuku/Store-Manager.git`
2. Switch to `challenge 2` branch \
`$ git checkout challenge 2`
3. install requirements
`$ pip install -r requirements.txt`
4. in the terminal 
`$ export FLASK_APP=run.py`
5. run the app
`$ flask run`

### Run tests

in the terminal in the root directory of the folder run `pytest`

### Pivotal tracker stories 
https://www.pivotaltracker.com/n/projects/2202864

###Heroku link
https://storemanager-vmuthabuku.herokuapp.com/

##Endpoints
The api endpoints are

| Endpoint | Description |
| --- | --- |
| GET /products | Fetch all products |
| GET /products/productId | Fetch a single product record |
| GET /sales | Fetch all sale records |
| GET /sales/saleId | Fetch a single sale record |
| POST /products | Create a product |
| POST /sales | Create a sale order |
