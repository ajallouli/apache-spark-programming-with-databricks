# Databricks notebook source
# MAGIC %md 
# MAGIC ### 1. Create an Azure Key Vault
# MAGIC 
# MAGIC ```sh
# MAGIC az keyvault create --name "akv-databricks-amine" --resource-group "rg-databricks-workspace" --location "EastUS"
# MAGIC ```

# COMMAND ----------

# MAGIC %md
# MAGIC ### 2. Create a Secret Scope
# MAGIC 
# MAGIC * Open the link: https://adb-744973935127893.13.azuredatabricks.net/?o=744973935127893#secrets/createScope . Be noticed that getting the url is as follows: https://azuredatabrics-url#secrets/createScope
# MAGIC * Specify the `Scope Name` (in this example, the scope name is amineScope)
# MAGIC * Specify the `Manager Principal` (in this example, the manager principal is All Users. The other option for manager principal `Creator` will tried later)
# MAGIC * Specify the `DNS name` (in this example, the DNS Name is https://akv-databricks-amine.vault.azure.net/)
# MAGIC * Specify the `Source ID` (in this example, the source ID is `/subscriptions/798b9fd2-5b3f-4302-88c3-c4eb676053bc/resourceGroups/rg-databricks-workspace/providers/Microsoft.KeyVault/vaults/akv-databricks-amine`)
# MAGIC 
# MAGIC Once created, the message below is returned
# MAGIC 
# MAGIC `The secret scope named amineScope has been added.
# MAGIC Manage secrets in this scope in Azure KeyVault with manage principal = users`

# COMMAND ----------

# MAGIC %md
# MAGIC ### 3. Listing the secret scopes
# MAGIC 
# MAGIC ```sh
# MAGIC databricks secrets list-scopes
# MAGIC # Scope       Backend         KeyVault URL
# MAGIC # ----------  --------------  ---------------------------------------------
# MAGIC # amineScope  AZURE_KEYVAULT  https://akv-databricks-amine.vault.azure.net/
# MAGIC ```
# MAGIC 
# MAGIC The secret scope is created successfully!

# COMMAND ----------

# MAGIC %md
# MAGIC ### 4. Create a secret in Azure Key Vault
# MAGIC 
# MAGIC Create a secret in Azure Key Vault as follows:
# MAGIC * Create a secret
# MAGIC * set the Secret Name to `key-samydatalake`
# MAGIC * set Secret Value to the key that can be collected from the Storage Account `samydatalake`. This key could be collected through Az CLI as follows:
# MAGIC ```sh
# MAGIC az storage account keys list \
# MAGIC   --account-name samydatalake
# MAGIC ```
# MAGIC * Create a storage container that will be mounter through Azure Key Vault backed Secret Scope.
# MAGIC 
# MAGIC ```sh
# MAGIC az storage container create \
# MAGIC   --name akvdata \
# MAGIC   --account-name samydatalake
# MAGIC ```

# COMMAND ----------

dbutils.fs.mount(
    source='wasbs://akvdata@samydatalake.blob.core.windows.net',
    mount_point='/mnt/akvdata',
    extra_configs={'fs.azure.account.key.samydatalake.blob.core.windows.net':dbutils.secrets.get('amineScope','key-samydatalake')}
)

# COMMAND ----------

display(dbutils.fs.ls('dbfs:/mnt/akvdata'))

# COMMAND ----------

# MAGIC %md
# MAGIC ### 5. Extra

# COMMAND ----------

dbutils.secrets.help()

# COMMAND ----------

# the key is not shown for security purposes!
dbutils.secrets.get('amineScope','key-samydatalake')

# COMMAND ----------


