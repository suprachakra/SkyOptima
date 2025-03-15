// main.tf: Provisions core infrastructure for SkyOptima on AWS.

resource "aws_instance" "skyoptima_app" {
  ami                    = var.ami_id
  instance_type          = var.instance_type
  key_name               = var.key_name
  subnet_id              = var.subnet_id
  vpc_security_group_ids = [var.security_group_id]

  tags = {
    Name    = "SkyOptima-App-Instance"
    Project = "SkyOptima"
  }
}

resource "aws_s3_bucket" "skyoptima_data" {
  bucket = var.data_bucket_name
  acl    = "private"

  tags = {
    Name    = "SkyOptima-Data-Bucket"
    Project = "SkyOptima"
  }
}
