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
    
    users = [
        {'username': 'user1', 'email': 'user1@example.com', 'active': True},
        {'username': 'user2', 'email': 'user2@example.com'},
        {'username': 'user3', 'email': 'user3@example.com', 'active': True},
        {'username': 'user4', 'email': 'user4@example.com'},
        {'username': 'user5', 'email': 'user5@example.com'},
        {'username': 'user6', 'email': 'user6@example.com', 'active': True},
        {'username': 'user7', 'email': 'user7@example.com', 'active': True},
    ]
    
    
    query = User.insert_many(users)
    query.execute()
    
    
    # SELECT * FROM users;
    users = User.select() # Es del tipo MODEL SELECT

    #print(users)
    
    """ for user in users:
        print(user.email) """
    
    # SELECT username, email, active FROM users WHERE active = 1;    
    users = User.select(User.username, User.email, User.active).where(
        (User.active == True) & (User.id > 3)
        )    
    
    """ for user in users:
        print(user)
     """    
        
   # SELECT username, email, active FROM users WHERE active = 1 and (id=1 or id=7);    
    users = User.select(User.username,
                        User.email, 
                        User.active
    ).where(
        (User.active == True) &
        (
            (User.id ==1 ) | (User.id == 7)
        )
    )    
    
    for user in users:
        print(user)     