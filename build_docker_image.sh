

AWS_ACCESS_KEY=$(cat ~/.aws/credentials  | grep aws_access_key | cut -d "="-f 2 | awk '{S1=s1};1')
AWS_SECRET_ACCESS_KEY=$(cat ~/.aws/credentials  | grep aws_secret_access_key | cut -d "="-f 2 | awk '{S1=s1};1')

docker build -t environment: academy-capstone-winter-2022 .
