# .zip files

`cd my_lambda_function`

`pip install -r requirements.txt --target .`


# Docker

`cd docker_image`

### Retrieve an authentication token and authenticate your Docker client to your registry. Use the AWS CLI:

`aws ecr get-login-password --region eu-west-2 | docker login --username AWS --password-stdin 339712700454.dkr.ecr.eu-west-2.amazonaws.com`

### Build your Docker image using the following command:
`docker build -t model-prediction .`

`docker tag model-prediction:latest 339712700454.dkr.ecr.eu-west-2.amazonaws.com/model-prediction:latest`

### Run the following command to push this image to your newly created AWS repository:

`docker push 339712700454.dkr.ecr.eu-west-2.amazonaws.com/model-prediction:latest`
