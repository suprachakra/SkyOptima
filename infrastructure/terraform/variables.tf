// variables.tf: Defines input variables for SkyOptima infrastructure.

variable "ami_id" {
  description = "The AMI ID for the EC2 instance"
  type        = string
}

variable "instance_type" {
  description = "The type of EC2 instance to launch"
  type        = string
  default     = "t3.medium"
}

variable "key_name" {
  description = "The SSH key name for accessing the EC2 instance"
  type        = string
}

variable "subnet_id" {
  description = "The Subnet ID for deploying the EC2 instance"
  type        = string
}

variable "security_group_id" {
  description = "The security group ID for the EC2 instance"
  type        = string
}

variable "data_bucket_name" {
  description = "The name of the S3 bucket for data storage"
  type        = string
}

variable "aws_region" {
  description = "The AWS region for deployment"
  type        = string
  default     = "us-east-1"
}
