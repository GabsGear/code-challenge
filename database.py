import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

connection = psycopg2.connect(database=os.getenv('POSTGRES_DB'), 
                              user=os.getenv('POSTGRES_USER'), 
                              password=os.getenv('POSTGRES_PASSWORD'),
                              host=os.getenv('POSTGRES_HOST'), 
                              port=os.getenv('POSTGRES_PORT'))

cursor = connection.cursor()

cursor.execute("SELECT 1+1;")

# Fetch all rows from database
record = cursor.fetchall()

print("Data from Database:- ", record)