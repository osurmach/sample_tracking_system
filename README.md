# Sample Tracking System API #

## Requirements ##

To run API you need the following software:
* [Docker](https://docs.docker.com/engine/install/)

## How to run ##

1. Clone the project from GitHub (or unpack .zip file).
2. Make sure Docker is up and running.
3. Run `run.sh -start` from terminal.

`run.sh` script will create Docker image and start Docker container.

To access API Docs open <docker_container_url>/docs in your browser (e.g. http://0.0.0.0:80/docs).

## API ##

The following API methods are available:

### /orders/new  [POST] ###

to place new order. Requires the following payload:
```
{
  "order": [
    {
      "sample_uuid": "string",
      "sequence": "string"
    }
  ]
}
```
*Note*: `sample_uuid`'s must be unique.


Returns order UUID if order created successfully
```
{
  "order_uuid": "string"
}
```
Or Validation Error 422 with repeated sample UUIDs if duplicated were sent
```
{
  "repeat_sample_uuids": []
}
```

### /sample [GET] ###

To get sample.

<b>Parameters</b>
* status* _required_. Must be one of the following values:
  * ordered - to return list of samples that are ready to be processed
  * processed - to retun list of samples that are ready to be shipped


### /sample/update/processed [PUT] ###

To update processed orders. Requires the following payload:
```
{
  "samples_made": [
    {
      "sample_uuid": "string",
      "plate_id": int,
      "well": "string",
      "qc_1": float,
      "qc_2": float,
      "qc_3": ["FAIL" or "PASS"]
    }
  ]
}
```

### /sample/update/shipped [PUT] ###

To update status of shipped orders. Requires the following payload:
```
{
  "samples_shipped": [
    {
      "sample_uuid": "string"
    }
  ]
}
```

### /order/status [POST] ###

To report sample statuses in order. Requires the following payload:
```
{
  "order_uuid_to_get_sample_statuses_for": "string"
}
```

![Sample Tracking API](api.png?raw=true "Sample Tracking API")