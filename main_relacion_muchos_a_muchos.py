import peewee
from datetime import datetime

database = peewee.MySQLDatabase(database='pythondb', host='localhost', port=3306, user='root', passwd='root')

class Product(peewee.Model):
    title = peewee.CharField(max_length=50)
    price = peewee.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        database = database
        db_table = 'products'
        
    def __str__(self) -> str:
        return self.title    

class Category(peewee.Model):
    title = peewee.CharField(max_length=20)
    
    class Meta:
        database = database
        db_table = 'categories'
        
    def __str__(self) -> str:
        return self.title 
    
    
class ProductCategory(peewee.Model):
    product = peewee.ForeignKeyField(Product, backref='categories')
    category = peewee.ForeignKeyField(Category, backref='products')   
    
    class Meta:
        database = database
        db_table = 'product_categories'
    

            
if __name__ == '__main__':
    
    database.drop_tables([Product, Category, ProductCategory])
    database.create_tables([Product, Category, ProductCategory])
    
    ipad = Product.create(title='Ipad', price=500.50)
    iphone = Product.create(title='Iphone', price=800)
    tv = Product.create(title='Tv', price=600)
    
    technology = Category.create(title='Technology')
    home = Category.create(title='Home')
    
    ProductCategory.create(product=ipad, category=technology)
    ProductCategory.create(product=iphone, category=technology)
    ProductCategory.create(product=tv, category=technology)
    
    ProductCategory.create(product=tv, category=home)
    
    
    for product_category in technology.products:
        # print(type(product))
        print(product_category.product)
    
    for product_category in tv.categories:
        print(product_category.category)
    
    
    
    
    
    
    