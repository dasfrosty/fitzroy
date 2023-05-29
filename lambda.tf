resource "aws_lambda_function" "fitzroy_lambda" {
  filename      = local.lambda_archive_filename
  function_name = "fitzroy_lambda"
  role          = aws_iam_role.iam_for_lambda.arn
  handler       = "fitzroy.handle_event"

  source_code_hash = filebase64sha256("${local.lambda_archive_filename}")

  runtime = "python3.9"

  environment {
    variables = {
      PRODUCT_URL    = var.product_url
      LINK_URL       = var.link_url
      EXPECTED_PRICE = var.expected_price
      SNS_TOPIC_ARN  = aws_sns_topic.fitzroy_notifications_topic.arn
    }
  }
}

resource "aws_cloudwatch_log_group" "fitzroy_lambda_logs" {
  name              = "/aws/lambda/${aws_lambda_function.fitzroy_lambda.function_name}"
  retention_in_days = 180
}
