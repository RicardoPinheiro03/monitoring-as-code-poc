from prometheus_client import CollectorRegistry, Gauge, push_to_gateway
import random, time

LOWER_THRESHOLD_RNG = 0
UPPER_THRESHOLD_RNG = 100
STEP_RNG = 1

registry = CollectorRegistry()

g_svc_a = Gauge("svc_a_cpu_usage", "CPU Usage Service A", registry=registry)

i = 0
while i < 50:
        rand_number = random.randrange(LOWER_THRESHOLD_RNG, UPPER_THRESHOLD_RNG, STEP_RNG)
        print(f"Number generated for CPU Usage in Service A: {rand_number}")
        g_svc_a.set(rand_number)
        time.sleep(3)
        i += 1
        push_to_gateway("http://localhost:9091", job="cpu_metrics_job", registry=registry)