import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_python_tests.cdk_python_tests_stack import CdkPythonTestsStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_python_tests/cdk_python_tests_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkPythonTestsStack(app, "cdk-python-tests")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
