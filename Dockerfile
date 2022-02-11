FROM public.ecr.aws/dataminded/spark-k8s-glue:v3.1.2-hadoop-3.3.1
WORKDIR ~/wetl
COPY ./requirements.txt .
RUN pip install -r ./requirements.txt -h
COPY ./Pyspark .
RUN python3 ./Pyspark/gettingdatafroms3.py
