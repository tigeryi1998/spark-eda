# Spark + Kafka EDA Project (OpenShift Deployment)

This project demonstrates a complete streaming workflow:

-   A **Python Kafka Producer** streams rows from a large CSV file.
-   A **Kafka broker** stores the stream.
-   A **PySpark Notebook** running on OpenShift consumes Kafka messages
    for EDA.
-   The whole pipeline can run **locally with Podman Compose** or
    **fully on OpenShift** using Kubernetes YAML and BuildConfigs.

[Github URL](https://github.com/tigeryi1998/spark-eda)

## 📁 Project Structure

``` text
spark-eda/
├── customers-1000000.csv (NOT on Github)            
├── docker-compose.yml               
├── README.md                        
│
├── producer/                        
│   ├── Containerfile
│   ├── producer.py
│   └── requirements.txt
│
├── eda/                             
│   ├── Containerfile
│   ├── csv-eda.ipynb
│   ├── kafka-eda.ipynb
│   └── requirements.txt
│
└── k8s/                             
    ├── buildconfig-producer.yaml
    ├── buildconfig-notebook.yaml
    ├── kafka-deployment.yaml
    ├── kafka-service.yaml
    ├── kafka-data-persistentvolumeclaim.yaml
    ├── producer-deployment.yaml
    ├── notebook-deployment.yaml
    ├── notebook-service.yaml
```

## 🚀 Deploying on OpenShift

### 1. Login

``` bash
oc login --token=<TOKEN> --server=<cluster-api-url>

oc login --token=<TOKEN> --server=https://api.edu.nerc.mghpcc.org:6443
```

### 2. Check project

``` bash
# create a project (NOT allowed on NERC)
# oc new-project spark-eda

oc project
# Using project "ds551-2025fall-cb9303" on server "https://api.edu.nerc.mghpcc.org:6443".
```

## 🏗️ Step 1 --- Build Images for Kakfa Producer and EDA Notebook

``` bash
oc apply -f k8s/buildconfig-producer.yaml
oc apply -f k8s/buildconfig-notebook.yaml
```

Start builds: (Optional) it will automatically build from Git

``` bash
oc start-build kafka-producer --follow
oc start-build spark-eda-notebook --follow
```

## 🧱 Step 2 --- Deploy Kafka (KRaft mode)

``` bash
oc apply -f k8s/kafka-data-persistentvolumeclaim.yaml
oc apply -f k8s/kafka-deployment.yaml
oc apply -f k8s/kafka-service.yaml
```

## 🚚 Step 3 --- Deploy Kafka Producer

``` bash
oc apply -f k8s/producer-deployment.yaml
```

Logs:

``` bash
oc get pod
oc get deployment
oc logs -f deployment/kafka-producer
```

## 📓 Step 4 --- Deploy Notebook

``` bash
oc apply -f k8s/notebook-deployment.yaml
oc apply -f k8s/notebook-service.yaml
```

Get route:

``` bash
oc get route spark-eda-notebook
# https://jupyter-ds551-2025fall-cb9303.apps.edu.nerc.mghpcc.org
```

You can also use the Openshift UI to find the URL link launch the Jupyter Notebook



## 🖥️ Local Option: Podman Compose

``` bash
podman-compose build
podman-compose up -d
```

Check producer logs:

``` bash
podman logs -f spark-eda-producer-1
```

Shutdown
``` bash
podman-compose down -v 
```

## 📊 Notebooks

-   **csv-eda.ipynb**\
-   **kafka-eda.ipynb**

## 🔮 Future Work

-   Structured Streaming on OpenShift
-   Schema Registry
-   Airflow or Kafka Connect integration

## 📜 License

Apache 2.0
