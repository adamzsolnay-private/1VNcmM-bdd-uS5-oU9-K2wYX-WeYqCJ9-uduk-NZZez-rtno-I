 
<!-- ABOUT THE PROJECT -->
### Notes on my implementation
* I have not used any GenAI tools
* Time was up
* The phase I reached:
  * The REST API endpoint can receive JSON-formatted metrics
  * from multiple sensors, multiple datapoints
  * Datasets are normalized to 2 decimal points
  * Then inserted into the DB along with the actual UTC timestamp
  * Input validation and exception handling is included

### Prerequisites

* python v3.10+
* python modules:
  * fastapi
  * pydantic
  * uvicorn


<!-- USAGE EXAMPLES -->
### Usage
* Create a python virtual environment
* Install the dependencies
* Start the server, executing this in the same folder as main.py:
  ```sh
  uvicorn main:app --reload
  ```
* Post some test data:
  ```sh
  curl -H "Content-Type: application/json" -X POST -d'{"sensor_id": 1,"temperature":23.123456,"humidity":50.1234,"wind_speed": 5}' http://127.0.0.1:8000/api/weather_metrics
  ```
*  Validate as needed

<!-- What is missing from this POC -->
### What is missing from this POC
* The feature to query the ingested data

<!-- Enhancements -->
### Enhancements in my mind
* Implement ORM against SQL Injections
* Authentication for both GETs and POSTs
* Secure communication between client-API and API-DB
* Identify and convert values in non-SI units (ex: Fahrenheit) to SI
* Create and document the API schema

###
