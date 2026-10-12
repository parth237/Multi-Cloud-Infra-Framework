variable "environment" {
  description = "Target deployment environment"
  type        = string
  default     = "production"
}

variable "aws_region" {
  description = "Target AWS Region"
  type        = string
  default     = "us-east-1"
}

variable "aws_vpc_cidr" {
  description = "CIDR block for AWS VPC"
  type        = string
  default     = "10.100.0.0/16"
}

variable "aws_public_subnet_cidr" {
  description = "Public subnet CIDR for AWS"
  type        = string
  default     = "10.100.1.0/24"
}

variable "aws_private_subnet_cidr" {
  description = "Private subnet CIDR for AWS"
  type        = string
  default     = "10.100.2.0/24"
}

variable "azure_location" {
  description = "Target Azure Region"
  type        = string
  default     = "eastus"
}

variable "azure_vnet_cidr" {
  description = "CIDR block for Azure VNet"
  type        = string
  default     = "10.200.0.0/16"
}

variable "azure_app_subnet_cidr" {
  description = "Application subnet CIDR for Azure"
  type        = string
  default     = "10.200.1.0/24"
}

variable "azure_db_subnet_cidr" {
  description = "Database subnet CIDR for Azure"
  type        = string
  default     = "10.200.2.0/24"
}