# DATABASE (MONGO)

"""
MongoDB Atlas:
· https://www.mongodb.com
. Cloud database service for MongoDB
. 512mb free tier
· pip install pymongo
"""

"""
Initialize:
· pip install pymongo
· pip install python-dotenv
"""

# Initialize:

from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os

load_dotenv()   # Load enviroment variables from .env file

mongo_uri = os.getenv('MONGODB_ATLAS_CLUSTER_URI' )

class DatabaseManager:
    def __init__(self, db_name='example_db', connection_string=mongo_uri):
        self.client = MongoClient(connection_string)
        self.db = self.client[db_name]
        self.users_collection = self.db.users
        self.posts_collection = self.db.posts
        self.init_database()

    def init_database(self):
        """Initialize database with collections and indexes"""
        # Create unique index on email for users
        self.users_collection.create_index("email", unique=True)
        # Create index on user_id for posts for better query performance
        self.posts_collection.create_index("user id")

# Create function:

    def create_user(self, name, email, age):
        """Create a new user"""
        try:
            user_doc = {
            "name": name,
            "email": email,
            "age": age,
            "created_at": datetime.now()
        }

            result = self.users_collection.insert_one(user_doc)
            return str(result.inserted_id)
        except Exception as e:
            print(f"Error: {e}")
            return None
        
    def create_post(self, user_id, title, content):
        """Create a new post"""
        try:
            # Convert string user_id to ObjectId if it's a valid ObjectId
            if ObjectId.is_valid(user_id):
                user_object_id = ObjectId(user_id)
            else:
                user_object_id = user_id

            post_doc = {
                "user_id": user_object_id,
                "title": title,
                "content": content,
                "created_at": datetime.now()
            }

            result = self.posts_collection. insert_one(post_doc)
            return str(result.inserted_id)
        except Exception as e:
            print(f"Error creating post: {e}")
            return None

# Read Function:

    def get_all_users(self):
        "Get all users"
        try:
            users = list(self.users_collection.find())
            # Convert ObjectId to string for display
            for user in users:
                user['_id'] = str(user['_id'])
            return users
        except Exception as e:
            print(f"Error fetching users: {e}")
            return []

    def get_user_posts(self, user_id):
        """Get posts by user"""
        try:
        # Convert string user_id to ObjectId if it's a valid ObjectId
            if ObjectId.is_valid(user_id):
                user_object_id = ObjectId(user_id)
            else:
                user_object_id = user_id

            posts = list(self.posts_collection.find(
                {"user_id": user_object_id}
            ).sort("created_at", -1))

        # Convert ObjectId to string for display
            for post in posts:
                    post['_id'] = str(post['_id'])
                    post['user_id'] = str(post['user_id'])

            return posts
        except Exception as e:
            print(f"Error fetching posts: {e}")
            return []

# Update Functions in DatabaseManager class:

def update_user(self, user_id, name, email, age):
    """Update user fields
    
    Args:
        user_id: User's ObjectId or string ID
        name: User's name
        email: User's email
        age: User's age
    
    Returns:
        bool: True if update successful, False otherwise
    """
    try:
        # Convert string user_id to ObjectId if valid
        if ObjectId.is_valid(user_id):
            user_object_id = ObjectId(user_id)
        else:
            user_object_id = user_id
        
        # Add updated_at timestamp
        update_fields = {
            "name": name,
            "email": email,
            "age": age,
            "updated_at": datetime.now()
        }
        
        result = self.users_collection.update_one(
            {"_id": user_object_id},
            {"$set": update_fields}
        )
        
        return result.modified_count > 0
    except Exception as e:
        print(f"Error updating user: {e}")
        return False

def update_post(self, post_id, title, content):
    """Update post fields
    
    Args:
        post_id: Post's ObjectId or string ID
        title: New title
        content: New content
    
    Returns:
        bool: True if update successful, False otherwise
    """
    try:
        # Convert string post_id to ObjectId if valid
        if ObjectId.is_valid(post_id):
            post_object_id = ObjectId(post_id)
        else:
            post_object_id = post_id
        
        # Build update dict with updated_at timestamp
        update_fields = {
            "title": title,
            "content": content,
            "updated_at": datetime.now()
        }
        
        result = self.posts_collection.update_one(
            {"_id": post_object_id},
            {"$set": update_fields}
        )
        
        return result.modified_count > 0
    except Exception as e:
        print(f"Error updating post: {e}")
        return False


 # Delete Function

    def delete_user(self, user_id):
        """Delete user and their posts"""
        try:
            # Convert string user_id to ObjectId if it's a valid ObjectId
            if ObjectId.is_valid(user_id):
                user_object_id = ObjectId(user_id)
            else:
                user_object_id = user_id

            # Delete user's posts first
            self.posts_collection.delete_many({"user_id": user_object_id})

            # Delete the user
            result = self.users_collection.delete_one({"_id": user_object_id})
            return result.deleted_count > 0
        except Exception as e:
            print(f"Error deleting user: {e}")
            return False
        
# Close DB Function:

    def close_connection(self):
        """Close the MongoDB connection"""
        self.client.close()

# Run on Terminal Funtion:

def display_menu():
    """ Display the main menu """
    print("\n" + "="*40)
    print("         DATABASE MANAGER")
    print("="*40)
    print("1. Create User")
    print("2. View All Users")
    print("3. Create Post")
    print("4. View User Posts")
    print("5. Update User")
    print("6. Update Post")
    print("7. Delete User")
    print("8. Exit")  # Change from 6 to 9
    print("-"*40)

def main():
    """Main interactive CLI function """
    try:
        db = DatabaseManager()
        print("/ Connected to MongoDB successfully!")
    except Exception as e:
        print(f"X Failed to connect to MongoDB: {e}")
        print("Make sure MongoDB is running on localhost:27017")
        return
    

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            print("\n --- Create New User --- ")
            name = input("Enter name: ").strip()
            email = input("Enter email: ").strip()
            try:
                age = int(input("Enter age: ").strip())
                user_id = db.create_user(name, email, age)
                if user_id:
                    print(f"/ User created successfully! ID: {user_id}")
                else:
                    print("X Failed to create user")
            except ValueError:
                print("X Invalid age. Please enter a number.")

        elif choice == '2':
            print("\n --- All Users ---")
            users = db.get_all_users()
            if users:
                for user in users:
                    print(f"ID: {user['_id']} | Name: {user['name']} | Email: {user['email']} | Age: {user['age']}")

            else:
                print("No users found.")

        elif choice == '3':
            print("\n --- Create New Post --- ")
            user_id = input("Enter user ID: ").strip()
            title = input("Enter post title: ").strip()
            content = input("Enter post content: ").strip()
            post_id = db.create_post(user_id, title, content)
            if post_id:
                print(f"/ Post created successfully! ID: {post_id}")
            else:
                print("X Failed to create post")

        elif choice == '4':
            print("\n --- View User Posts --- ")
            user_id = input("Enter user ID: ").strip()
            posts = db.get_user_posts(user_id)
            if posts:
                for post in posts:
                    print(f"\nPost ID: {post['_id']}")
                    print(f"Title: {post['title']}")
                    print(f"Content: {post['content']}")
                    print(f"Created: {post['created_at']}")
                    print("-" * 30)
            else:
                print("No posts found for this user.")

        elif choice == '5':
            print("\n --- Update User --- ")
            user_id = input("Enter user ID: ").strip()
            print("Leave blank to skip updating a field")
            name = input("Enter new name: ").strip() or None
            email = input("Enter new email: ").strip() or None
            age_input = input("Enter new age: ").strip()
            age = int(age_input) if age_input else None
            
            if db.update_user(user_id, name=name, email=email, age=age):
                print("✓ User updated successfully!")
            else:
                print("✗ Failed to update user")

        elif choice == '6':
            print("\n --- Update Post --- ")
            post_id = input("Enter post ID: ").strip()
            print("Leave blank to skip updating a field")
            title = input("Enter new title: ").strip() or None
            content = input("Enter new content: ").strip() or None
            
            if db.update_post(post_id, title=title, content=content):
                print("✓ Post updated successfully!")
            else:
                print("✗ Failed to update post")

        elif choice == '7':
            print("\n --- Delete User --- ")
            user_id = input("Enter user ID to delete: ").strip()
            confirm = input(f"Are you sure you want to delete user {user_id}? (y/N): ").strip().lower()
            if confirm == 'y':
                if db.delete_user(user_id):
                    print("/ User deleted successfully!")
                else:
                    print("X User not found or deletion failed.")

            print("Deletion cancelled.")

        elif choice == '8':
            print("\nClosing database connection ... ")
            db.close_connection()
            print("Goodbye!")
            break

        else:
            print("X Invalid choice. Please enter 1-6.")

        input("\nPress Enter to continue ... ")

if __name__ == "__main__":
    main()