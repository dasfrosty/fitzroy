variable "product_url" {
  type     = string
  nullable = false
}

variable "link_url" {
  type     = string
  nullable = false
}

variable "desired_color" {
  type     = string
  nullable = false
}

variable "expected_price" {
  type     = string
  nullable = false
}

variable "cron_schedule_utc" {
  type     = string
  nullable = false
}

variable "notification_email_address" {
  type     = string
  nullable = false
}

variable "zapier_email_address" {
  type     = string
  nullable = false
}
