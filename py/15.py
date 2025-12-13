# DATABASE (SQLITE)

"""
sqlite:
    · SQLite3 comes pre-installed with Python
    · Serverless
    · Single file database (self-contained)

Basic Commands:
    . CREATE: create a table for database
    . INSERT: create data
    . SELECT: read data
    · UPDATE: update data
    . DELETE: delete data
"""
#---------------------------------------------
# Initialize database (CREATE):

import sqlite3

class DatabaseManager:
    def __init__(self, db_name='example.db'):
        self.db_name = db_name
        self.init_database()

    def init_database(self):
        """ Initialize database with tables """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    age INTEGER,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS posts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    title TEXT NOT NULL,
                    content TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users(id)
                    )
                ''')

#------------------------------------------------------
# Create data (INSERT):

    def create_user(self, name, email, age):
        """Create a new user"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO users (name, email, age) VALUES (?, ?, ?)
                ''', (name, email, age))
                return cursor.lastrowid
        except sqlite3.IntegrityError as e:
            print(f"Error: {e}")
            return None

#------------------------------------------------------
 # Create data (INSERT):

    def create_post(self, user_id, title, content):
        """Create a new post"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO posts (user_id, title, content) VALUES (?, ?, ?)
            ''', (user_id, title, content))
            return cursor.lastrowid

#------------------------------------------------------        
# Read data (SELECT):

    def get_all_users(self):
        """Get all users"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users')
            return cursor.fetchall()

#------------------------------------------------------
# Read data (SELECT):

    def get_user_posts(self, user_id):
        """Get posts by user"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT p.id, p.title, p.content, p.created_at
                FROM posts p
                WHERE p.user_id = ?
                ORDER BY p.created_at DESC
            ''', (user_id,))
            return cursor.fetchall()

#------------------------------------------------------
 # Delete data (DELETE):

    def delete_user(self, user_id):
        """Delete a user and their posts"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM posts WHERE user_id = ?', (user_id,))
            cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
            return cursor.rowcount > 0

#------------------------------------------------------
# Update data (UPDATE):

    def update_user(self, user_id, name=None, email=None, age=None):
        """Update user information"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                
                # Build dynamic UPDATE query
                updates = []
                params = []
                
                if name:
                    updates.append("name = ?")
                    params.append(name)
                if email:
                    updates.append("email = ?")
                    params.append(email)
                if age:
                    updates.append("age = ?")
                    params.append(age)
                
                if not updates:
                    print("No fields to update")
                    return False
                
                params.append(user_id)
                query = f"UPDATE users SET {', '.join(updates)} WHERE id = ?"
                cursor.execute(query, params)
                return cursor.rowcount > 0
        except sqlite3.IntegrityError as e:
            print(f"Error: {e}")
            return False

#------------------------------------------------------
# Run on Terminal Function:

def display_menu():
    """Display the main menu"""
    print("\n" + "="*40)
    print("          DATABASE MANAGER")
    print("="*40)
    print("1. Create User")
    print("2. View All Users")
    print("3. Create Post")
    print("4. View User Posts")
    print("5. Update User")
    print("6. Delete User")
    print("7. Exit")
    print("-" * 40)

def main():
    """Main interaction CLI function"""
    db = DatabaseManager()

    while True:
        display_menu()
        choice = input("Select an option (1-6): ").strip()

        if choice == '1':
            print("\n-- Create New User --")
            name = input("Enter Name: ").strip()
            email = input("Enter Email: ").strip()
            try:
                age = int(input("Enter Age: ").strip())
                user_id = db.create_user(name, email, age)
                if user_id:
                    print(f"User created successfully! ID: {user_id}")
                else:
                    print("Failed to create user")
            except ValueError:
                print(" Invalid age. Please enterr a number")
        
        elif choice == '2':
            print("\n--- All users ---")
            users = db.get_all_users()
            if users:
                for user in users:
                    print(f"ID: {user[0]} | Name: {user[1]} | Email: {user[2]} | Age: {user[3]}")
            else:
                print("No users found.")
        
        elif choice == '3':
            print("\n--- Create New Post ---")
            try:
                user_id = int(input("Enter user ID: ").strip())
                title = input("Enter post title: ").strip()
                content = input("Enter post content: ").strip()
                post_id = db.create_post(user_id, title, content)
                if post_id:
                    print(f"Post created successfully! ID {post_id}")
                else:
                    print("Failed to created post")
            except ValueError:
                print("Invalid user ID. Please enter a number.")
        
        elif choice == '4':
            try:
                user_id = int(input("Enter user ID: ").strip())
                posts = db.get_user_posts(user_id)
                if posts:
                    for post in posts:
                        print(f"\nPost ID: {post[0]}")
                        print(f"Title: {post[1]}")
                        print(f"Content: {post[2]}")
                        print(f"created: {post[3]}")
                        print("-" * 30)
                else:
                    print("No post found for this user.")
            except ValueError:
                print("Invalid user ID. Please enter a number.")

        elif choice == '5':
            print("\n--- Update User ---")
            try:
                user_id = int(input("Enter user ID to update: ").strip())
                print("Leave field empty to skip")
                name = input("Enter new name (or skip): ").strip() or None
                email = input("Enter new email (or skip): ").strip() or None
                age_input = input("Enter new age (or skip): ").strip()
                age = int(age_input) if age_input else None
                
                if db.update_user(user_id, name, email, age):
                    print("User updated successfully!")
                else:
                    print("Failed to update user or user not found")
            except ValueError:
                print("Invalid input. Please enter valid data")
        

        elif choice == '6':
            print("\n --- Delete User ---")
            try:
                user_id = int(input("Enter user ID to delete: ").strip())
                confirm = input(f"are you sure you want to delete user {user_id}? (y/n): ").strip().lower()
                if confirm == "y":
                    if db.delete_user(user_id):
                        print("user deleted successfully!")
                    else:
                        print("Deletion cancelled")
            except ValueError:
                print("\n Invalid user ID. Please enter a number")           
        
        elif choice == '7':
            print("\nGoodbye!")
            break

        else:
            print("Invalid choice. Please enter 1-6")

        input("\Press Enter to continue...")

if __name__ == "__main__":
    main()