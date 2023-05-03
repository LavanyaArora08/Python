class Product:
    def __init__(self, product_id, price_per_unit, stock_qty):
        self.product_id = product_id
        self.price_per_unit = price_per_unit
        self.stock_qty = stock_qty
        
    def is_available(self, qty):
        return self.stock_qty >= qty
    
    def reduce_stock(self, qty):
        self.stock_qty -= qty
        
class Purchase(Product):
    def __init__(self, product_id, price_per_unit, stock_qty):
        super().__init__(product_id, price_per_unit, stock_qty)
        
    def generate_bill(self, pid, qty_purchased, discount=0):
        if self.product_id != pid:
            print(f"Error: Product with ID {pid} not found.")
            return
        
        if not self.is_available(qty_purchased):
            print(f"Error: Not enough stock. Available stock: {self.stock_qty}")
            return
        
        total_cost = qty_purchased * self.price_per_unit
        if discount > 0:
            total_cost -= total_cost * (discount/100)
            
        self.reduce_stock(qty_purchased)
        
        print(f"Bill:\nProduct ID: {self.product_id}\nPrice per unit: {self.price_per_unit}\nQuantity purchased: {qty_purchased}\nDiscount: {discount}%\nTotal cost: {total_cost}")
p1 = Purchase("P1", 10, 20)
p1.generate_bill("P1", 5, 10)