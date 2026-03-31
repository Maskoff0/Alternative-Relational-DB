import json

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

if __name__ == "__main__":
    db = Database()
    create_tables(None, db, "users", ["name", "age", "email"])

    sample_rows = [
        {"name": "Alice", "age": 28, "email": "alice@example.com"},
        {"name": "Bob", "age": 35, "email": "bob@example.com"},
        {"name": "Carol", "age": 42, "email": "carol@example.com"}
    ]

    for row in sample_rows:
        insert(db.tables["users"], row)

    print("\nDB CLI Demo")
    print("1. List all users")
    print("2. List users age > 30")
    print("3. Run sample SELECT query")
    print("4. Save DB to db.json")
    print("5. Load DB from db.json and show users")
    choice = input("Choose option (1-5): ").strip()

    if choice == "1":
        print(select(db.tables["users"]))
    elif choice == "2":
        print(select_where(db.tables["users"], "age", ">", 30))
    elif choice == "3":
        result = execute_query(db, {"type": "SELECT", "columns": ["name", "email"], "table": "users", "where": ("age", ">", 30)})
        print(result)
    elif choice == "4":
        save_db(db)
        print("Saved to db.json")
    elif choice == "5":
        loaded_db = load_db()
        print(loaded_db.tables.get("users").rows if "users" in loaded_db.tables else [])
    else:
        print("Invalid option")
