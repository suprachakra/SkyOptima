// outputs.tf: Outputs key infrastructure details after deployment.

output "instance_id" {
  description = "The ID of the SkyOptima EC2 instance"
  value       = aws_instance.skyoptima_app.id
}

output "public_ip" {
  description = "The public IP address of the SkyOptima EC2 instance"
  value       = aws_instance.skyoptima_app.public_ip
}

output "data_bucket_arn" {
  description = "The ARN of the S3 bucket for SkyOptima data"
  value       = aws_s3_bucket.skyoptima_data.arn
}
