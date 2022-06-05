# Project: assign_notification_to_codecommit_repository
AWS Lambda function code (Python 3.9) that assigns an Amazon SNS Topic to AWS CodeCommit repositories through AWS CodeStar. 
Event source for the AWS Lambda function is an Amazon EventBridge Rule. 

# Setup (AWS):


## Reference
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications.html#CodeStarNotifications.Client.create_notification_rule