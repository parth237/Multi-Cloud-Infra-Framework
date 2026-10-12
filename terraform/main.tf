terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

# 1. AWS Provider Configuration
provider "aws" {
  region = var.aws_region
  default_tags {
    tags = {
      Environment = var.environment
      ManagedBy   = "Terraform"
      Project     = "Multi-Cloud-Framework"
    }
  }
}

# 2. Azure Provider Configuration
provider "azurerm" {
  features {}
}

# 3. Call Reusable AWS Network Module
module "aws_network" {
  source             = "./modules/aws_network"
  environment        = var.environment
  vpc_cidr           = var.aws_vpc_cidr
  public_subnet_cidr = var.aws_public_subnet_cidr
  private_subnet_cidr= var.aws_private_subnet_cidr
}

# 4. Call Reusable Azure Network Module
module "azure_network" {
  source          = "./modules/azure_network"
  environment     = var.environment
  location        = var.azure_location
  vnet_cidr       = var.azure_vnet_cidr
  app_subnet_cidr = var.azure_app_subnet_cidr
  db_subnet_cidr  = var.azure_db_subnet_cidr
}