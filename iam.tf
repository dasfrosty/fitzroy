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

data "aws_iam_policy_document" "sns_publish" {
  statement {
    effect   = "Allow"
    actions  = ["sns:Publish"]
    resources = [aws_sns_topic.fitzroy_notifications_topic.arn]
  }
}

resource "aws_iam_role" "iam_for_lambda" {
  name               = "iam_for_lambda"
  assume_role_policy = data.aws_iam_policy_document.assume_role.json
  inline_policy {
    name   = "sns_publish"
    policy = data.aws_iam_policy_document.sns_publish.json
  }
}
