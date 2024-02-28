#!/bin/bash

# run this script using ./scripts/main.sh <workspace_name> <resource_group_name> <location>
# e.g. ./scripts/main.sh csuazureopensource csu-nl-azure-opensource westeurope

# arg_1 = workspace_name, arg_2 = resource_group_name, arg_3 = location

WORKSPACE = $1
RESOURCE_GROUP = $2
LOCATION = $3

# echo start of deployment

echo "Starting deployment of azure resources..."

# Create a resource group
az group create --name $RESOURCE_GROUP --location $LOCATION

# Create a workspace
az ml workspace create --workspace-name $WORKSPACE --resource-group $RESOURCE_GROUP --location $LOCATION

# Get the workspace details
az ml workspace show --resource-group $RESOURCE_GROUP --workspace-name $WORKSPACE

# configure defaults
az configure --defaults group=$RESOURCE_GROUP workspace=$WORKSPACE location=$LOCATION

# echo end of deployment
echo "Done."


echo "Download open-source model. (1/4)"
./scripts/download_model.sh

echo "Push model artifact to Azure ML workspace. (2/4)"
./scripts/push_model_as_artifact.sh

echo "Deploy azure ml endpoint. (3/4)"
./scripts/deploy_endpoint.sh

echo "Deploy azure ml deployment. (4/4)"
./scripts/deploy_deployment.sh

echo "Done."



