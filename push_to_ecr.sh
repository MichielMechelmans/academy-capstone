#!bin/bash
ACCESS_KEY_ID=$(cat ~/.aws/credentials | grep aws_access_key | cut -d "=" -f 2 | awk '{$1=$1};1')
SECRET_ACCESS_KEY=$(cat ~/.aws/credentials | grep aws_secret_access_key | cut -d "=" -f 2 | awk '{$1=$1};1')
REGION="eu-west-1"
DEFAULT_REGION="eu-west-1"

aws ecr get-login-password --region $REGION | docker login --username AWS --password-stdin $ACCESS_KEY_ID.dkr.ecr.$REGION.amazonaws.com
# run "docker images"in the terminal to identify the image ID 

docker push $ACCESS_KEY_ID.dkr.ecr.$REGION.amazonaws.com/my-repository:tag