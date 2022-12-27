# Databricks notebook source
# MAGIC %md
# MAGIC ### 1. Introduction
# MAGIC 
# MAGIC * In the previous notebooks, in order to read data from Azure Data Lake Storage Gen2, several methods were used:
# MAGIC   1. Mouting Azure containers to DBFS (throught `dbutils.fs.mount()` either with Account Key or SAS).
# MAGIC   2. Reading directly Azure container (through ``spark.conf.set('fs.azure.account.key.samydatalake.dfs.core.windows.net', dbutils.secrets.get('databricksScope','abfss-samydatalake'))``)
# MAGIC * In this notebook, a service principal 
# MAGIC   - will be created 
# MAGIC   - will get a role allowing Reading, Writing the Azure Account
# MAGIC * Unfortunately, no privilege was available to create Service Principal 
# MAGIC * Reference https://www.youtube.com/watch?v=bLHCnwvfU6A&list=PLMWaZteqtEaKi4WAePWtCSQCfQpvBT2U1&index=29

# COMMAND ----------

# MAGIC %md
# MAGIC ### 2. Create a Service Principal
# MAGIC 
# MAGIC 1. Navigate to: Azure Active Directory> App Registration > +New Registration 
# MAGIC 2. Create a name for the service Principal: DatabricksSevicePrincipal 
# MAGIC 3. Store the following variables:
# MAGIC   - the Application ID 
# MAGIC   - Secret
# MAGIC     * Azure Active Directory > DatabricksSevicePrincipal > Certificates & Secrets > +New Client Secret > the Variable Value is the password
# MAGIC 
# MAGIC ### 3. Role Assignment to the Service Principal
# MAGIC 
# MAGIC 1. Navigate to: Azure Storage Account (samydatalake) > IAM > Add Role Assignement > Storage Blob Data Contributor > +Select Member > DatabricksSevicePrincipal
# MAGIC 
# MAGIC ### 4. Create Secret in Azure Key Vault
# MAGIC 
# MAGIC 1. Navigate to: Azure Key Vault > Secrets > +Generate/Import > put the secret and the name of the Secret (that it will be named DatabricksSevicePrincipalSecret)
# MAGIC 
# MAGIC ### 5. Configure the spark session

# COMMAND ----------

spark.conf.set("fs.azure.account.auth.type.samydatalake.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.samydatalake.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.samydatalake.dfs.core.windows.net", "wr4re54re-4r5e45er4re-4r5e4r5er4")
spark.conf.set("fs.azure.account.oauth2.client.secret.samydatalake.dfs.core.windows.net", dbutils.secrets.get('amineScope','DatabricksSevicePrincipalSecret'))
spark.conf.set("fs.azure.account.oauth2.client.endpoint.samydatalake.dfs.core.windows.net", "https://login.microsoftonline.com/directory-id/oauth2/token")

# to get the directory-id: Navigate to Azure Active Directory > App Registration > Overview > get the value of Directory ID
# to get the application-id: Navigate to Azure Active Directory > App Registration > Overview > get the value of Application ID

##############################################
## Original version of the code
# spark.conf.set("fs.azure.account.auth.type.storage-account.dfs.core.windows.net", "OAuth")
# spark.conf.set("fs.azure.account.oauth.provider.type.storage-account.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
# spark.conf.set("fs.azure.account.oauth2.client.id.storage-account.dfs.core.windows.net", "application-id")
# spark.conf.set("fs.azure.account.oauth2.client.secret.storage-account.dfs.core.windows.net", service_credential)
# spark.conf.set("fs.azure.account.oauth2.client.endpoint.storage-account.dfs.core.windows.net", "https://login.microsoftonline.com/dir...")
