import sqlite3
import sys
# 1. DATABASE SETUP & INITIALIZATION
def initialize_database():
    conn = sqlite3.connect("retail_store.db")
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT,
        category TEXT,
        cost_price REAL,
        original_price REAL,
        current_price REAL,
        stock INTEGER,
        days_in_store INTEGER
    )
    """)
    
    cursor.execute("SELECT COUNT(*) FROM products")
    if cursor.fetchone()[0] == 0:
        mock_products = [
            (101, 'Classic Winter Jacket', 'Apparel', 40.0, 100.0, 100.0, 2, 10),
            (102, 'Graphic Cotton T-Shirt', 'Apparel', 8.0, 25.0, 25.0, 45, 45),
            (103, 'Leather Running Shoes', 'Footwear', 30.0, 80.0, 80.0, 12, 15)
        ]
        cursor.executemany("INSERT INTO products VALUES (?, ?, ?, ?, ?, ?, ?, ?)", mock_products)
        conn.commit()
        print("[SUCCESS] SQL Database initialized with default mock retail products.")
        
    conn.close()

# 2. RETAIL LOGIC: Dynamic Pricing Engine
def optimize_prices_and_inventory():
    print("\n==================================================")
    print("--- RUNNING RETAIL OPTIMIZATION ENGINE (SQL) ---")
    print("==================================================")
    conn = sqlite3.connect("retail_store.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, name, original_price, current_price, stock, days_in_store FROM products")
    products = cursor.fetchall()
    
    for item in products:
        p_id, name, original_price, current_price, stock, days_in_store = item
        new_price = current_price
        
        # Rule A: Low Stock -> Surge Pricing (+10%)
        if stock <= 3 and stock > 0:
            new_price = round(original_price * 1.10, 2)
            print(f"[SURGE PRICING] '{name}' stock is low ({stock}). Price optimized to €{new_price}.")
            print(f"   ⚠️ SUPPLY CHAIN ALERT: Reorder event triggered for '{name}'.")
            
        # Rule B: Overstock / Deadstock Risk -> Discount (-20%)
        elif days_in_store > 30 and stock > 20:
            new_price = round(original_price * 0.80, 2)
            print(f"[MARKDOWN DISCOUNT] '{name}' is moving slow ({days_in_store} days). Price reduced to €{new_price} to clear inventory.")
            
        # Rule C: Out of Stock
        elif stock == 0:
            print(f"[OUT OF STOCK] '{name}' is completely unavailable. Urgent procurement required.")
            
        # Rule D: Normal Status
        else:
            new_price = original_price
            print(f"[NORMAL] '{name}' metrics are stable. Price remains at €{new_price}.")
            
        cursor.execute("UPDATE products SET current_price = ? WHERE id = ?", (new_price, p_id))
    
    conn.commit()
    conn.close()
    print("[SUCCESS] Dynamic pricing updates saved to SQL.")

# 3. BUSINESS LOGIC: Financial Analytics & Profit Dashboard
def calculate_business_metrics():
    print("\n==================================================")
    print("--- FINANCIAL PERFORMANCE DASHBOARD ---")
    print("==================================================")
    conn = sqlite3.connect("retail_store.db")
    cursor = conn.cursor()
    
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
        print(f"  • Strategy Revenue : €{item_revenue:.2f} (Stock: {stock})")
        print(f"  • Profit Margin     : {item_margin:.1f}%")
        print("-" * 30)
        
    total_projected_profit = total_potential_revenue - total_cost
    global_margin = (total_projected_profit / total_potential_revenue) * 100 if total_potential_revenue > 0 else 0
    
    print("--- GLOBAL STORE FINANCIALS ---")
    print(f"Aggregate Projected Revenue: €{total_potential_revenue:.2f}")
    print(f"Aggregate Projected Profit : €{total_projected_profit:.2f}")
    print(f"Global Store Profit Margin : {global_margin:.1f}%")
    conn.close()

# 4. USER INTERACTION: Add New Retail Item to SQL
def add_new_product():
    print("\n--- ADD NEW PRODUCT TO INVENTORY ---")
    try:
        p_id = int(input("Enter unique Product ID (e.g. 104): "))
        name = input("Enter Product Name (e.g. Silk Dress): ")
        category = input("Enter Category (e.g. Apparel, Accessories): ")
        cost_price = float(input("Enter Wholesale Cost Price (€): "))
        original_price = float(input("Enter Base Retail Price (€): "))
        stock = int(input("Enter Initial Stock Level: "))
        days_in_store = int(input("Enter Days in Store: "))
        
        conn = sqlite3.connect("retail_store.db")
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO products (id, name, category, cost_price, original_price, current_price, stock, days_in_store)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (p_id, name, category, cost_price, original_price, original_price, stock, days_in_store))
        
        conn.commit()
        conn.close()
        print(f"\n[SUCCESS] '{name}' successfully injected into SQL Database.")
    except Exception as e:
        print(f"\n[ERROR] Failed to add product. Make sure ID is unique and numbers are formatted correctly. ({e})")

# 5. THE INTERACTIVE CLI MENU
def interactive_menu():
    initialize_database()
    
    while True:
        print("\n" + "="*40)
        print("    RETAIL BUSINESS INTELLIGENCE SYSTEM")
        print("="*40)
        print("1. Run Dynamic Pricing Engine (Retail Optimization)")
        print("2. View Financial Dashboard (Business Performance)")
        print("3. Add New Product to SQL Inventory")
        print("4. Exit System")
        print("="*40)
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == "1":
            optimize_prices_and_inventory()
        elif choice == "2":
            calculate_business_metrics()
        elif choice == "3":
            add_new_product()
        elif choice == "4":
            print("\nShutting down system. Goodbye!")
            sys.exit()
        else:
            print("\n[INVALID CHOICE] Please enter a number between 1 and 4.")

# Main Flow Execution
if __name__ == "__main__":
    interactive_menu()
