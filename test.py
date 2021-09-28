import sqlite3

try:
    conn = sqlite3.connect('accountant.db')
    cursor = conn.cursor()

    #     Создадим пользователя с user_id = 1000
    cursor.execute("INSERT OR IGNORE INTO `users` (`user_id`) VALUES (?)", (1002,))

    #     Считываем всех пользователей
    users = cursor.execute("SELECT * FROM `users` ")
    print(users.fetchall())

    #     Подтверждаем изменения
    conn.commit()

except sqlite3.Error as error:
    print('Error', error)

finally:
    if(conn):
        conn.close()

print('555')