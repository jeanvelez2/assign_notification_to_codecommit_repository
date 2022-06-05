import os
import boto3

# Variables
notifications = boto3.client("codestar-notifications")
filter_result = {}
detail_type = 'FULL'
status = 'ENABLED'
tags = {'Creator': '<Add your name>'}

# https://docs.aws.amazon.com/dtconsole/latest/userguide/concepts.html#events-ref-repositories
event_type_ids = [
    "codecommit-repository-comments-on-commits",
    "codecommit-repository-comments-on-pull-requests",
    "codecommit-repository-approvals-status-changed",
    "codecommit-repository-approvals-rule-override",
    "codecommit-repository-pull-request-created",
    "codecommit-repository-pull-request-source-updated",
    "codecommit-repository-pull-request-status-changed",
    "codecommit-repository-pull-request-merged",
    "codecommit-repository-branches-and-tags-created",
    "codecommit-repository-branches-and-tags-deleted",
    "codecommit-repository-branches-and-tags-updated"
]

# Environment variables
sns_arn = os.environ["SNS_ARN"]

def lambda_handler(event, context):
    repository_arn = event["detail"]["responseElements"]["repositoryMetadata"]["arn"]
    repository_name = event["detail"]["responseElements"]["repositoryMetadata"]["repositoryName"]
    create_notification_rule(repository_name, repository_arn, sns_arn)
    print("Notification sucessfully configured for " + repository_arn)
    return {"status": "Notification sucessfully configured for " + repository_arn}

# Create codestar notification on codecommit repository
def create_notification_rule(name, resource, sns_arn):
    return notifications.create_notification_rule(
        Name=name,
        EventTypeIds= event_type_ids,
        Resource=resource,
        Targets=[
            {
                'TargetType': 'SNS',
                'TargetAddress': sns_arn
            },
        ],
        DetailType=detail_type,
        Tags=tags,
        Status=status
    )