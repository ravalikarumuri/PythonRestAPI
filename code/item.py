import sqlite3
from flask import Flask,request
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
    type =float,
    required=True,
    help="this field cannot be left blank"
    )

    @classmethod
    def find_by_name(cls,name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "select * from items where name = ?"
        result=cursor.execute(query,(name,))
        row= result.fetchone()
        connection.close()
        if row:
            return(row[0])

    @jwt_required()
    def get(self, name):
        item = self.find_by_name(name)
        if item:
            return(item)
        return {'message':'Item not found'},404

    def post(self,name):
        item = self.find_by_name(name)
        if item:
            return{'message':"an item with name'{}' already exists".format(name)},400
        data =Item.parser.parse_args()
        item = {'name':name,'price':data['price']}
        connection =sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "insert into items values(Null,?,?)"
        cursor.execute(query,(item['name'],item['price']))
        connection.commit()
        connection.close()
        return item,201

    def delete(self,name):
        global items
        items = list(filter(lambda x: x['name']!= name,items))
        return{'message':"Deleted successfully"},200

    def put(self,name):
        data =Item.parser.parse_args()
        item = next(filter(lambda x :x['name']== name,items),None)
        if item is None:
            item = {'name':name,'price':data['price']}
            items.append(item)
        else:
            item.update(data)
        return item
class ItemList(Resource):
    def get(self):
        return{'items':items}
