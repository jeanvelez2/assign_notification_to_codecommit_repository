# Project: assign_notification_to_codecommit_repository
AWS Lambda function code (Python 3.9) that assigns an Amazon SNS Topic to AWS CodeCommit repositories through AWS CodeStar. 
Event source for the AWS Lambda function is an Amazon EventBridge Rule. 

# Setup (AWS):
https://medium.com/@jean.velez2/automate-notification-assignment-to-aws-codecommit-repositories-b787e003dafb

## Reference
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codestar-notifications.html#CodeStarNotifications.Client.create_notification_rule
