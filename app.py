from flask import Flask, render_template, request
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'
db = SQLAlchemy(app)


def check_connection():
    try:
        engine = db.engine
        with engine.connect() as connection:
            return True
    except Exception as e:
        return False

# 定义一个简单的数据模型
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer)

# 定义一个理赔台账的数据模型
class Client(db.Model):
    id = db.Column(db.String(80), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    mobile = db.Column(db.String(200), nullable=False)
    descript = db.Column(db.String(2000), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    if check_connection():
        print("Database connection is successful.")
    else:
        print("Database connection failed.")
    app.run(debug=True)

# API 路由，返回所有用户
@app.route('/getusers', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'name': user.name} for user in users])

@app.route('/addusers', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = User(name=data['name'], age=data['age'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User added successfully'}), 201

# API 路由，返回所有报案人
@app.route('/getclients', methods=['GET'])
def get_Clients():
    Clients = Client.query.all()
    return jsonify([{'id': client.id, 'name': client.name,'mobile':client.mobile,'descript':client.descript} for client in Clients])

@app.route('/addclients', methods=['POST'])
def add_Client():
    data=request.get_json()
    new_client=Client(name=data['name'],mobile=data['mobile'],descript=data['descript'])
    db.session.add(new_client)
    db.session.commit()
    return jsonify({'message':'new client added'})

