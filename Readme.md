# Python Application with OpenTelemetry and Docker

This guide provides instructions on how to containerize a simple Python application with OpenTelemetry, which is configured to send trace data to Grafana Tempo.

## Prerequisites

- Docker installed on your machine.
- Access to a Grafana Tempo instance (replace the endpoint in the Python script accordingly).

## Step 1: Prepare the Python Application

Create a file named `app.py` with the following content:

```python
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
```
Replace `http://your-tempo-instance:4317` with your Grafana Tempo instance's endpoint.

## Step 2: Create a Requirements File

Create a `requirements.txt` file to list the necessary Python packages:

```
opentelemetry-api
opentelemetry-sdk
opentelemetry-exporter-otlp
```

## Step 3: Dockerfile

Create a Dockerfile for building your Docker image:

```Dockerfile
# Dockerfile
FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

CMD [ "python", "./app.py" ]
```

## Step 4: Build and Run the Docker Container

Build the Docker image and run it as a container:

```bash
docker build -t my-python-app .
docker run -d --name my-python-app-container my-python-app
```

## Conclusion

After completing these steps, you will have a Docker container running your Python application, configured to send traces to Grafana Tempo.

---

You can include this `README.md` file in your project directory to provide clear instructions on how to set up and run your containerized Python application.