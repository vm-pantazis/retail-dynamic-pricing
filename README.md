# Retail Inventory & Dynamic Pricing Optimization Engine
### Developed by Pantazis Vlasios Marios   | Independent Financial Analytics Project

A Python and SQL terminal application designed to help retail shops manage their stock and adjust prices automatically. This project applies programming logic to real-world business challenges, focusing on how supply and demand impact store profitability. Additionally, it features a financial dashboard to track gross profit margins and business performance, making it highly relevant to both retail management and economic analysis.

---

## 📈 Business Case & Strategic Objective
In modern retail, profitability is constantly threatened by two main operational failures:
1. **Deadstock (Overstocking):** Capital tied down in slow-moving items, leading to high storage costs and eventual losses.
2. **Stockouts (Understocking):** Missed revenue opportunities and reduced consumer loyalty due to product unavailability.

This system solves these core business issues by deploying an **Automated Dynamic Pricing Engine** that alters retail prices programmatically based on supply chain and consumer demand metrics, maximizing the **Global Store Profit Margin**.

---

## 🛠️ System Architecture & Logic

### 1. Relational Database Layer (SQL)
The system operates on an embedded SQLite database featuring a strict relational table structure (`products`). It tracks wholesale costs, retail pricing, live inventory volumes, and product aging metrics (`days_in_store`).

### 2. Retail Optimization Algorithms
* **Surge Pricing Rule (High Demand):** When an item's stock drops to ≤ 3 units, the engine implements a **10% price surge** to capture high consumer willingness-to-pay while generating an automated **Supply Chain Procurement Alert** for restocking.
* **Markdown Discount Rule (Deadstock Risk):** If a product remains unsold for over 30 days and inventory levels are high, a **20% markdown discount** is applied to clear store shelf-space and liquidate assets.

### 3. Financial Performance Dashboard
Computes active product-by-product revenue projections and gross profit margins. It aggregates store data to present global portfolio analytics, including:
* **Aggregate Projected Revenue**
* **Aggregate Projected Profit**
* **Global Store Profit Margin (%)**

---

## 💻 Tech Stack & Frameworks
* **Language:** Python 3
* **Database Engine:** SQLite3 (SQL)
* **Architecture:** Command Line Interface (CLI) / Object-Oriented Logic Flow

---

## 🚀 How to Run the System
1. Clone this repository: `git clone https://github.com`/vm-pantazis/retail-dynamic-pricing
2. Navigate to the project directory: `cd retail-dynamic-pricing`
3. Execute the core terminal application: `python main.py`
