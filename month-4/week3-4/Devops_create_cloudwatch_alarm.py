# Create a CloudWatch Alarm
# Problem: Create a CloudWatch alarm using Boto3 to monitor CPU utilization.
# Objective: Automate AWS monitoring tasks.

# create_cloudwatch_alarm.py
import boto3

def create_cloudwatch_alarm(instance_id, threshold, period, evaluation_periods):
    cloudwatch = boto3.client('cloudwatch')

    alarm_name = f"High_CPU_Utilization_{instance_id}"
    alarm_description = f"Alarm when CPU utilization exceeds {threshold}% for {evaluation_periods} periods"

    try:
        response = cloudwatch.put_metric_alarm(
            AlarmName=alarm_name,
            AlarmDescription=alarm_description,
            ActionsEnabled=True,
            MetricName='CPUUtilization',
            Namespace='AWS/EC2',
            Statistic='Average',
            Period=period,
            EvaluationPeriods=evaluation_periods,
            Threshold=threshold,
            ComparisonOperator='GreaterThanThreshold',
            Dimensions=[
                {
                    'Name': 'InstanceId',
                    'Value': instance_id
                },
            ],
            AlarmActions=[
                # Add your SNS Topic ARN here for notifications
                # 'arn:aws:sns:us-east-1:123456789012:YourSNSTopic'
            ],
            Unit='Percent'
        )

        print(f"Successfully created CloudWatch alarm: {alarm_name}")

    except Exception as e:
        print(f"Error creating CloudWatch alarm: {e}")

if __name__ == "__main__":
    instance_id = input("Enter the EC2 Instance ID: ")
    threshold = float(input("Enter the CPU utilization threshold (e.g., 80): "))
    period = int(input("Enter the period in seconds (e.g., 60): "))  # e.g., 60 seconds
    evaluation_periods = int(input("Enter the number of evaluation periods (e.g., 2): "))

    create_cloudwatch_alarm(instance_id, threshold, period, evaluation_periods)
