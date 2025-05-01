import hashlib;
import sqlite3;

conn = sqlite3.connect("LoginDB.db")
cursor = conn.cursor()

def init_db():
        cursor.execute("""
               CREATE TABLE IF NOT EXISTS users (
               username TEXT PRIMARY KEY,
               hashed_password TEXT NOT NULL,
               admin INTEGER DEFAULT 0
            )
        """)
        conn.commit()


def hash_password(password):
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return hashed

def add_user_to_database(username, hashed_pass):
    
    cursor.execute("INSERT INTO users (username, hashed_password) VALUES (?, ?)", (username, hashed_pass))
    conn.commit()


def check_login(username, hashed_pass):
    cursor.execute("SELECT * FROM users WHERE username = ? AND hashed_password = ?", (username, hashed_pass))
    result = cursor.fetchone()
    return bool(result)

def admin_login(username, hashed_pass):
    cursor.execute ("SELECT * FROM users WHERE username = ? AND hashed_password = ? AND admin = 1", (username, hashed_pass))
    result = cursor.fetchone()
    return bool(result)

def view_users():
    cursor.execute("SELECT username FROM users WHERE admin = 0")
    userList = cursor.fetchall()
    for row in userList:
        print(row[0])



def main():
    init_db()
    print("1. Create an Account \n 2. Login \n 3. Admin Login \n 4. Exit")
    while True:
        user_choice = int(input("Choose an option:   "))
        if user_choice == 1:
            while True:
                username = input("Enter your username: ")
                if cursor.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone():
                    print("Sorry, username already exists. Try again.")
                else:
                    break
            password = input("Enter your password: ")
            hashed_pass = hash_password(password)
            add_user_to_database(username, hashed_pass)
            print("Account created!")
        elif user_choice == 2:
            username = input("Username: ")
            password = input("Password: ")
            hashed_pass = hash_password(password)
            if check_login(username, hashed_pass):
                print("Login complete!")
            else:
                print("Login failed!")
        elif user_choice == 3:
            username = input("Username: ")
            password = input("Password: ")
            hashed_pass = hash_password(password)
            if admin_login(username, hashed_pass):
                print("Admin login successful!\n")
                print("User List: ")
                view_users()
            else:
                print("Admin login failed.")
        elif user_choice == 4:
            cursor.close()
            conn.close()
            exit()
        else:
            print("Enter a valid option.")

if __name__ == "__main__":
    main()
