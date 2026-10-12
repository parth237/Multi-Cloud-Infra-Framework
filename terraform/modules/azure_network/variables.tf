variable "environment" {
  description = "Environment name (e.g. dev, prod)"
  type        = string
  default     = "dev"
}

variable "location" {
  description = "Azure region"
  type        = string
  default     = "eastus"
}

variable "resource_group_name" {
  description = "Name of the Azure Resource Group"
  type        = string
  default     = "rg-multicloud-framework"
}

variable "vnet_cidr" {
  description = "CIDR space for Azure Virtual Network"
  type        = string
  default     = "10.200.0.0/16"
}

variable "app_subnet_cidr" {
  description = "CIDR for application subnet"
  type        = string
  default     = "10.200.1.0/24"
}

variable "db_subnet_cidr" {
  description = "CIDR for backend database subnet"
  type        = string
  default     = "10.200.2.0/24"
}