import mysql.connector
from cryptography.fernet import Fernet
import bcrypt
from typing import Optional
import tkinter as tk
from tkinter import messagebox,simpledialog


class DatabaseManager:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor(buffered=True)
        
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        user = self.auth_manager.authenticate_user(username,password)
        if user : self.setup_password_manager_interface(user)
        else: messagebox.showerror("Login failed", "Invalid username or password")

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                password_hash VARCHAR(255) NOT NULL,
                mfa_data BLOB
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS passwords (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                service_name VARCHAR(255) NOT NULL,
                encrypted_password BLOB NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        """)
        self.connection.commit()

    def add_user(self, username, password_hash, mfa_data):
        sql = "INSERT INTO users (username, password_hash, mfa_data) VALUES (%s, %s, %s)"
        val = (username, password_hash, mfa_data)
        self.cursor.execute(sql, val)
        self.connection.commit()
        return self.cursor.lastrowid

    def view_passwords(self, user_id):
        passwords = self.db_manager.get_passwords(user_id)
        print(passwords, type(passwords))
        return passwords
    
    def add_password(self, user_id, service_name, encrypted_password):
        sql = "INSERT INTO passwords (user_id, service_name, encrypted_password) VALUES (%s, %s, %s)"
        val = (user_id, service_name, encrypted_password)
        self.cursor.execute(sql, val)
        self.connection.commit()

    def get_user_by_username(self, username):
        sql = "SELECT * FROM users WHERE username = '"+username+"';"
        print(sql)
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        if result:
            return {
                'id': result[0],
                'username': result[1],
                'password_hash': result[2],
            }
        return None

    def get_passwords(self, user_id):
        sql = "SELECT service_name, encrypted_password FROM passwords WHERE user_id = %s"
        self.cursor.execute(sql, (user_id,))
        data = self.cursor.fetchall()
        return data

    def close(self):
        self.connection.close()
        
class AuthenticationManager:
    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager

    def hash_password(self, password: str) -> bytes:
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    def verify_password(self, stored_password_hash: bytes, provided_password: str) -> bool:
        return bcrypt.checkpw(provided_password.encode(), stored_password_hash.encode())

    def authenticate_user(self, username: str, password: str) -> Optional[int]:
        user = self.db_manager.get_user_by_username(username)
        print(user)
        if user and self.verify_password(user['password_hash'], password):
            return user['id']
        return None
         
class EncryptionManager:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

    def encrypt_password(self, key, password: str) -> bytes:
        self.key = key
        self.cipher_suite = Fernet(self.key)
        return self.cipher_suite.encrypt(password.encode())

    def decrypt_password(self, key, encrypted_password: bytes) -> str:
        self.key = key
        self.cipher_suite = Fernet(self.key)
        return self.cipher_suite.decrypt(encrypted_password).decode()

    def get_encryption_key(self) -> str:
        return self.key.decode()