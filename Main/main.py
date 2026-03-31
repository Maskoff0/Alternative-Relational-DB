import json
import re

#Implementing a simple relational database system in Python
#Building a database engine
#Creating Database and Table to represent the Data Stucture
class Table:
    def __init__(self, name, columns):
        self.name = name
        self.columns = columns
        self.rows = []
    
class Database:
    def __init__(self):
        self.tables = {}
        
#implementing basic CRUD operations
def create_tables(self , db, name, columns):
    if name in db.tables:
        print(f"Table {name} already exists.")
    else:
        db.tables[name] = Table(name, columns)
        print(f"Table {name} created successfully.")
        
# Insert a row into a table
def insert(table, row):
    table.rows.append(row)
    print(f"Row inserted into table {table.name} successfully.")

# Select Rows from a table
def select(table, condition=None):
    if condition is None:
        return table.rows
    else:
        return [row for row in table.rows if condition(row)]
    
#Adding a filter [WHERE clause]
def select_where(table, column , operator, value):
 result = []
 for row in table.rows:
     if operator == ">" and row[column] > value :
       result.append(row)
 return result

#Building a simple query parser
query = "SELECT name FROM users WHERE age > 30"
tokens = query.split()

#Convert the query into an AST
query_obj = {
    "type" : "SELECT",
    "columns" : ["name"],
    "table" : "users",
    "where" : ("age", ">" , 30)
}

#Execute parsed query
def execute_query(db, query):
    table = db.tables[query["table"]]
    rows = table.rows
    
    if query["where"]:
        column, operator, value = query["where"]
        rows = [r for r in rows if r[column]> value]
    return [{col: row[col] for col in query["columns"]} for row in rows]

#Adding parser logic
def parser(self):
    token = self.current().upper()
    if token == "SELECT":
        return self.parse_select()
    elif token == "INSERT":
        return self.parse_insert()
    elif token == "CREATE":
        return self.parse_create()
    else:
        raise Exception(f"Unknown command {token}")
    
#Create a table parser
def parse_create(self):
    self.advance()
    if self.current().upper() != "TABLE":
        raise Exception("Expected Table")
    
    self.advance()
    table_name = self.current()
    self.advance()
    
    if self.current() != "(":
        raise Exception("Expected (")
    self.advance()
    
    columns = {}
    
    while self.current() != ")":
        column_name = self.current()
        self.advance()
        
        column_type = self.current()
        self.advance()
        
        columns[column_name] = column_type
        
        if self.current() == ",":
            self.advance()
            
        self.advance()
    return {
        "type" : "CREATE",
        "table_name" : table_name,
        "columns" : columns
    }
    
def parse_create_sql(sql):
    sql = sql.strip().rstrip(";")
    m = re.match(
        r"^\s*CREATE\s+TABLE\s+([A-Za-z_][A-Za-z0-9_]*)\s*\((.*)\)\s*$",
        sql,
        re.I,
    )
    if not m:
        raise ValueError("Invalid CREATE TABLE syntax. Use: CREATE TABLE name (col1 TYPE, col2 TYPE)")

    table_name = m.group(1)
    cols = m.group(2).strip()
    if not cols:
        raise ValueError("No columns found in CREATE TABLE")

    column_names = []
    for part in cols.split(","):
        part = part.strip()
        if not part:
            continue
        tokens = part.split()
        if len(tokens) < 1:
            raise ValueError(f"Invalid column definition: '{part}'")
        column_names.append(tokens[0])

    return {"table_name": table_name, "columns": column_names}

#Logic for executing table creation
# query can be dict or SQL string
def execute_create(db, query):
    if isinstance(query, str):
        query = parse_create_sql(query)

    table_name = query.get("table_name")
    columns = query.get("columns")
    if not table_name or not columns:
        raise ValueError("execute_create expects table_name and columns")

    if table_name in db.tables:
        raise ValueError(f"Table {table_name} already exists.")

    create_tables(None, db, table_name, columns)
    return db.tables[table_name]

#Adding Persistence to the Database
def save_db(db, path="db.json"):
    payload = {name: table.rows for name, table in db.tables.items()}
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)

#Trying to load data from the db
def load_db(path="db.json"):
    db = Database()
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    for name, rows in data.items():
        if rows:
            columns = list(rows[0].keys())
        else:
            columns = []
        table = Table(name, columns)
        table.rows = rows
        db.tables[name] = table
    return db


#Indexing and Optimiation (not implemented in  this simple version)
index = {
    "age" : {
        28: [0],
        35: [1],
        42: [2]
    }
}