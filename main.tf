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

resource "local_file" "fitzroy-py" {
  content_base64 = filebase64("fitzroy.py")
  filename       = "dist/package/fitzroy.py"
}

data "archive_file" "lambda" {
  depends_on = [local_file.fitzroy-py]

  type        = "zip"
  source_dir  = "dist/package"
  output_path = "dist/fitzroy_archive.zip"

}

resource "aws_lambda_function" "test_lambda" {
  filename      = "dist/fitzroy_archive.zip"
  function_name = "fitzroy_lambda"
  role          = aws_iam_role.iam_for_lambda.arn
  handler       = "fitzroy.handle_event"

  source_code_hash = data.archive_file.lambda.output_base64sha256

  runtime = "python3.9"

  environment {
    variables = {
      TEST_URL = var.test_url
    }
  }
}
