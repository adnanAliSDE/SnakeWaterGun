import mysql.connector

# Connect with the MySQL Server
cnx = mysql.connector.connect(
    host='localhost', user='root', passwd='admin', database='swg')

my_cursor = cnx.cursor()

data = my_cursor.execute('DESC users;')
print(data)

# my_cursor.execute(
# 'CREATE TABLE games(id INT PRIMARY KEY AUTO_INCREMENT,player_1 INT,player_2 INT,played_at timestamp DEFAULT NOW(),FOREIGN KEY (player_1) references users(id),FOREIGN KEY (player_2) references users(id));')

print('Created table successfully')

# cnx.commit()