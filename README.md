# 🚀 Azure Data Engineering Project

An end-to-end Azure Data Engineering project built using **Azure Data Factory, ADLS Gen2, Azure Databricks, PySpark, Delta Lake, Unity Catalog, Databricks SQL Warehouse, and Power BI**.

## 🏗️ Project Architecture diagram

<img width="1580" height="996" alt="ChatGPT Image Sep 26, 2026, 03_36_02 PM" src="https://github.com/user-attachments/assets/d5ae4464-c11b-48a4-97c2-4b320f042510" />

## 📌 Project Overview

The project demonstrates how different Azure services work together to build a cloud-based data engineering pipeline.

The data is organized using the **Medallion Architecture**:

* 🥉 **Bronze** – Raw/ingested data
* 🥈 **Silver** – Cleaned and processed data
* 🥇 **Gold** – Business-ready data

## 🔧 Technologies Used

* Azure Data Factory
* Azure Data Lake Storage Gen2
* Azure Databricks
* PySpark
* Delta Lake
* Unity Catalog
* Databricks SQL Warehouse
* Power BI
* SQL

## 🔄 Data Ingestion

Azure Data Factory was used for **data ingestion and pipeline orchestration**.

The pipeline is designed to ingest source/API data into **ADLS Gen2**.

Key ADF concepts used:

* Copy Activity
* Lookup
* ForEach
* Parameters
* Dynamic expressions
* Triggers
* Pipeline orchestration

## 🥈 Silver Layer

Silver-layer data is processed using **Azure Databricks and PySpark**.

The Silver notebook reads data from ADLS Gen2 and prepares it for the Gold layer.

Notebook:

```text
notebooks/Silver.py
```

## 🥇 Gold Layer

The Gold layer contains business-ready data stored using **Delta Lake**.

Gold tables include:

* `trip_zone`
* `trip_type`
* `trips`

Notebook:

```text
notebooks/Gold.py
```

Gold data is stored in the **ADLS Gen2 Gold container**.

## 🧱 Delta Lake

Delta Lake was used for reliable storage of the Gold-layer data.

Concepts explored:

* ACID transactions
* Schema enforcement
* Transaction history
* Versioning
* Time Travel

Example:

```sql
DESCRIBE HISTORY gold.trips;
```

## 🔐 Unity Catalog

Unity Catalog was used for:

* Data governance
* Table management
* Access control
* External Locations
* Storage credentials

An External Location was configured to allow the Gold Delta data to be stored in ADLS Gen2.

## 📊 Data Consumption

The Gold Delta tables were accessed through **Databricks SQL Warehouse**.

Power BI was connected to Databricks SQL Warehouse for reporting and visualization.

The data was **not physically copied into the SQL Warehouse**. The Gold data remains stored in ADLS Gen2.

## 📁 Repository Structure

```text
azure-data-engineering-project/
│
├── README.md
│── Silver.py
│── Gold.py
|__ trip_zone_lookup.csv
|__ trip_type.csv
```

## 🧠 Key Skills Demonstrated

* Azure Data Engineering
* API Data Ingestion
* Azure Data Factory
* ADLS Gen2
* PySpark
* Azure Databricks
* Medallion Architecture
* Delta Lake
* Unity Catalog
* SQL
* Databricks SQL Warehouse
* Power BI Integration

## 🚀 Future Improvements

Possible improvements for the project:

* Incremental loading using watermark
* Change Data Capture (CDC)
* Data quality checks
* Better error handling and retries
* Monitoring and alerting
* Automated Power BI refresh

> **Note:** Incremental loading and CDC were not implemented in the current version and are listed as future improvements.

## 🔒 Security

No secrets, passwords, access tokens, client secrets, API keys, or other credentials should be committed to this repository.

Authentication values should be replaced with placeholders when sharing code publicly.

For production implementations, secure approaches such as **Azure Key Vault and Managed Identity** should be used.

## 👨‍💻 Author

**Om Nadarkar**

Data Engineering | Azure | Databricks | PySpark | SQL
