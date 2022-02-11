#!/bin/sh


REGION="eu-west-1"


aws ecr get-login-password --region $REGION | docker login --username AWS --password-stdin 338791806049.dkr.ecr.$REGION.amazonaws.com
# run "docker images"in the terminal to identify the image ID 

docker push 338791806049.dkr.ecr.$REGION.amazonaws.com/michielwinterschool