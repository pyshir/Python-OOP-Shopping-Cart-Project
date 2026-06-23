# 🛒 Python OOP Shopping Cart Project

A simple **menu-driven Shopping Cart system** built using Python OOP concepts.  
This project demonstrates core Object-Oriented Programming principles like **Inheritance, Polymorphism, Encapsulation, and Method Overriding**.

---

## 🚀 Features

- Add products to cart
- Supports multiple product types:
  - Electronics (15% VAT)
  - Grocery (5% VAT)
  - Clothing (10% VAT)
- Show all products in cart
- Calculate total price with VAT
- Menu-driven CLI interface

---

## 🧠 OOP Concepts Used

This project is built to practice:

- ✅ Encapsulation (`_price`)
- ✅ Inheritance (`Product → Electronics, Grocery, Clothing`)
- ✅ Method Overriding (`get_final_price()`)
- ✅ Polymorphism (same method, different behavior)
- ✅ Composition (`Cart has Products`)
- ✅ `super()` usage

---

## 📂 Project Structure

```text
shopping_cart.py
🧾 Classes Overview
🟦 Product (Base Class)
Stores product name and price
Provides base method for final price
🟩 Electronics
Adds 15% VAT
🟨 Grocery
Adds 5% VAT
🟥 Clothing
Adds 10% VAT
🛒 Cart
Stores all products
Add product
Show products
Calculate total price
▶️ How to Run
1. Clone the repository
git clone https://github.com/your-username/shopping-cart.git
2. Run the program
python shopping_cart.py
🧑‍💻 Usage Example
1.Add Product
2.Show Cart
3.Total Price
4.Exit
=
Example Flow:
Enter product name:
Laptop
Enter product price:
50000
Product added successfully
💡 Example Output
Product name: Laptop, Product Price: 50000, Final Price: 57500.00
Total Cost is: 57500.00
📌 Future Improvements
Add remove product feature
Add discount system
Save cart data to file/database
Add error handling (try/except)
Improve UI using GUI or Web version
📚 Learning Purpose

This project is created for learning Python OOP concepts step-by-step through a real-world mini project.

⭐ Author

Made with 💻 by pyShir
