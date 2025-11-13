# spark-eda

This is the DS 551 lab on Spark EDA, followed by the Kakfa K8S lab. 

[Kakfa K8S URL link](https://github.com/tigeryi1998/kafka-k8s)

The dataset `customers-1000000.csv` is NOT included in this Github repo because of its 170 MB size. 

`producer.py` is the KafkaProducer python script to send this CSV data to Kafka. 

`customer.ipynb` is the notebook for the EDA on the 1M customers data. 

`health.ipynb` is the notebook for the EDA on the health event data. But the kafka broker no longer exist. 

`k8s/` folder contains the same Openshift Kubernetes K8S YAML files to start kakfa, producer, and consumer from the last lab. 


## Procedure 

The goal of the project is to first produce the data into Kafka producer. 

Then consume the data from Kakfa, either directly into Spark or via a kafka consumer.  

Eventually you want to perform some EDA analysis on the data. 

