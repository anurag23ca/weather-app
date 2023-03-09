# FastAPI Weather API
These are the respective API endpoints :
        
        /api/weather - retrieves weather data
        /api/weather/stats - provides statistics about the data
        /docs - provides documentation using openapi

## Prerequisites

The following prerequisites are required to use this API:

    Python (3.7 or higher)
    Virtualenv
    SQLite
    AWS account (if deploying to AWS)

## Installation and Usage

### To install the required dependencies, create and activate a virtual environment with the following commands:

    python -m venv venv

### To activate the virtual environment:

    venv\Scripts\activate (in Windows)
    source venv/bin/activate (in Linux and Mac)

### Then, install the required dependencies:

    pip install -r requirements.txt

### Move to src dir:
    
    cd src

### To ingest the data:

    python ingest.py

### To run the server:

    uvicorn main:app --reload

### To access the API endpoints:
    http://127.0.0.1:8000/api/weather/ -- for weather records
    http://127.0.0.1:8000/api/weather/stats -- for weather stats
    http://127.0.0.1:8000/docs -- ui specification of api

    
## To run tests:
    
    cd src
    pytest

# AWS Deployment

To deploy the API to AWS, use the following steps:

    - Create a Python project with a app.py file containing the FastAPI application code.
    - Create a new AWS Lambda function and configure its runtime to use Python 3.8 or later.
    - Package your Python code and any dependencies as a ZIP file and upload it to AWS Lambda.
    - Set the handler function in your Lambda function to the name of your FastAPI application function.
    - Create an API Gateway , REST API or HTTP API that integrates with your Lambda function.
    - Deploy respective APIs to a publicly accessible endpoint.
    - RDS can be used to store the ingested data

## Conclusion
    - This was one of the ways to implement these weather APIs using fastAPI. Scalability and security features can be
        managed in deployment strategies over aws.