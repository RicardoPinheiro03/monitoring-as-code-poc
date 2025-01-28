from prometheus_client import CollectorRegistry, Gauge, push_to_gateway
import random, time

LOWER_THRESHOLD_RNG = 0
UPPER_THRESHOLD_RNG = 100
STEP_RNG = 1
METRICS_COUNTER = 500

global_registry = CollectorRegistry() # Global registry creation

cpu_usage = Gauge('service_cpu_usage', 'CPU usage of services', ['service'], registry=registry)
ram_usage = Gauge('service_ram_usage', 'RAM usage of services', ['service'], registry=registry)

i = 0
# While cycle to generate artificial CPU and RAM metrics to be injected in Prometheus
while i < METRICS_COUNTER:
        cpu_usage.labels(service='service_A').set(generateNumberZeroToHundred())
        ram_usage.labels(service='service_A').set(generateNumberZeroToHundred())
        time.sleep(3)
        cpu_usage.labels(service='service_B').set(generateNumberZeroToHundred())
        ram_usage.labels(service='service_B').set(generateNumberZeroToHundred())
        time.sleep(3)
        cpu_usage.labels(service='service_C').set(generateNumberZeroToHundred())
        ram_usage.labels(service='service_C').set(generateNumberZeroToHundred())
        time.sleep(3)
        i += 1
        push_to_gateway('http://localhost:9091', job='backend_services', registry=global_registry)

def generateNumberZeroToHundred():
        """
        Generates a random number within a range of 0 and 100.

        Args:
          No input arguments.

        Returns:
          num: Integer randomly generated between 0 and 100.

        """
        num = random.randrange(LOWER_THRESHOLD_RNG, UPPER_THRESHOLD_RNG, STEP_RNG)
        return num
