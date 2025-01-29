local grafana = import '../grafonnet-lib/grafonnet/grafana.libsonnet';
local dashboard = grafana.dashboard;
local graph = grafana.graphPanel;
local prometheus = grafana.prometheus;

dashboard.new(
    'Resources Usage',
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