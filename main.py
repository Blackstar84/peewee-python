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
    
    # ORDER BY
    # users = User.select().where(
    #     User.active == True
    # ).order_by(User.username.desc()).limit(2)
    
    # print(users)
    
    # for user in users:
    #     print(user)
        
    # user = User.select().where(User.username == 'user1').first()
    # print(type(user))
    # print(user)
    
    # try:
    #     user = User.select().where(User.username == 'user11').get()
    # except User.DoesNotExist as err:
    #     print('No fue posible encontrar el usuario!')
        
    # user = User.select().where(User.username == 'user11').first()
    
    # if user:
    #     print(user)
    # else:
    #     print('No fue posible encontrar el usuario!')       
    
     
    
    # Validar existencia de Registros
    # count = User.select().where(User.username == 'user11').count()
    # print(count)
    
    # if count > 0:
    #     print('El usuario existe en la tabla')
    # else:
    #     print('No fue posible obtener el usuario')
        
    # existe = User.select().where(User.username == 'user11').exists()
    # print(existe)
    
    # if existe:
    #     print('El usuario existe en la tabla')
    # else:
    #     print('No fue posible obtener el usuario')
    
    # Actualizar Registros
    
    user = User.select().where(User.id == 1).get()
    # print(user)
    
    # # Primera Forma

    # user.username = 'Nuevo username'
    # user.email = 'nuevo_emai@example.com'
    
    # user.save()
    
    
    # # Segunda Forma
    
    # query = User.update(username='User2 nuevo valor', email= 'user2_nuevovalorexample.com').where(User.id == 2)
    # print(type(query))
    # query.execute()
    # print(type(query))
    
    user = User.select().where(User.username == 'user7').get()
    
    # Primera forma de eliminar
    
    user.delete_instance()
    
    
    
    
    
    
    