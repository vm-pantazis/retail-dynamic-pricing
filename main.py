# Implements Dynamic Pricing and Inventory Management for a Mock Retail Store

# 1. Mock Database Layout (Simulating our SQL table format using Python dictionaries)
inventory = [
    {
        "id": 101,
        "name": "Classic Winter Jacket",
        "category": "Apparel",
        "cost_price": 40.0,       # Wholesale price paid to supplier
        "original_price": 100.0,  # Base retail price
        "current_price": 100.0,   # Adjusted price by algorithm
        "stock": 2,               # High demand / Low stock scenario
        "days_in_store": 10       # Recently arrived
    },
    {
        "id": 102,
        "name": "Graphic Cotton T-Shirt",
        "category": "Apparel",
        "cost_price": 8.0,
        "original_price": 25.0,
        "current_price": 25.0,
        "stock": 45,              # Overstock / Low demand scenario
        "days_in_store": 45       # Staying in store too long (Deadstock risk)
    },
    {
        "id": 103,
        "name": "Leather Running Shoes",
        "category": "Footwear",
        "cost_price": 30.0,
        "original_price": 80.0,
        "current_price": 80.0,
        "stock": 12,              # Healthy operational scenario
        "days_in_store": 15
    }
]

# 2. RETAIL LOGIC: Dynamic Pricing and Supply Chain Automation
def optimize_prices_and_inventory(products):
    print("\n--- RUNNING RETAIL OPTIMIZATION ENGINE ---")
    
    for item in products:
        old_price = item["current_price"]
        
        # Rule A: High Demand / Low Stock Scenario -> Surge Pricing (+10%)
        if item["stock"] <= 3:
            item["current_price"] = round(item["original_price"] * 1.10, 2)
            print(f"[SURGE PRICING] '{item['name']}' stock is low ({item['stock']}). Price increased from €{old_price} to €{item['current_price']}.")
            print(f"   ⚠️ SUPPLY CHAIN ALERT: Triggering automated reorder for '{item['name']}' to prevent stockout.")
            
        # Rule B: Overstock / Deadstock Risk -> Discount Pricing (-20%)
        elif item["days_in_store"] > 30 and item["stock"] > 20:
            item["current_price"] = round(item["original_price"] * 0.80, 2)
            print(f"[MARKDOWN DISCOUNT] '{item['name']}' is moving slow ({item['days_in_store']} days in store). Price reduced from €{old_price} to €{item['current_price']} to boost volume.")
            
        # Rule C: Normal Status
        else:
            item["current_price"] = item["original_price"]
            print(f"[NORMAL] '{item['name']}' metrics are stable. Price remains at €{item['current_price']}.")

# 3. BUSINESS LOGIC: Financial Analytics & Profit Margin Calculations
def calculate_business_metrics(products):
    print("\n--- FINANCIAL PERFORMANCE DASHBOARD ---")
    
    total_potential_revenue = 0
    total_cost = 0
    
    for item in products:
        # Calculate total metrics based on current stock levels
        item_revenue = item["current_price"] * item["stock"]
        item_cost = item["cost_price"] * item["stock"]
        item_profit = item_revenue - item_cost
        
        # Avoid division by zero if pricing is faulty
        item_margin = (item_profit / item_revenue) * 100 if item_revenue > 0 else 0
        
        total_potential_revenue += item_revenue
        total_cost += item_cost
        
        print(f"Product: {item['name']}")
        print(f"  • Current Pricing Strategy Revenue: €{item_revenue:.2f}")
        print(f"  • Projected Profit Margin: {item_margin:.1f}%")
    
    # Global Store Analytics
    total_projected_profit = total_potential_revenue - total_cost
    global_margin = (total_projected_profit / total_potential_revenue) * 100 if total_potential_revenue > 0 else 0
    
    print("\n--- GLOBAL STORE FINANCIALS ---")
    print(f"Total Projected Portfolio Revenue: €{total_potential_revenue:.2f}")
    print(f"Total Projected Portfolio Profit : €{total_projected_profit:.2f}")
    print(f"Aggregate Store Profit Margin    : {global_margin:.1f}%")

# 4. Execution Flow
if __name__ == "__main__":
    # Step 1: Run the Retail Pricing engine to adjust prices based on supply/demand
    optimize_prices_and_inventory(inventory)
    
    # Step 2: Run the Business engine to see how changes impact profitability
    calculate_business_metrics(inventory)
