# app.py
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

# Configure the tracer to export traces to Tempo
tracer_provider = TracerProvider()
tracer_provider.add_span_processor(
    BatchSpanProcessor(OTLPSpanExporter(endpoint="http://your-tempo-instance:4317", insecure=True))
)
trace.set_tracer_provider(tracer_provider)

# Start a trace
tracer = trace.get_tracer(__name__)
with tracer.start_as_current_span("example-span"):
    # Your application logic here
    print("Hello, OpenTelemetry!")
