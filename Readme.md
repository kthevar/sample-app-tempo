# Python Application with OpenTelemetry and Docker

This guide provides instructions on how to containerize a simple Python application with OpenTelemetry, which is configured to send trace data to Grafana Tempo.

## Prerequisites

- Docker installed on your machine.
- Access to a Grafana Tempo instance (replace the endpoint in the Python script accordingly).

```bash
docker build -t my-python-app .
docker run -d --name my-python-app-container my-python-app
docker run -d --name my-python-app-container -e TEMPO_ENDPOINT="http://localhost:4317" my-python-app

```

## Conclusion

After completing these steps, you will have a Docker container running your Python application, configured to send traces to Grafana Tempo.

---

You can include this `README.md` file in your project directory to provide clear instructions on how to set up and run your containerized Python application.