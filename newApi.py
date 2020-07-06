import os, sqlite3, json
from flask import Flask, render_template, request, jsonify
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
api = Api(app)

con = sqlite3.connect('./test1.db', check_same_thread=False)
    
with open('./test.json', encoding='utf-8-sig') as f:
    imp_json = json.load(f)


class test1(Resource):
    def get(self, imp_id):
        return imp_json[int(imp_id)-11]

class test2(Resource):
    def get(self):
        return imp_json

api.add_resource(test1, '/imp/<imp_id>')
api.add_resource(test2, '/imp')

@app.route('/api/in')
def api():
    cur = con.cursor()
    sql = 'SELECT * FROM test1'
    cur.execute(sql)
    results = cur.fetchall()
    return render_template('api_in.html', results=results)

@app.route('/api/json')
def serviceJson():
    return jsonify(imp_json)

@app.route('/')
def home():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')