#🛒 Shopping Cart
import sys

class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    def  get_final_price(self):
        return self._price

    def get_product_detail(self):
        return f'Product name: {self.name}, Product Price: {self._price}, Final Price: {self.get_final_price()}'    

class Electronics(Product):
    def get_final_price(self):
        price = super().get_final_price()
        vat = (price * 15) / 100
        return price + vat

class Grocery(Product):
    def get_final_price(self):
        price = super().get_final_price()
        vat = (price * 5) / 100
        return price + vat

class Clothing(Product):
    def get_final_price(self):
        price = super().get_final_price()
        vat = (price * 10) / 100
        return price + vat

class Cart:

    def __init__(self):
        self.products = []
    
    def show_product(self):
        if not self.products:
            print('Cart is Empty!')
            return
        
        for item in self.products:
            print(item.get_product_detail())    

    def add_product(self, name, price, product_class):
        self.products.append(product_class(name, price))
        print('Product added successfully')

    def total_price(self):
        total = 0
        for item in self.products:
            item_price = item.get_final_price()
            total += item_price
        return total

if __name__ == '__main__':

    cart = Cart()

    while True:
        operation = input('1.Add Product\n2.Show Cart\n3.Total Price\n4.Exit\n=')
    
        if operation == '1':
            product_type = input('1.Electronic\n2.Grocery\n3.Clothing\n=')
            product_name = input('Enter product name:\n')
            product_price = int(input('Enter product price:\n'))

            if product_type == '1':
                cart.add_product(product_name, product_price, Electronics)
            elif product_type == '2':
                cart.add_product(product_name, product_price, Grocery)
            elif product_type == '3':
                cart.add_product(product_name, product_price, Clothing)

        elif operation == '2':
            cart.show_product()

        elif operation == '3':
            if not cart.products:
                print('Cart is empty')
            else:
                print(f'Total Cost is: {cart.total_price():.2f}')
        
        elif operation == '4':
            sys.exit()

