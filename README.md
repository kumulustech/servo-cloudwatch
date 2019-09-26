# servo-cloudwatch

## AWS Cloudwatch Measure Driver for use with Opsani Optune

This driver uses the boto3 Cloudwatch client to retrieve metrics via the get_metric_data function. Metric queries are defined in the config.yaml (see config.yaml.example) and their structure can be found here: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.get_metric_data

Note: the config allows a custom key `AsgName` on dimensions with `Name: InstanceId`. This is not part of AWS api; it is implemented within the driver for the sake of config brevity. Each instance in AsgName gets a copy of the metric query made with `AsgName` removed and `Value: <instanceId>` replacing it within the dimension

## Deployment caveats

1. This driver requires measure.py base class from the Optune servo core. It can be copied or symlinked here as part of packaging.
1. AWS credentials must be present on the servo host (can be environment variables, or a .aws folder)
1. AWS default region must be defined as well
