
## About this project

The Master Thesis project representing a framework 
for standardization of data integration process by creation 
of sources and queries common registry.

## Prerequisites

1. Python 3
2. Docker
3. Packages from project requirements

## How to use

1. `docker-compose up` to run test database instances
2. run `scripts/load_data.py` to load test data
3. run `scripts/make_docs.py` to generate the documentation from code
4. run `mkdocs serve` to launch documentation web-service
5. check the `lib` directory to find Source and Query interfaces definition
6. check the `app` directory to find specific Source and Query realizations and integration code examples