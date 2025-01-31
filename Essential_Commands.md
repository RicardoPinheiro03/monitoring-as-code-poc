# Essential Commands to Use Grafonnet

## Download Grafonnet Library
```bash
jb install github.com/grafana/grafonnet/gen/grafonnet-latest@main
```

## Generate JSON dashboard file from JSONNet
```bash
jsonnet -J ${LIBRARY_LOCATION} ${JSONNET_TEMPLATE_LOCATION} > ${DESTINATION_RESULTING_JSON_FILE}
```

Or using the library directly downloaded from Grafonnet repository:
```bash
jsonnet -J vendor ${DASHBOARD_TEMPLATE_NAME}.jsonnet
```

## Import Dashboards into Grafana With Curl
```bash
apikey=${GRAFANA_SERVICE_ACCOUNT_TOKEN}
header="Content-Type: application/json"
endpoint_create_dash="http://localhost:3000/api/dashboards/db"
json_location=${RESULT_JSON_LOCATION}
curl -X POST $endpoint_create_dash \
     -H $header \
     -H "Authorization: Bearer $apikey" \
     -d @$json_location
```

## Example of JSONNet dashboard template definition
```json
local grafana = import '../grafonnet-lib/grafonnet/grafana.libsonnet';
local dashboard = grafana.dashboard;
local graph = grafana.graphPanel;
local prometheus = grafana.prometheus;

dashboard.new(
    'Services Resources Usage',
    timezone = 'utc',
    schemaVersion = 16,
    time_from = 'now-1h',
    tags = [ 'cpu', 'compute' ],
    uid = 'services-cpu-usage'
)
.addPanel(
    graph.new(
        'CPU Usage on Service A',
        datasource = 'Prometheus'
    )
    .addTarget(
        prometheus.target(
            'rate(service_cpu_usage{service="service_A"}[5m])'
        )
    ),
    gridPos = { x: 0, y: 0, w: 24, h: 10 }
).
.addPanel(
    graph.new(
        'CPU Usage on Service B',
        datasource = 'Prometheus'
    )
    .addTarget(
        prometheus.target(
            'rate(service_cpu_usage{service="service_B"}[5m])'
        )
    ),
    gridPos = { x: 10, y: 10, w: 24, h: 10 }
)
.addPanel(
    graph.new(
        'CPU Usage on Service C',
        datasource = 'Prometheus'
    )
    .addTarget(
        prometheus.target(
            'rate(service_cpu_usage{service="service_C"}[5m])'
        )
    ),
    gridPos = { x: 15, y: 15, w: 24, h: 10 }
)
.addPanel(
    graph.new(
        'CPU Usage on All Services',
        datasource = 'Prometheus'
    )
    .addTarget(
        prometheus.target(
            'rate(service_cpu_usage{job="pushgateway"}[5m])'
        )
    ),
    gridPos = { x: 20, y: 20, w: 24, h: 10 }
)
```