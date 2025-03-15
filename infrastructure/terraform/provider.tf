// provider.tf: Configures the AWS provider for Terraform.

provider "aws" {
  region  = var.aws_region
  version = "~> 3.0"
}
