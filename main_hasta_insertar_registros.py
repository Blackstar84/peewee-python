import peewee
from datetime import datetime

database = peewee.MySQLDatabase(database='pythondb', host='localhost', port=3306, user='root', passwd='root')


# users
class User(peewee.Model):
    username = peewee.CharField(max_length=50, unique=True, index=True)
    email = peewee.CharField(max_length=60, null=False, )
    active = peewee.BooleanField(default=False)
    created_at = peewee.DateTimeField(default=datetime.now)
    
    class Meta:
        database = database
        db_table = 'users'
        
    def __str__(self):
        return self.username    
        
            
if __name__ == '__main__':
    
    if User.table_exists():
        User.drop_table()
        
    User.create_table()
    
    #Método 1
    user1 = User(username='user1', email='user1@example.com', active=True)

    """ print(user1)
    print(user1.email)
    print(user1.active) """
    
    user1.save()
    
    # Método 2
    user2 = User()
    user2.username = 'user2'
    user2.email = 'user2@example.com'
    user2.save()
    
    # Método 3
    
    values = {
        'username': 'user3',
        'email': 'user3@example.com'
    }
    
    user3 = User(**values)
    user3.save()
    
    user4 = User.create(username='user4', email='user4@example.com')
    print(user4.id)
    
    query = User.insert(username='user5', email='user5@example.com')
    print(query)
    print(type(query)) # Es del tipo Model Insert
    query.execute()
    
    
    