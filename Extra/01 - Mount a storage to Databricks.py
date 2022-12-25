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

# MAGIC %md ### 4. Mounting a storage container through an account key

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

# COMMAND ----------

# MAGIC %md
# MAGIC ### 5. Creating another container
# MAGIC 
# MAGIC ```sh
# MAGIC az storage container create \
# MAGIC   --name sasdata \
# MAGIC   --account-name samydatalake
# MAGIC ```
# MAGIC 
# MAGIC and then, create a SAS token throught Azure Portal.
# MAGIC 
# MAGIC The SAS token is `sp=racwdli&st=2022-12-25T13:57:59Z&se=2022-12-25T21:57:59Z&spr=https&sv=2021-06-08&sr=c&sig=6%2FpFlbUWx0vUDS2xqhkiG12xzqAk6aBxdqlOYqPrNwY%3D`

# COMMAND ----------

# MAGIC %md 
# MAGIC ### 6. Mounting storage container throught a SAS token

# COMMAND ----------

dbutils.fs.mount(
    source='wasbs://sasdata@samydatalake.blob.core.windows.net',
    mount_point='/mnt/sasdata',
    extra_configs={'fs.azure.sas.sasdata.samydatalake.blob.core.windows.net':'sp=racwdli&st=2022-12-25T13:57:59Z&se=2022-12-25T21:57:59Z&spr=https&sv=2021-06-08&sr=c&sig=6%2FpFlbUWx0vUDS2xqhkiG12xzqAk6aBxdqlOYqPrNwY%3D'}
)

# COMMAND ----------

display(dbutils.fs.ls('/mnt/sasdata'))

# COMMAND ----------

# MAGIC %md ### 7. Listing the mounts to databricks

# COMMAND ----------

display(dbutils.fs.mounts())

# COMMAND ----------


