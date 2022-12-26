# Databricks notebook source
# MAGIC %md 
# MAGIC ### 1. Install databricks CLI
# MAGIC 
# MAGIC ```sh
# MAGIC pip install databricks-cli
# MAGIC # Collecting databricks-cli
# MAGIC #   Downloading databricks-cli-0.17.4.tar.gz (82 kB)
# MAGIC #      |████████████████████████████████| 82 kB 432 kB/s 
# MAGIC # Requirement already satisfied: click>=7.0 in /usr/lib/python3/dist-packages (from databricks-cli) (7.0)
# MAGIC # Requirement already satisfied: oauthlib>=3.1.0 in /usr/lib/python3/dist-packages (from databricks-cli) (3.1.0)
# MAGIC # Requirement already satisfied: pyjwt>=1.7.0 in /usr/lib/python3/dist-packages (from databricks-cli) (1.7.1)
# MAGIC # Requirement already satisfied: requests>=2.17.3 in /usr/lib/python3/dist-packages (from databricks-cli) (2.22.0)
# MAGIC # Requirement already satisfied: six>=1.10.0 in /usr/lib/python3/dist-packages (from databricks-cli) (1.14.0)
# MAGIC # Collecting tabulate>=0.7.7
# MAGIC #   Downloading tabulate-0.9.0-py3-none-any.whl (35 kB)
# MAGIC # Building wheels for collected packages: databricks-cli
# MAGIC #   Building wheel for databricks-cli (setup.py) ... done
# MAGIC #   Created wheel for databricks-cli: filename=databricks_cli-0.17.4-py3-none-any.whl size=142892 sha256=43776bf95efab90a077d1609df3defadde0a4304bf1dc5265ee73f7d946cd8e5
# MAGIC #   Stored in directory: /home/amine/.cache/pip/wheels/48/7c/6e/4bf2c1748c7ecf994ca951591de81674ed6bf633e1e337d873
# MAGIC # Successfully built databricks-cli
# MAGIC # Installing collected packages: tabulate, databricks-cli
# MAGIC #   WARNING: The script tabulate is installed in '/home/amine/.local/bin' which is not on PATH.
# MAGIC #   Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
# MAGIC #   WARNING: The scripts databricks and dbfs are installed in '/home/amine/.local/bin' which is not on PATH.
# MAGIC #   Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
# MAGIC # Successfully installed databricks-cli-0.17.4 tabulate-0.9.0
# MAGIC 
# MAGIC ```
# MAGIC 
# MAGIC In order to run `databricks` command lines, the bin folder of folder needs to put in `$PATH` as follows:
# MAGIC 
# MAGIC ```sh
# MAGIC export PATH=$PATH:$HOME/.local/bin
# MAGIC source ~/.bashrc
# MAGIC ```

# COMMAND ----------

# MAGIC %md
# MAGIC ### 2. Configure the databricks CLI
# MAGIC 
# MAGIC ```sh
# MAGIC databricks configure --token
# MAGIC ```
# MAGIC 
# MAGIC The config is in the `/home/amine/.databrickscfg`
# MAGIC 
# MAGIC Please be noticed that even if all the clusters are down in the databricks workspace, the DBFS is always accessible.
# MAGIC 
# MAGIC ```sh
# MAGIC databricks fs ls dbfs:/mnt/aminedata
# MAGIC # data.csv 
# MAGIC ```

# COMMAND ----------


