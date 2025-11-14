# Spark + Kafka EDA Project

This project demonstrates a full workflow for streaming CSV data into Kafka using a Python producer, consuming and analyzing the data using PySpark in Jupyter notebooks, and running services locally using **Podman Compose**. Kubernetes manifests are included but not fully wired yet.

---

## 📁 Project Structure

```text
spark-eda/
├── customers-1000000.csv       # Large CSV dataset used by the producer
├── docker-compose.yml          # Podman/Docker Compose services (Kafka, Producer, EDA)
├── README.md                   # Project documentation
├── producer/                   # Kafka Producer container
│   ├── Containerfile
│   ├── producer.py
│   └── requirements.txt
├── eda/                        # Spark / Jupyter analysis container
│   ├── Containerfile
│   ├── csv-eda.ipynb           # Local CSV EDA
│   ├── kafka-eda.ipynb         # Kafka → Spark decoding + analysis
│   └── requirements.txt
└── k8s/                        # Kubernetes YAML files (WIP)
    ├── buildconfig-producer.yaml
    ├── kafka-deployment.yaml
    ├── kafka-data-persistentvolumeclaim.yaml
    ├── kafka-service.yaml
    └── producer-deployment.yaml
```

---

## 🚀 Running Services with Podman Compose

### **1. Build and start all containers**
```bash
podman-compose up --build -d
```
This starts:
- **Kafka broker**
- **Producer container** (streams CSV → Kafka)
- **EDA container** (Jupyter environment)

---

## 🧪 Testing the Kafka Producer

The producer reads:
```
/app/customers-1000000.csv
```
And sends rows to Kafka topic `customer`.

Check producer logs:
```bash
podman logs -f spark-eda-producer-1
```

---

## 📊 Running EDA in Jupyter Notebook

The **eda** container exposes JupyterLab.

Find the container:
```bash
podman ps
```
Then inspect Jupyter token:
```bash
podman logs <eda-container-name>
```
Open the printed Jupyter URL in your browser.

### Notebooks:
- **csv-eda.ipynb** → EDA directly on CSV
- **kafka-eda.ipynb** →
  - Consume Kafka
  - Decode JSON strings using PySpark UDF
  - Extract columns
  - Run analytics

---

## 🧱 Kubernetes (WIP)
YAMLs for Kafka and the producer exist in the `k8s/` folder but are not linked to EDA yet. Future improvements may include:
- Deploying Kafka + Producer in OpenShift
- Adding a Spark deployment
- Using BuildConfig to build images

---

## 📝 Notes
- The project uses **Podman** instead of Docker, but `docker-compose.yml` works with Podman directly.
- Two separate containers are used for Producer and EDA.
- CSV path is mounted into containers via volume.
- Kafka producer runs asynchronously and flushes periodically.

---

## 🔮 Future Enhancements
- Kubernetes consumer/EDA deployment
- Add Spark Structured Streaming notebook
- Add schema registry
- Add Airflow or Kafka Connect pipeline

---

## 🤝 Contributing
Feel free to open issues or extend the notebooks.

---

## 📜 License
Apache 