import os

project_root = "exchange_rate_pipeline"

folders = [
    "etl",
    "db",
    "utils",
    "notebooks"
]

files = [
    ".env",
    "README.md",
    "requirements.txt",
    "prefect_flow.py",
    "etl/__init__.py",
    "etl/extract.py",
    "etl/transform.py",
    "etl/load.py",
    "db/schema.sql",
    "db/db_config.py",
    "utils/logger.py",
    "notebooks/powerbi_dashboard_demo.ipynb"
]

# Create folders
for folder in folders:
    path = os.path.join(project_root, folder)
    os.makedirs(path, exist_ok=True)

# Create files
for file in files:
    file_path = os.path.join(project_root, file)
    with open(file_path, 'w') as f:
        pass  # Creates an empty file

print("✅ Project structure created successfully!")
