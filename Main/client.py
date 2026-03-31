from main import Database, create_tables, insert, select, select_where, execute_query, save_db, load_db , execute_create


def main():
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
    print("3. Run create table function")
    print("4. Run sample SELECT query")
    print("5. Save DB to db.json")
    print("6. Load DB from db.json and show users")

    choice = input("Choose option (1-5): ").strip()

    if choice == "1":
        print(select(db.tables["users"]))
    elif choice == "2":
        print(select_where(db.tables["users"], "age", ">", 30))
    elif choice == "3":
        ddl = input("Enter CREATE TABLE statement (e.g. CREATE TABLE subscribers (id INT, username TEXT, email TEXT)): ").strip()
        try:
            execute_create(db, ddl)
            print("Created table from SQL:", ddl)
        except Exception as e:
            print("Failed to create table:", e)
    elif choice == "4":
        result = execute_query(db, {"type": "SELECT", "columns": ["name", "email"], "table": "users", "where": ("age", ">", 30)})
        print(result)
    elif choice == "5":
        save_db(db)
        print("Saved to db.json")
    elif choice == "6":
        loaded_db = load_db()
        print(loaded_db.tables.get("users").rows if "users" in loaded_db.tables else [])
    else:
        print("Invalid option")


if __name__ == "__main__":
    main()
