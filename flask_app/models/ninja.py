from flask_app.config.mysqlconnection import connectToMySQL

class Ninja():
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    @classmethod
    def save_ninja(cls, data ):
        query = "INSERT INTO ninjas ( dojo_id, first_name , last_name, age, created_at, updated_at ) VALUES ( %(dojo_id)s, %(fname)s, %(lname)s, %(age)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py

        return connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )