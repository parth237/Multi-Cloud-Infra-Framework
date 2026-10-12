output "aws_vpc_id" {
  description = "Provisioned AWS VPC ID"
  value       = module.aws_network.vpc_id
}

output "aws_security_group_id" {
  description = "Provisioned AWS Security Group ID"
  value       = module.aws_network.security_group_id
}

output "azure_vnet_id" {
  description = "Provisioned Azure VNet ID"
  value       = module.azure_network.vnet_id
}

output "azure_log_analytics_workspace_id" {
  description = "Provisioned Azure Log Analytics Workspace ID"
  value       = module.azure_network.log_analytics_workspace_id
}