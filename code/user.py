import sqlite3
from flask_restful import Resource,reqparse
from flask import Flask,request
class User:
    def __init__(self,_id,username,password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls,username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query= "select * from users where username=?"
        result = cursor.execute(query,(username,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls,_id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query= "select * from users where id=?"
        result = cursor.execute(query,(_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user
class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',type=str,required = True)
    parser.add_argument('password',type=str,required = True)
    def post(self):
        data = UserRegister.parser.parse_args()
        if User.find_by_username(data['username']):
            return {'message':'User with same name exists'},400
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "insert into users values (Null,?,?)"
        cursor.execute(query,(data['username'],data['password']))
        connection.commit()
        connection.close()
        return {'message': 'User created successfully'},201
