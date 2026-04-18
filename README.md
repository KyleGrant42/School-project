[Grant.Kyle-Readme-ITT103-SP2026.txt](https://github.com/user-attachments/files/26846140/Grant.Kyle-Readme-ITT103-SP2026.txt)
================================================================
  AUTHORS:          Grant, Kyle
  DATE CREATED:     April 17, 2026
  COURSE:           ITT103 - Programming Techniques
  GITHUB URL:       https://github.com/KyleGrant42/School-project/tree/main
================================================================


================================================================
  PURPOSE OF THE PROGRAM
================================================================

This program is a menu-driven Point of Sale (POS) system built
in Python for a fictional store called "QuickMart". It is
designed to simulate the daily operations of a retail cashier,
including product management, shopping cart operations,
checkout, payment processing, and receipt generation.

The program was developed as the Major Project for the course
ITT103 - Programming Techniques (SP2026) at the University of
the Caribbean.


================================================================
  HOW TO RUN THE PROGRAM
================================================================

REQUIREMENTS:
  - Python 3.6 or higher must be installed on your computer.
  - No third-party libraries are required. The program uses
    only Python's built-in "datetime" module.

STEPS TO RUN:

  1. Download the file:
        Grant.Kyle-POS-ITT103-SP2026.py

  2. Open a terminal or command prompt and navigate to the
     folder where the file is saved. For example:
        cd Downloads

  3. Run the program with the following command:

     On Mac / Linux:
        python3 Grant.Kyle-POS-ITT103-SP2026.py

     On Windows:
        python Grant.Kyle-POS-ITT103-SP2026.py

  4. The main menu will appear. Use the number keys (1-7)
     to navigate through the options.


================================================================
  PROGRAM FEATURES & MODIFICATIONS
================================================================

  FEATURE 1 - PRODUCT CATALOG
  ----------------------------
  Purpose:
    A predefined dictionary of 12 products is included at the
    top of the program. Each product stores its name, unit
    price (in JMD), and available stock quantity.

  Products included:
    Apple, Banana, Bread, Butter, Chicken, Eggs (dozen),
    Milk (1L), Rice (1kg), Sugar (1kg), Cooking Oil,
    Cheese, Orange Juice.

  Modification:
    Stock quantities are updated in real time as items are
    added to or removed from the cart. This ensures the
    catalog always reflects accurate stock levels throughout
    the session.

  -----------------------------------------------------------

  FEATURE 2 - SHOPPING CART OPERATIONS
  -------------------------------------
  Purpose:
    Allows the cashier to build a customer's order by adding
    and removing products. The cart stores each product's
    name, quantity, and unit price.

  Add to Cart:
    - The cashier enters a product name and quantity.
    - The system validates that the product exists in the
      catalog and that sufficient stock is available before
      adding it.
    - Stock is deducted from the catalog immediately.

  Remove from Cart:
    - The cashier selects a product already in the cart.
    - The item is removed and its quantity is restored to
      the catalog stock.

  View Cart:
    - Displays all items with quantity, unit price, line
      total, and a running subtotal.

  -----------------------------------------------------------

  FEATURE 3 - CHECKOUT & PAYMENT PROCESSING
  ------------------------------------------
  Purpose:
    Calculates the final bill and processes customer payment.

  Calculation steps:
    1. Subtotal  = sum of (quantity x unit price) for all
                   items in the cart.
    2. Discount  = 5% off the subtotal if subtotal > $5,000.
    3. Tax       = 10% applied to the discounted subtotal.
    4. Total Due = (Subtotal - Discount) + Tax.

  Payment:
    - The cashier enters the amount received from the customer.
    - The system validates that the payment is not less than
      the total due.
    - Change is calculated and displayed.

  -----------------------------------------------------------

  FEATURE 4 - RECEIPT GENERATION
  --------------------------------
  Purpose:
    Produces a clearly formatted receipt at the end of each
    transaction.

  Receipt includes:
    - Store name, location, and telephone number.
    - Date and time of the transaction.
    - Itemised list: product name, quantity, unit price,
      and line total.
    - Subtotal, discount (if applied), sales tax, and
      total amount due.
    - Amount paid by customer and change returned.
    - A "Thank You" message at the bottom.

  -----------------------------------------------------------

  FEATURE 5 - DISCOUNT SYSTEM
  ----------------------------
  Purpose:
    Rewards customers with large purchases.

  Rule:
    If the subtotal of the cart exceeds JMD $5,000, a 5%
    discount is automatically applied before tax is
    calculated.

  -----------------------------------------------------------

  FEATURE 6 - LOW STOCK ALERTS
  -----------------------------
  Purpose:
    Notifies the cashier when a product is running low so
    that restocking can be arranged.

  Rule:
    After any item is added to the cart, the system checks
    the catalog. If any product has fewer than 5 units
    remaining, an alert is displayed listing those products
    and their remaining quantities.

  -----------------------------------------------------------

  FEATURE 7 - MULTIPLE TRANSACTIONS
  -----------------------------------
  Purpose:
    Allows the cashier to process more than one customer
    transaction in the same session without restarting the
    program.

  How it works:
    - After a successful checkout, the cart is automatically
      cleared and a new transaction begins.
    - The cashier can also manually start a new transaction
      via Menu Option 6 at any time. If there are items in
      the cart, the system will ask for confirmation and
      restore stock before clearing.

  -----------------------------------------------------------

  FEATURE 8 - INPUT VALIDATION
  -----------------------------
  Purpose:
    Prevents the program from crashing due to incorrect input.

  Validations applied:
    - Quantity entries must be whole numbers of 1 or more.
    - Payment amounts must be numeric and non-negative.
    - Product names are checked against the catalog before
      any operation is performed.
    - Menu choices that are not between 1 and 7 are rejected
      with an error message.
    - Payment less than the total due is rejected and the
      cashier is prompted to re-enter.


================================================================
  ASSUMPTIONS
================================================================

  1. All prices are in Jamaican Dollars (JMD).
  2. Product names are case-insensitive on entry (the program
     converts input to Title Case automatically).
  3. The product catalog is preloaded at program start and
     resets only when the program is restarted.
  4. Stock quantities are shared across transactions within
     the same session (i.e. stock deducted in Transaction 1
     is not restored for Transaction 2).
  5. Only one cashier uses the system at a time (no multi-
     user or network support).


================================================================
  LIMITATIONS
================================================================

  1. The product catalog is hardcoded. There is no option to
     add, edit, or delete products while the program is
     running.
  2. There is no data persistence. All stock changes and
     transaction history are lost when the program closes.
  3. The system does not support barcode scanning or
     integration with external databases.
  4. Only one discount rule is implemented (5% for bills
     over $5,000). No coupon or loyalty card system is
     included.
  5. Receipts are printed to the terminal only and cannot
     be saved to a file or sent by email.


================================================================
  FILE NAMING
================================================================

  Program file : Grant.Kyle-POS-ITT103-SP2026.py
  Report file  : Grant.Kyle-Readme-ITT103-SP2026.txt
  Zip folder   : Grant.Kyle-Major_Project-ITT103-SP2026.zip

================================================================
