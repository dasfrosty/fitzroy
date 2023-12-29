terraform {
  required_providers {
    local = {
      source = "hashicorp/local"
    }
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }

  backend "local" {
    path = "/etc/fitzroy/tfstate/terraform.tfstate"
  }
}

provider "aws" {
  region                   = "us-west-2"
  shared_credentials_files = ["~/.aws/credentials"]
  profile                  = "default"
}
