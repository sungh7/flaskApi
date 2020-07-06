from flask import Flask
from flask_restful import Resource, Api, reqparse
from requests import get, post
app = Flask(__name__)
api = Api(app)

todos = {} 

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def post(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_di: todos[todo_id]}

api.add_resource(TodoSimple, '/<string:todo_id>')


if __name__ == '__main__':
    app.run(debug=True)

