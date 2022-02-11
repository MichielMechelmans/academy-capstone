FROM public.ecr.aws/dataminded/spark-k8s-glue:v3.1.2-hadoop-3.3.1
WORKDIR ~/Pyspark
COPY ./requirements.txt
RUN pip install -r ./requirements.txt
RUN aws configure
COPY ./Pyspark
CMD [ "/bin/bash","python","Pyspark/gettingdatafroms3.py"]