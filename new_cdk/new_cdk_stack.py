from aws_cdk import (
    # Duration,
    RemovalPolicy,
    Stack,
    # aws_sqs as sqs,
    aws_s3 as s3
)
from constructs import Construct
from . import lambda_service as lambda_service

class NewCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "NewCdkQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )

        s3.Bucket(self, "MyBucket", versioned=True,
            removal_policy=RemovalPolicy.DESTROY)
        
        lambda_service.LambdaService(self, "My Lambda Service")
        
    