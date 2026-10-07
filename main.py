import sqlite3

# 1. DATABASE SETUP & INITIALIZATION (SQL Phase)
def initialize_database():
    # Connects to SQLite (creates the file if it doesn't exist)
    conn = sqlite3.connect("retail_store.db")
    cursor = conn.cursor()
    
    # Create the SQL table for our Retail Inventory
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT EXISTS,
        category TEXT,
        cost_price REAL,
        original_price REAL,
        current_price REAL,
        stock INTEGER,
        days_in_store INTEGER
    )
    """)
    
    # Check if table is empty, if so, insert mock data
    cursor.execute("SELECT COUNT(*) FROM products")
    if cursor.fetchone()[0] == 0:
        mock_products = [
            (101, 'Classic Winter Jacket', 'Apparel', 40.0, 100.0, 100.0, 2, 10),
            (102, 'Graphic Cotton T-Shirt', 'Apparel', 8.0, 25.0, 25.0, 45, 45),
            (103, 'Leather Running Shoes', 'Footwear', 30.0, 80.0, 80.0, 12, 15)
        ]
        cursor.executemany("INSERT INTO products VALUES (?, ?, ?, ?, ?, ?, ?, ?)", mock_products)
        conn.commit()
        
    conn.close()

# 2. RETAIL LOGIC: Fetch from SQL, apply Dynamic Pricing, and update Database
def optimize_prices_and_inventory():
    print("\n--- RUNNING RETAIL OPTIMIZATION ENGINE (SQL POWERED) ---")
    conn = sqlite3.connect("retail_store.db")
    cursor = conn.cursor()
    
    # SQL Query to pull all products from inventory
    cursor.execute("SELECT id, name, original_price, current_price, stock, days_in_store FROM products")
    products = cursor.fetchall()
    
    for item in products:
        p_id, name, original_price, current_price, stock, days_in_store = item
        new_price = current_price
        
        # Rule A: High Demand / Low Stock Scenario -> Surge Pricing (+10%)
        if stock <= 3:
            new_price = round(original_price * 1.10, 2)
            print(f"[SURGE PRICING] '{name}' stock is low ({stock}). Price increased to €{new_price}.")
            print(f"   ⚠️ SUPPLY CHAIN ALERT: Automatically triggered reorder event for '{name}'.")
            
        # Rule B: Overstock / Deadstock Risk -> Discount Pricing (-20%)
        elif days_in_store > 30 and stock > 20:
            new_price = round(original_price * 0.80, 2)
            print(f"[MARKDOWN DISCOUNT] '{name}' is moving slow ({days_in_store} days in store). Price reduced to €{new_price} to clear inventory.")
            
        # Rule C: Normal Status
        else:
            new_price = original_price
            print(f"[NORMAL] '{name}' metrics are stable. Price remains at €{new_price}.")
            
        # SQL Update Query to save the optimized price back to the database
        cursor.execute("UPDATE products SET current_price = ? WHERE id = ?", (new_price, p_id))
    
    conn.commit()
    conn.close()

# 3. BUSINESS LOGIC: Financial Analytics & Profit Margin Calculations
def calculate_business_metrics():
    print("\n--- FINANCIAL PERFORMANCE DASHBOARD ---")
    conn = sqlite3.connect("retail_store.db")
    cursor = conn.cursor()
    
    # Advanced SQL query calculating profit and margins directly if needed, 
    # but we will fetch and calculate in Python to show dual-proficiency
    cursor.execute("SELECT name, current_price, cost_price, stock FROM products")
    products = cursor.fetchall()
    
    total_potential_revenue = 0
    total_cost = 0
    
    for item in products:
        name, current_price, cost_price, stock = item
        
        item_revenue = current_price * stock
        item_cost = cost_price * stock
        item_profit = item_revenue - item_cost
        item_margin = (item_profit / item_revenue) * 100 if item_revenue > 0 else 0
        
        total_potential_revenue += item_revenue
        total_cost += item_cost
        
        print(f"Product: {name}")
        print(f"  • Active Strategy Revenue: €{item_revenue:.2f}")
        print(f"  • Projected Profit Margin: {item_margin:.1f}%")
        
    total_projected_profit = total_potential_revenue - total_cost
    global_margin = (total_projected_profit / total_potential_revenue) * 100 if total_potential_revenue > 0 else 0
    
    print("\n--- GLOBAL STORE FINANCIALS ---")
    print(f"Total Projected Portfolio Revenue: €{total_potential_revenue:.2f}")
    print(f"Total Projected Portfolio Profit : €{total_projected_profit:.2f}")
    print(f"Aggregate Store Profit Margin    : {global_margin:.1f}%")
    
    conn.close()

# 4. Main Execution Flow
if __name__ == "__main__":
    initialize_database()          # Setup the SQL table and load data
    optimize_prices_and_inventory() # Extract, run business intelligence, and update SQL
    calculate_business_metrics()    # Generate financial report
