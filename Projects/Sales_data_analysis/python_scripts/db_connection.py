from sqlalchemy import create_engine

# PostgreSQL connection parameters
db_params = {
    'user': 'postgres',  # Your PostgreSQL username
    'password': 'sanath888',  # Your PostgreSQL password
    'host': 'localhost',  # PostgreSQL server address
    'port': '5432',  # Default PostgreSQL port
    'database': 'sales_data_db_analytics'  # Your database name
}

# Create a PostgreSQL engine
engine = create_engine(f'postgresql://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:{db_params["port"]}/{db_params["database"]}')
