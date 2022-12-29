# Databricks notebook source
# MAGIC %md
# MAGIC ### 1. Create Azure Resource Group
# MAGIC 
# MAGIC ```sh
# MAGIC # 1. Creation of the resource group
# MAGIC az group create --location eastus --name rg-databricks-workspace 
# MAGIC ```

# COMMAND ----------

# MAGIC %md
# MAGIC ### 2. Create Azure Databricks Workspace
# MAGIC 
# MAGIC ```sh
# MAGIC # 2. Create a databricks workspace
# MAGIC az databricks workspace create --resource-group rg-databricks-workspace --name mydatabricks-workspace --location eastus --sku standard
# MAGIC 
# MAGIC # The command requires the extension databricks. Do you want to install it now? The command will continue to run after the extension is installed. (Y/n): Y
# MAGIC # Run 'az config set extension.use_dynamic_install=yes_without_prompt' to allow installing extensions without prompt.
# MAGIC # {
# MAGIC #   "authorizations": [
# MAGIC #     {
# MAGIC #       "principalId": "9a74af6f-d153-4348-988a-e2672920bee9",
# MAGIC #       "roleDefinitionId": "8e3af657-a8ff-443c-a75c-2fe8c4bcb635"
# MAGIC #     }
# MAGIC #   ],
# MAGIC #   "createdBy": {
# MAGIC #     "applicationId": "04b07795-8ddb-461a-bbee-02f9e1bf7b46",
# MAGIC #     "oid": "f735b166-77d7-4ede-bd91-18cbfb3a3de9",
# MAGIC #     "puid": "10032001A6F4D365"
# MAGIC #   },
# MAGIC #   "createdDateTime": "2022-12-23T22:05:30.470814+00:00",
# MAGIC #   "encryption": null,
# MAGIC #   "id": "/subscriptions/798b9fd2-5b3f-4302-88c3-c4eb676053bc/resourceGroups/rg-databricks-workspace/providers/Microsoft.Databricks/workspaces/mydatabricks-workspace",
# MAGIC #   "location": "eastus",
# MAGIC #   "managedResourceGroupId": "/subscriptions/798b9fd2-5b3f-4302-88c3-c4eb676053bc/resourceGroups/databricks-rg-mydatabricks-workspace-xso0p2i411fic",
# MAGIC #   "name": "mydatabricks-workspace",
# MAGIC #   "parameters": {
# MAGIC #     "amlWorkspaceId": null,
# MAGIC #     "customPrivateSubnetName": null,
# MAGIC #     "customPublicSubnetName": null,
# MAGIC #     "customVirtualNetworkId": null,
# MAGIC #     "enableFedRampCertification": {
# MAGIC #       "type": "Bool",
# MAGIC #       "value": false
# MAGIC #     },
# MAGIC #     "enableNoPublicIp": {
# MAGIC #       "type": "Bool",
# MAGIC #       "value": false
# MAGIC #     },
# MAGIC #     "encryption": null,
# MAGIC #     "loadBalancerBackendPoolName": null,
# MAGIC #     "loadBalancerId": null,
# MAGIC #     "natGatewayName": {
# MAGIC #       "type": "String",
# MAGIC #       "value": "nat-gateway"
# MAGIC #     },
# MAGIC #     "prepareEncryption": {
# MAGIC #       "type": "Bool",
# MAGIC #       "value": false
# MAGIC #     },
# MAGIC #     "publicIpName": {
# MAGIC #       "type": "String",
# MAGIC #       "value": "nat-gw-public-ip"
# MAGIC #     },
# MAGIC #     "relayNamespaceName": {
# MAGIC #       "type": "String",
# MAGIC #       "value": "dbrelayfte22rjfjh2tc"
# MAGIC #     },
# MAGIC #     "requireInfrastructureEncryption": {
# MAGIC #       "type": "Bool",
# MAGIC #       "value": false
# MAGIC #     },
# MAGIC #     "resourceTags": {
# MAGIC #       "type": "Object",
# MAGIC #       "value": {
# MAGIC #         "application": "databricks",
# MAGIC #         "databricks-environment": "true"
# MAGIC #       }
# MAGIC #     },
# MAGIC #     "storageAccountName": {
# MAGIC #       "type": "String",
# MAGIC #       "value": "dbstoragefte22rjfjh2tc"
# MAGIC #     },
# MAGIC #     "storageAccountSkuName": {
# MAGIC #       "type": "String",
# MAGIC #       "value": "Standard_GRS"
# MAGIC #     },
# MAGIC #     "vnetAddressPrefix": {
# MAGIC #       "type": "String",
# MAGIC #       "value": "10.139"
# MAGIC #     }
# MAGIC #   },
# MAGIC #   "privateEndpointConnections": null,
# MAGIC #   "provisioningState": "Succeeded",
# MAGIC #   "publicNetworkAccess": null,
# MAGIC #   "requiredNsgRules": null,
# MAGIC #   "resourceGroup": "rg-databricks-workspace",
# MAGIC #   "sku": {
# MAGIC #     "name": "standard",
# MAGIC #     "tier": null
# MAGIC #   },
# MAGIC #   "storageAccountIdentity": null,
# MAGIC #   "systemData": null,
# MAGIC #   "tags": null,
# MAGIC #   "type": "Microsoft.Databricks/workspaces",
# MAGIC #   "uiDefinitionUri": null,
# MAGIC #   "updatedBy": {
# MAGIC #     "applicationId": "04b07795-8ddb-461a-bbee-02f9e1bf7b46",
# MAGIC #     "oid": "f735b166-77d7-4ede-bd91-18cbfb3a3de9",
# MAGIC #     "puid": "10032001A6F4D365"
# MAGIC #   },
# MAGIC #   "workspaceId": "744973935127893",
# MAGIC #   "workspaceUrl": "adb-744973935127893.13.azuredatabricks.net"
# MAGIC # }
# MAGIC ```
