 [README.md](https://github.com/user-attachments/files/26846108/README.md)
# 🛒 QuickMart POS System

A menu-driven **Point of Sale (POS) system** built in Python for the course **Programming Techniques (ITT-103)** at the University of the Caribbean.

---

## 📋 Features

- **Product Catalog** — 12 preloaded products with prices and stock quantities
- **Shopping Cart** — Add and remove items with real-time stock validation
- **Checkout & Payment** — Tax calculation, change computation, and payment validation
- **Discount System** — 5% discount automatically applied on bills over JMD $5,000
- **Receipt Generation** — Formatted receipt with itemised list, totals, and thank-you message
- **Low Stock Alerts** — Warns cashier when any product falls below 5 units
- **Multiple Transactions** — Start a new transaction without restarting the program
- **Input Validation** — Handles invalid entries (letters where numbers are expected, etc.)

---

## 🚀 Getting Started

### Requirements

- Python 3.6 or higher
- No external libraries required

### Run the Program

```bash
python3 pos_system.py
```

On Windows:

```bash
python pos_system.py
```

---

## 🖥️ Menu Options

| Option | Description |
|--------|-------------|
| 1 | View Product Catalog |
| 2 | Add Item to Cart |
| 3 | Remove Item from Cart |
| 4 | View Cart |
| 5 | Checkout & Pay |
| 6 | Start New Transaction |
| 7 | Exit |

---

## 🧾 Sample Receipt

```
*******************************************************
*              QuickMart — Point of Sale              *
*                  Kingston, Jamaica                  *
*                 Tel: (876) 555-0199                 *
*******************************************************
  Date & Time : 2026-04-17  10:45:22
-------------------------------------------------------
  ITEM                QTY  UNIT PRICE       TOTAL
-------------------------------------------------------
  Apple                 3   JMD $   50.00  JMD $  150.00
  Bread                 2   JMD $  250.00  JMD $  500.00
  Chicken              10   JMD $  800.00  JMD $ 8000.00
-------------------------------------------------------
  Subtotal                            : JMD $ 8650.00
  Discount (5% bill over $5000)       : -JMD $ 432.50
  Sales Tax (10%)                     : JMD $  821.75
-------------------------------------------------------
  TOTAL DUE                           : JMD $ 9039.25
  Amount Paid                         : JMD $10000.00
  Change Returned                     : JMD $  960.75
*******************************************************
*        Thank you for shopping at QuickMart!         *
*                 Please come again.                  *
*******************************************************
```

---

## 📦 Product Catalog

| Product | Price (JMD) | Starting Stock |
|---------|-------------|----------------|
| Apple | $50.00 | 100 |
| Banana | $30.00 | 80 |
| Bread | $250.00 | 40 |
| Butter | $350.00 | 25 |
| Chicken | $800.00 | 20 |
| Eggs (dozen) | $450.00 | 15 |
| Milk (1L) | $200.00 | 50 |
| Rice (1kg) | $180.00 | 60 |
| Sugar (1kg) | $220.00 | 45 |
| Cooking Oil | $600.00 | 30 |
| Cheese | $500.00 | 10 |
| Orange Juice | $350.00 | 8 |

---

## 🏗️ Code Structure

```
pos_system.py
│
├── Constants & Product Catalog
│
├── Helper Functions
│   ├── display_separator()
│   ├── display_header()
│   ├── get_integer_input()
│   └── get_float_input()
│
├── Product Management
│   ├── display_catalog()
│   └── check_low_stock()
│
├── Shopping Cart
│   ├── create_cart()
│   ├── add_to_cart()
│   ├── remove_from_cart()
│   └── view_cart()
│
├── Checkout & Payment
│   ├── calculate_totals()
│   └── checkout()
│
├── Receipt
│   └── print_receipt()
│
└── Main Loop
    ├── display_menu()
    └── run_pos()
```

---

## 📚 Course Information

| Field | Detail |
|-------|--------|
| Course | Programming Techniques |
| Code | ITT-103 |
| Institution | University of the Caribbean |
| Language | Python 3 |

---

## 📄 License

This project was created for academic purposes.
