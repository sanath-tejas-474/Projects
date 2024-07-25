import pandas as pd
from sqlalchemy import create_engine, Table, MetaData, insert

# Define the connection parameters
db_params = {
    'user': 'postgres',
    'password': 'sanath888',
    'host': 'localhost',
    'port': '5432',
    'database': 'sales_data_db_analytics'
}

# Create a PostgreSQL engine
engine = create_engine(f'postgresql://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:{db_params["port"]}/{db_params["database"]}')

# Define the transformation function
def transform_data(data):
    # Drop unnecessary columns if they exist
    data = data.drop(columns=['Unnamed: 0', 'Month', 'Hour'], errors='ignore')

    # Convert the 'Order_Date' column to datetime format
    data['Order Date'] = pd.to_datetime(data['Order Date'])

    # Extract the date part only
    data['Order Date'] = data['Order Date'].dt.date

    # Rename columns for consistency
    data = data.rename(columns={
        'Price Each': 'Prices Each in $',
        'Sales': 'Sales Amount in $'
    })

    # Drop columns that are not needed
    data = data.drop(columns='Purchase Address', errors='ignore')

    return data

# Define the ETL function
def etl_process(csv_file_path, table_name, schema_name):
    # Extract
    data = pd.read_csv(csv_file_path)
    
    # Transform
    transformed_data = transform_data(data)
    
    # Load to PostgreSQL using SQLAlchemy 2.x
    with engine.connect() as conn:
        # Define metadata and reflect the table
        metadata = MetaData()
        table = Table(table_name, metadata, autoload_with=engine, schema=schema_name)

        # Convert DataFrame to dicts
        records = transformed_data.to_dict(orient='records')
        
        # Insert data
        conn.execute(insert(table), records)
        print(f"Data loaded into PostgreSQL table: {schema_name}.{table_name}")

    # Optionally, save a local copy
    transformed_data.to_csv('transformed_sales_data.csv', index=False)
    print("Local copy of the transformed data saved.")

# Example usage
csv_file_path = r'C:\Users\yuria\Desktop\projects\Projects\Sales_data_analysis\Sales Data.csv'  # Update with your actual file path
table_name = 'data_for_analytics'
schema_name = 'data_for_analytics'
etl_process(csv_file_path, table_name, schema_name)
