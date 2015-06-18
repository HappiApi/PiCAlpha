from db import conn
from flask import Flask, request, jsonify

app = Flask(__name__)

def valid_pic(code):
    return True

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/schools')
def schools():
    # parse query parameter
    pic_code = request.args.get('pic_code')
    if valid_pic(pic_code):
        cursor = conn.cursor()
        cursor.execute('SELECT name, type, admission FROM schools WHERE pic_code={0};'.format(pic_code))
        data = cursor.fetchone()
        if data:
            name = data[0]
            school_type = data[1]
            admission = data[2]
        cursor.close()
        return jsonify(
            pic_code=pic_code,
            name=name,
            type=school_type,
            admission=admission
        )
    else:
        return jsonify(error='pic_code does not exist.')