resource "aws_sns_topic" "fitzroy_notifications_topic" {
  name = "fitzroy-notifications-topic"
}

resource "aws_sns_topic_subscription" "fitzroy_notifications_subscription" {
  topic_arn = aws_sns_topic.fitzroy_notifications_topic.arn
  protocol  = "email"
  endpoint  = var.notification_email_address
}

resource "aws_sns_topic_subscription" "fitzroy_zapier_subscription" {
  topic_arn = aws_sns_topic.fitzroy_notifications_topic.arn
  protocol  = "email"
  endpoint  = var.zapier_email_address
}
