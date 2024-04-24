import sqlite3

database_path = 'db.sqlite3'

# Создание подключения к базе данных
conn = sqlite3.connect(database_path)

# Создание курсора
cursor = conn.cursor()

# Использование курсора для выполнения SQL-запроса
try:
   
    cursor.execute('''SELECT * FROM auth_user''')
    for row in cursor.fetchall():
        print(row)
        
except sqlite3.Error as e:
    print(f"An error occurred: {e}")

finally:
    # Закрытие курсора и подключения
    cursor.close()
    conn.close()
