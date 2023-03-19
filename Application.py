import random

class Product:
    def __init__(self, code, name, sale_price, manufacture_cost, stock_level, monthly_production):
        self.code = code
        self.name = name
        self.sale_price = sale_price
        self.manufacture_cost = manufacture_cost
        self.stock_level = stock_level
        self.monthly_production = monthly_production
        self.total_sold = 0
        self.total_manufactured = 0
    
    @classmethod
    def from_input(cls):
        while True:
            try:
                code = int(input("Enter product code (100-1000): "))
                if code < 100 or code > 1000:
                    raise ValueError
                break
            except ValueError:
                print("Invalid code. Please enter an integer between 100 and 1000.")
        
        name = input("Enter product name: ")
        
        while True:
            try:
                sale_price = float(input("Enter sale price: "))
                if sale_price <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid sale price. Please enter a positive number.")
        
        while True:
            try:
                manufacture_cost = float(input("Enter manufacture cost: "))
                if manufacture_cost <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid manufacture cost. Please enter a positive number.")
        
        while True:
            try:
                stock_level = int(input("Enter stock level: "))
                if stock_level <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid stock level. Please enter a positive integer.")
        
        while True:
            try:
                monthly_production = int(input("Enter monthly production: "))
                if monthly_production < 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid monthly production. Please enter a non-negative integer.")
        
        return cls(code, name, sale_price, manufacture_cost, stock_level, monthly_production)
    
    def simulate_month(self):
        units_sold = random.randint(self.monthly_production - 10, self.monthly_production + 10)
        if units_sold > self.stock_level:
            units_sold = self.stock_level
        revenue = units_sold * self.sale_price
        cost = units_sold * self.manufacture_cost
        profit = revenue - cost
        self.stock_level -= units_sold
        self.total_sold += units_sold
        self.total_manufactured += self.monthly_production
        return revenue, cost, profit, units_sold
    
    def display_info(self):
        print("Product Code:", self.code)
        print("Product Name:", self.name)
        print("Sale Price:", self.sale_price)
        print("Manufacture Cost:", self.manufacture_cost)
        print("Stock Level:", self.stock_level)
        print("Monthly Production:", self.monthly_production)
        print("Total Sold:", self.total_sold)
        print("Total Manufactured:", self.total_manufactured)
