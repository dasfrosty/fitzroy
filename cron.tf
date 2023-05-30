resource "aws_cloudwatch_event_rule" "cron_schedule" {
  name                = "fitzroy_lambda_event_rule"
  schedule_expression = "cron(0 * * * ? *)"
}

resource "aws_cloudwatch_event_target" "cron_target" {
  rule = aws_cloudwatch_event_rule.cron_schedule.name
  arn  = aws_lambda_function.fitzroy_lambda.arn
}

resource "aws_lambda_permission" "allow_cloudwatch" {
  statement_id  = "AllowExecutionFromCloudWatch"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.fitzroy_lambda.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.cron_schedule.arn
}
