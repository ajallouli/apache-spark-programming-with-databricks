# Databricks notebook source
# MAGIC %md
# MAGIC ### 1. Introduction
# MAGIC 
# MAGIC * In the previous notebooks, in order to read data from Azure Data Lake Storage Gen2, the azure containers were mounted to DBFS.
# MAGIC * Mounting these containers relied on `dbutils.fs.mount()` based on storage account key that is saved in a secret scope (which could be backed by `Azure Key Vault` or `Azure Databricks`).
# MAGIC * Consequently, the data URL will be starting by `dbfs:/`
# MAGIC * The objetive of this notebook is accessing data directly from Azure Data Lake Storage Gen2 without mounting the container.
# MAGIC   - in that case, the data URL will be starting by `abfss://`

# COMMAND ----------

# MAGIC %md
# MAGIC ### 2. Creating a Azure Container
# MAGIC 
# MAGIC ```sh
# MAGIC az storage container create \
# MAGIC --name abfssdata \
# MAGIC --account-name samydatalake
# MAGIC ```

# COMMAND ----------

# MAGIC %md
# MAGIC ### 3. List of the Secret Scope
# MAGIC 
# MAGIC ```sh
# MAGIC databricks secrets list-scopes
# MAGIC Scope            Backend         KeyVault URL
# MAGIC ---------------  --------------  ---------------------------------------------
# MAGIC amineScope       AZURE_KEYVAULT  https://akv-databricks-amine.vault.azure.net/
# MAGIC databricksScope  DATABRICKS      N/A
# MAGIC ```

# COMMAND ----------

# MAGIC %md
# MAGIC ### 4. Getting the key of the Storage Account
# MAGIC ```sh
# MAGIC az storage account keys list --account-name samydatalake --resource-group rg-databricks-workspace
# MAGIC # [
# MAGIC #   {
# MAGIC #     "creationTime": "2022-12-24T20:51:22.853764+00:00",
# MAGIC #     "keyName": "key1",
# MAGIC #     "permissions": "FULL",
# MAGIC #     "value": "0dKCtjwpYydMBF0EjGoL58N2dVkBmio2N4QVBLg/5++J+/pHmZ4dQvjW/WV+xdjLekIrNLQdioUb+AStkAuxNw=="
# MAGIC #   },
# MAGIC #   {
# MAGIC #     "creationTime": "2022-12-24T20:51:22.853764+00:00",
# MAGIC #     "keyName": "key2",
# MAGIC #     "permissions": "FULL",
# MAGIC #     "value": "HMS3l5EbDelShzfVq5SMRMPB9rtuCHbcS1UNvF5GinpHfUse6dDQak1XetUIos9TQ+j/Hk3G0bm5+AStgaO6+g=="
# MAGIC #   }
# MAGIC # ]
# MAGIC ```

# COMMAND ----------

# MAGIC %md
# MAGIC ### 5. Put a secret in Secret Scope
# MAGIC 
# MAGIC ```sh
# MAGIC # Put the secret
# MAGIC databricks secrets put --scope databricksScope --key abfss-samydatalake
# MAGIC 
# MAGIC # list the secrets for the the scope databricksScope
# MAGIC databricks secrets list --scope databricksScope
# MAGIC # Key name              Last updated
# MAGIC # ------------------  --------------
# MAGIC # abfss-samydatalake   1672096155800
# MAGIC # dbkey-sanydatalake   1672091011510
# MAGIC 
# MAGIC 
# MAGIC ```

# COMMAND ----------

# MAGIC %md 
# MAGIC ### 6. Configure Spark to access the Azure Data Lake Storage Gen2

# COMMAND ----------

spark.conf.set('fs.azure.account.key.samydatalake.dfs.core.windows.net', dbutils.secrets.get('databricksScope','abfss-samydatalake'))

# COMMAND ----------

df = spark.read.csv('abfss://abfssdata@samydatalake.dfs.core.windows.net/LU_isic.csv',header=True)

# COMMAND ----------

display(df)
