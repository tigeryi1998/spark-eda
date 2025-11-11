# Containerfile

# Base image (includes Python, Java, Spark, Jupyter)
# Using the Spark version 3.5.0  
# Using Scala version 2.12.18, OpenJDK 64-Bit Server VM, 17.0.8.1
# https://hub.docker.com/r/jupyter/pyspark-notebook/tags?name=spark 

FROM jupyter/pyspark-notebook:spark-3.5.0 


# environment variables

ENV JUPYTER_PORT=8888
ENV SPARK_UI_PORT=4040

ENV KAFKA_BROKER=kafka:9092
ENV KAFKA_TOPIC=covid_data


# working directory

WORKDIR /home/jovyan


# install python dependencies

COPY requirements.txt ./work
RUN pip install --no-cache-dir -r ./work/requirements.txt


# copy application code

COPY . ./work


# expose ports

EXPOSE 8888
EXPOSE 4040


# command to run the application

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--NotebookApp.token=", "--NotebookApp.password="]
