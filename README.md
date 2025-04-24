# 💱 Currency Exchange Data Warehouse Pipeline

An end-to-end data engineering project that extracts real-time currency exchange rates using the [ExchangeRate API](https://www.exchangerate-api.com/), transforms and stores the data in a PostgreSQL data warehouse, schedules the ETL pipeline using Prefect, and visualizes the data in Power BI.

---

## 📌 Project Features

- 🔁 **ETL Pipeline**: Extracts currency exchange rates, transforms the data, and loads it into a PostgreSQL database.
- 🧠 **Deduplication**: Avoids inserting duplicate records based on timestamp, base currency, and target currency.
- 🗓️ **Scheduled Execution**: Automated with [Prefect 3.3.3](https://docs.prefect.io/).
- 📊 **Data Visualization**: Connects PostgreSQL to Power BI for interactive dashboards.
- ☁️ **Cloud-Ready**: Easily deployable to Prefect Cloud and a hosted PostgreSQL instance.

---

## 🛠️ Tech Stack

| Layer        | Tool / Technology     |
|--------------|------------------------|
| Orchestration| Prefect 3.3.3          |
| Storage      | PostgreSQL             |
| Language     | Python 3.11.8          |
| Scheduler    | Prefect CLI or Cloud   |
| API Source   | ExchangeRate API       |
| Visualization| Power BI               |
| Deployment   | Local or Cloud (EC2, RDS, etc.) |

---

## 📂 Project Structure

  2. 🐍 Create & Activate Virtual Environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate     # Windows
# OR
source venv/bin/activate  # macOS/Linux


3. 📦 Install Dependencies
pip install -r requirements.txt


5. 🔐 Setup Environment Variables
Create a .env file in the root folder:

API_KEY=your_exchangerate_api_key
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database
DB_USER=your_user
DB_PASSWORD=your_password

▶️ Run the ETL Flow
Option 1: Manual Trigger (Local)

python prefect_flow.py
Option 2: Prefect Deployment

# Build and apply deployment
prefect deployment build prefect_flow.py:currency_flow -n "exchange-flow"
prefect deployment apply exchange-flow-deployment.yaml

# Start agent to pick up scheduled runs
prefect agent start --pool default-agent-pool
