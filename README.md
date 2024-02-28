# azure-custom-llms-openai
Simple deployment of any open-source model behind an OpenAI interface


## Azure ML deployment
make sure to have the az cli installed.
In addition, 

az extension remove -n azure-cli-ml
az extension remove -n ml

and:
az extension add -n ml

and:
az extension update -n ml


list subscription


create resource group

set subscription and resource group

configure defaults for now

RG="<insert-resource-group>"

LOCATION="<insert-location>" e.g. westeurope

WORKSPACE="<insert-workspace-name>"

az configure --defaults group=$RG workspace=$WORKSPACE location=$LOCATION


show default configuration:
az configure -l -o table