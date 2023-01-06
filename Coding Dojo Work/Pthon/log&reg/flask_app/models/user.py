from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (`first_name`, `last_name`, `email`, `password`, `created_at`, `updated_at`) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"

        return connectToMySQL('recipes_db').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users"
        users_from_db = connectToMySQL('recipes_db').query_db(query)
        print(users_from_db)

        users = []
        for u in users_from_db:
            users.append(cls(u))

        return users

    @classmethod
    def get_by_email(cls, data):
        query = " SELECT * FROM users WHERE email = %(login_email)s"
        results = connectToMySQL('recipes_db').query_db(query, data)

        if len(results) < 1:
            return False

        user = cls(results[0])
        return user

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL('recipes_db').query_db(query,data)
        user = cls(results[0])
        return user

    @staticmethod
    def validate_registration(data):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL('recipes_db').query_db(query, data)

        #Email already exists
        if len(results) > 1:
            flash("Email already taken" , "register")
            is_valid = False

        #Improper Email Format
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid Email" , "register")
            is_valid = False
        
        # First Name present and at least 2 characters
        if not data['first_name'] or len(data['first_name']) < 2:
            flash("First name must at least be 2 characters"  , "register")
            is_valid = False
    
        # Last Name present and at least 2 characters
        if not data['last_name'] or len(data['last_name']) < 2:
            flash("Last name must at least be 2 characters"  , "register")
            is_valid = False

        # Password present and at least 2 characters
        if not data['password'] or len(data['password']) < 8:
            flash("Password must at least be 8 characters"  , "register")
            is_valid = False

        # Password confirmation present and at least 2 characters
        if not data['pw_conf'] or len(data['pw_conf']) < 8:
            flash("Confirm password must at least be 8 characters" , "register")
            is_valid = False

        #Password and confirm password match
        if data['password'] != data['pw_conf']:
            flash("Passwords must match"  , "register")
            is_valid = False

        return is_valid