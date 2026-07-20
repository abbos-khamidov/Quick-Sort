import sqlite3

def register_user():
    """Запрашивает у пользователя данные для регистрации."""
    print("=== РЕГИСТРАЦИЯ ПОЛЬЗОВАТЕЛЯ ===")
    name = input("Введите ваше имя: ").strip()
    while not name:
        name = input("Имя не может быть пустым. Введите имя: ").strip()
        
    while True:
        try:
            age = int(input("Введите ваш возраст: "))
            if age <= 0:
                print("Возраст должен быть больше нуля.")
                continue
            break
        except ValueError:
            print("Ошибка ввода! Возраст должен быть целым числом.")
    city = input("Введите город проживания: ").strip()
    while not city:
        city = input("Город не может быть пустым. Введите город: ").strip()
        
    return name, age, city

def init_user_db():
    """Создает базу данных user.db и таблицу users, если они отсутствуют."""
    conn = sqlite3.connect("user.db")
    cursor = conn.cursor()
    

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            city TEXT
        )
    """)

    
    conn.commit()
    conn.close()

def save_user(name, age, city):
    """Сохраняет зарегистрированного пользователя в базу данных user.db."""
    conn = sqlite3.connect("user.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO users (name, age, city) 
        VALUES (?, ?, ?)
    """, (name, age, city))
    
    conn.commit()
    conn.close()
    print(f"\n[Успех] Данные сохранены! Пользователь {name} добавлен в user.db.")


if __name__ == "__main__":
    init_user_db()
    user_name, user_age, user_city = register_user()
    save_user(user_name, user_age, user_city)