

ACCESS_KEY=$(cat ~/.aws/credentials  | grep aws_access_key | cut -d "="-f 2 | awk '{S1=s1};1')
SECRET_ACCESS_KEY=$(cat ~/.aws/credentials  | grep aws_secret_access_key | cut -d "="-f 2 | awk '{S1=s1};1')
DEFAULT_REGION="eu-west-1"

docker run -it --env AWS_ACCESS_KEY=$ACCESS_KEY --env AWS_SECRET_ACCESS_KEY=$SECRET_ACCESS_KEY --env AWS_DEFAULT_REGION=$DEFAULT_REGION environment:academy-capstone-winter-2022 
