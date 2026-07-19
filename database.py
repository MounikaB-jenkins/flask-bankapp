secret = get_database_secret()

connection = psycopg2.connect(

host=secret["host"],

database=secret["database"],

user=secret["username"],

password=secret["password"],

port=secret["port"]

)
