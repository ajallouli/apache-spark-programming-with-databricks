# Databricks notebook source
# MAGIC %md
# MAGIC ### 1. Overview on Secret Scopes
# MAGIC 
# MAGIC There are 2 methods to back the secret scopes for Databricks:
# MAGIC 1. Azure Key Vault
# MAGIC 2. Azure Databricks
# MAGIC 
# MAGIC The previous notebook showed how to create secret scope which is backed by Azure Key Vault.
# MAGIC 
# MAGIC The list of secret scope are:
# MAGIC 
# MAGIC ```sh
# MAGIC databricks secrets list-scopes
# MAGIC # Scope       Backend         KeyVault URL
# MAGIC # ----------  --------------  ---------------------------------------------
# MAGIC # amineScope  AZURE_KEYVAULT  https://akv-databricks-amine.vault.azure.net/
# MAGIC 
# MAGIC ```

# COMMAND ----------

# MAGIC %md ### 2.  Create a secret scope with databricks CLI
# MAGIC 
# MAGIC **Creating the secret scope (default param of the databricks CLI)**
# MAGIC ```sh
# MAGIC databricks secrets create-scope --scope databricksScope
# MAGIC # Error: b'{"error_code":"BAD_REQUEST","message":"Premium Tier is disabled in this workspace. Secret scopes can only be created with initial_manage_principal \\"users\\"."}'
# MAGIC ```
# MAGIC 
# MAGIC The deployed Azure Databricks is Standard Tier. Consequently, it is not possible to create a scope with --initial-manage-principal "creator", which comes with the Premium Tier.
# MAGIC 
# MAGIC **Creating the secret scope (Standard Tier)**
# MAGIC 
# MAGIC ```sh
# MAGIC databricks secrets create-scope --scope databricksScope --initial-manage-principal users
# MAGIC ```
# MAGIC 
# MAGIC **Checking if secret scope is created**
# MAGIC 
# MAGIC ```sh
# MAGIC databricks secrets list-scopes
# MAGIC # Scope            Backend         KeyVault URL
# MAGIC # ---------------  --------------  ---------------------------------------------
# MAGIC # amineScope       AZURE_KEYVAULT  https://akv-databricks-amine.vault.azure.net/
# MAGIC # databricksScope  DATABRICKS      N/A
# MAGIC 
# MAGIC ```

# COMMAND ----------

# MAGIC %md
# MAGIC ### 3. Creating a key in the Azure Databricks backed Secret Scope
# MAGIC 
# MAGIC ```sh
# MAGIC # Creation
# MAGIC databricks secrets put --scope databricksScope --key dbkey-sanydatalake
# MAGIC ```
# MAGIC 
# MAGIC ```sh
# MAGIC # listing
# MAGIC databricks secrets list --scope databricksScope
# MAGIC # Key name              Last updated
# MAGIC # ------------------  --------------
# MAGIC # dbkey-sanydatalake   1672091011510
# MAGIC ```

# COMMAND ----------

# the key is not shown for security purposes!
dbutils.secrets.get('databricksScope','dbkey-sanydatalake')

# COMMAND ----------

# MAGIC %md
# MAGIC ### 4. Mounting a storage container through 

# COMMAND ----------

dbutils.fs.mount(
    source='wasbs://dbdata@samydatalake.blob.core.windows.net',
    mount_point='/mnt/dbdata',
    extra_configs={'fs.azure.account.key.samydatalake.blob.core.windows.net':dbutils.secrets.get('databricksScope','dbkey-sanydatalake')}
)

# COMMAND ----------

dbutils.fs.ls('dbfs:/mnt/dbdata')
