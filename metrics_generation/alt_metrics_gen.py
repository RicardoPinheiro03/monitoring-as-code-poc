import time
import requests
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

PROMETHEUS_URL = "http://localhost:9090"  # Prometheus URL
PUSHGATEWAY_URL = "http://localhost:9091"  # PushGateway URL
METRIC_NAME = "example_metric"

# PushGateway setup
registry = CollectorRegistry()
gauge = Gauge(METRIC_NAME, 'Description of example metric', registry=registry)

def query_prometheus(metric_name):
    """Query Prometheus for the value of a metric."""
    response = requests.get(f"{PROMETHEUS_URL}/api/v1/query", params={'query': f"sum({metric_name})"})
    data = response.json()
    if response.status_code == 200 and data["status"] == "success":
        # Extract the value from the Prometheus query result
        result = data["data"]["result"]
        if result:
            return float(result[0]["value"][1])
    return 0  # Default to 0 if no data is found

def main():
    count_threshold = 10  # Stop condition: number of tuples in the metric table
    current_count = 0

    while current_count < count_threshold:
        # Push a random metric value to the PushGateway
        gauge.set(time.time() % 100)  # Example metric value
        push_to_gateway(PUSHGATEWAY_URL, job='example_job', registry=registry)
        print(f"Metric pushed to PushGateway.")

        # Query Prometheus for the current count of tuples
        current_count = query_prometheus(METRIC_NAME)
        print(f"Current count of tuples in Prometheus: {current_count}")

        if current_count >= count_threshold:
            print("Threshold reached. Exiting loop.")
            break

        time.sleep(5)  # Wait before the next iteration

if __name__ == "__main__":
    main()