resource "aws_lambda_function" "fitzroy_lambda" {
  filename      = "${local.lambda_archive_filename}"
  function_name = "fitzroy_lambda"
  role          = aws_iam_role.iam_for_lambda.arn
  handler       = "fitzroy.handle_event"

  source_code_hash = filebase64sha256("${local.lambda_archive_filename}")

  runtime = "python3.9"

  environment {
    variables = {
      TEST_URL = var.test_url
    }
  }
}
