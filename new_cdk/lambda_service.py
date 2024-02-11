import aws_cdk as cdk
from constructs import Construct
from aws_cdk import (aws_apigateway as apigateway,
                     aws_s3 as s3,
                     aws_lambda as lambda_)

class LambdaService(Construct):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        self.build_lambda_func()

    # https://dev.to/wesleycheek/deploy-a-docker-built-lambda-function-with-aws-cdk-fio
    def build_lambda_func(self):
        self.prediction_lambda = lambda_.DockerImageFunction(
            scope=self,
            id="ExampleDockerLambda2",
            # Function name on AWS
            function_name="ExampleDockerLambda2",
            # Use aws_cdk.aws_lambda.DockerImageCode.from_image_asset to build
            # a docker image on deployment
            code=lambda_.DockerImageCode.from_image_asset(
                # Directory relative to where you execute cdk deploy
                # contains a Dockerfile with build instructions
                directory="ExampleDockerLambda"
            ),
        )