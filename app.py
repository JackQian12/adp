from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'
db = SQLAlchemy(app)

# 定义一个简单的数据模型
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer)

class Clients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    mobile = db.Column(db.String(80), nullable=False)
    descript =db.Column(db.String(80), nullable=False)
    idno = db.Column(db.String(80), nullable=False)
    

# 创建数据库表（如果不存在）
with app.app_context():
    db.create_all()

# API 路由，返回所有用户
@app.route('/users', methods=['GET'])
def get_users():
    users = Users.query.all()
    return jsonify([{'id': user.id, 'name': user.name,'age':user.age} for user in users])

@app.route('/clients', methods=['GET'])
def get_clients():
    clients = Clients.query.all()
    return jsonify([{'idno': client.idno, 'name': client.name,'mobile':client.mobile,'descript':client.descript} for client in clients])

@app.route('/clients/<mobile>', methods=['GET'])
def search_clients_by_mobile(mobile):
    client = Clients.query.filter_by(mobile=mobile).first()
    if client:
        return jsonify({'id': client.id, 'name': client.name, 'mobile': client.mobile, 'descript': client.descript})
    else:
        return jsonify({'message': 'Client not found'})

@app.route('/clients', methods=['POST'])
def add_client():
    data = request.get_json()
    name = data.get('name')
    mobile = data.get('mobile')
    descript = data.get('descript')
    idno = data.get('idno')
    if not name or not mobile or not descript:
        return jsonify({'message': 'Missing required fields'}), 400
    client = Clients(idno=idno,name=name, mobile=mobile, descript=descript)
    db.session.add(client)
    db.session.commit()
    return jsonify({'message': 'Client added successfully'}), 201


if __name__ == '__main__':
    app.run(debug=True)