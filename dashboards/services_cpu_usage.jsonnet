local grafana = import '../grafonnet-lib/grafonnet/grafana.libsonnet';
local dashboard = grafana.dashboard;
local graph = grafana.graphPanel;
local prometheus = grafana.prometheus;

dashboard.new(
    'Services Resources Usage',
    timezone = 'utc',
    schemaVersion = 14,
    time_from = 'now-1h'
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
)
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