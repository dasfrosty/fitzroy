data "aws_iam_policy_document" "assume_role" {
  statement {
    effect = "Allow"

    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }

    actions = ["sts:AssumeRole"]
  }
}

resource "aws_iam_role" "iam_for_lambda" {
  name               = "iam_for_lambda"
  assume_role_policy = data.aws_iam_policy_document.assume_role.json
}

data "archive_file" "lambda" {
  type        = "zip"
  source_file = "fitzroy.py"
  output_path = "fitzroy_archive.zip"
}

resource "aws_lambda_function" "test_lambda" {
  filename      = "fitzroy_archive.zip"
  function_name = "fitzroy_lambda"
  role          = aws_iam_role.iam_for_lambda.arn
  handler       = "fitzroy.lambda_handler"

  source_code_hash = data.archive_file.lambda.output_base64sha256

  runtime = "python3.7"

  environment {
    variables = {
      TEST_URL = var.test_url
    }
  }
}
