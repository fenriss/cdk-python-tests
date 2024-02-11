# Authenticate with Artifactory

`docker login my-artifactory-repo -u my-username -p my-password`

# Pull the Docker image

`docker pull my-artifactory-repo/my-image:my-tag`

# Authenticate with Amazon ECR

`aws ecr get-login-password --region region | docker login --username AWS --password-stdin my-account-id.dkr.ecr.region.amazonaws.com`

# Tag the Docker image with the ECR repository URI

`docker tag my-artifactory-repo/my-image:my-tag my-account-id.dkr.ecr.region.amazonaws.com/my-ecr-repo:my-tag`

# Push the Docker image to the ECR repository

`docker push my-account-id.dkr.ecr.region.amazonaws.com/my-ecr-repo:my-tag`

# Make Lambda from ECR URI

`aws_lambda.DockerImageFunction(
    self,
    "MyLambdaFunction",
    code=aws_lambda.DockerImageCode.from_ecr(
        repository_uri="my-account-id.dkr.ecr.region.amazonaws.com/my-ecr-repo",
        tag="my-tag"
    )
)`
