# Databricks notebook source
# MAGIC %md
# MAGIC 
# MAGIC ### 1. creating a storage account
# MAGIC 
# MAGIC ```sh
# MAGIC az storage account create \
# MAGIC   --name samydatalake \
# MAGIC   --resource-group rg-databricks-workspace  \
# MAGIC   --location eastus \
# MAGIC   --sku Standard_LRS
# MAGIC ```
# MAGIC 
# MAGIC ### 2. showing the keys of the storage account
# MAGIC ```sh
# MAGIC az storage account keys list --account-name samydatalake
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
# MAGIC 
# MAGIC ### 3. Creating a storage container
# MAGIC ```sh
# MAGIC az storage container create \
# MAGIC   --name data \
# MAGIC   --account-name samydatalake
# MAGIC ```

# COMMAND ----------

dbutils.fs.mount(
    source='wasbs://data@samydatalake.blob.core.windows.net',
    mount_point='/mnt/aminedata',
    extra_configs={'fs.azure.account.key.samydatalake.blob.core.windows.net':'0dKCtjwpYydMBF0EjGoL58N2dVkBmio2N4QVBLg/5++J+/pHmZ4dQvjW/WV+xdjLekIrNLQdioUb+AStkAuxNw=='}
)

# COMMAND ----------

display(dbutils.fs.ls('/mnt/aminedata'))

# COMMAND ----------

# MAGIC %sh
# MAGIC ls -al
