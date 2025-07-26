import mysql.connector

def connect_to_db():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="mgs_user",  # custom user
            password="pa55word",  # custom user
            database="my_guitar_shop"
        )
        print("Successfully connected to MySQL database!")

    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")

    return mydb

class cli: 

    def start(self):
        running = True
        while running:
            self.interface()

    def interface(self):
        print("\nQueries:")
        print("1. Simple Single Table Queries")
        print("2. Inner Joins")
        print("3. Functions & Group By")
        print("0. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        match choice:
            case '1':
                # Simple Single Table Queries
                print("\nSimple Single Table Queries:")
                print("1. View all addresses")
                print("2. View all administrators")
                print("3. View all categories")
                print("4. View all customers")
                print("5. View all order items")
                print("6. View all orders")
                print("7. View all products")
                print("0. Back to main menu")
                
                query_choice = input("\nEnter your choice (0-7): ")
                
                match query_choice:
                    case '1':
                        self.execute_query("SELECT * FROM addresses")
                    case '2':
                        self.execute_query("SELECT * FROM administrators")
                    case '3':
                        self.execute_query("SELECT * FROM categories")
                    case '4':
                        self.execute_query("SELECT * FROM customers")
                    case '5':
                        self.execute_query("SELECT * FROM order_items")
                    case '6':
                        self.execute_query("SELECT * FROM orders")
                    case '7':
                        self.execute_query("SELECT * FROM products")
                    case '0':
                        pass
                    case _:
                        print("Invalid choice, please try again.")
                
            case '2':
                # Inner Joins
                print("\nInner Joins:")
                print("1. Orders with their items")
                print("2. Order items with product names")
                print("3. Customers with their addresses")
                print("4. Customers with their orders")
                print("5. Products with categories")
                print("0. Back to main menu")
                
                query_choice = input("\nEnter your choice (0-5): ")
                
                match query_choice:
                    case '1':
                        self.execute_query("SELECT o.order_id, oi.product_id FROM orders o INNER JOIN order_items oi ON o.order_id = oi.order_id")
                    case '2':
                        self.execute_query("SELECT oi.order_id, p.product_name FROM order_items oi INNER JOIN products p ON oi.product_id = p.product_id")
                    case '3':
                        self.execute_query("SELECT c.email_address, c.customer_id FROM customers c INNER JOIN addresses a ON c.customer_id = a.customer_id")
                    case '4':
                        self.execute_query("SELECT c.first_name, c.last_name, o.order_date FROM customers c INNER JOIN orders o ON c.customer_id = o.customer_id")
                    case '5':
                        self.execute_query("SELECT p.product_name, cat.category_name FROM products p INNER JOIN categories cat ON p.category_id = cat.category_id")
                    case '0':
                        pass
                    case _:
                        print("Invalid choice, please try again.")
                
            case '3':
                # Functions & Group By
                print("\nFunctions & Group By:")
                print("1. Days to ship each order")
                print("2. Order count by customer")
                print("3. Product count by category")
                print("4. Item count by order")
                print("5. Customer count by state")
                print("0. Back to main menu")
                
                query_choice = input("\nEnter your choice (0-5): ")
                
                match query_choice:
                    case '1':
                        self.execute_query("SELECT order_id, order_date, ship_date, DATEDIFF(ship_date, order_date) AS days_to_ship FROM orders WHERE ship_date IS NOT NULL")
                    case '2':
                        self.execute_query("SELECT customer_id, COUNT(*) AS total_orders FROM orders GROUP BY customer_id")
                    case '3':
                        self.execute_query("SELECT category_id, COUNT(*) AS product_count FROM products GROUP BY category_id")
                    case '4':
                        self.execute_query("SELECT order_id, COUNT(*) AS item_count FROM order_items GROUP BY order_id")
                    case '5':
                        self.execute_query("SELECT state, COUNT(*) AS customer_count FROM addresses GROUP BY state")
                    case '0':
                        pass
                    case _:
                        print("Invalid choice, please try again.")

    def execute_query(self, query):
        try:
            mydb = connect_to_db()
            cursor = mydb.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            
            print(f"\nExecuting: {query}")
            print("-" * 50)
            
            
            for row in results:
                print(row)
                
            print(f"\nTotal rows: {len(results)}")
            input("\nPress Enter to continue...")
            
        except mysql.connector.Error as err:
            print(f"Error executing query: {err}")
            input("\nPress Enter to continue...")
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'mydb' in locals():
                mydb.close()


if __name__ == "__main__":  
    cli_instance = cli()
    cli_instance.start()