from flask import Flask, jsonify, request
"""
This module sets up a Flask web application with SQLAlchemy for database management. 
It defines three data models: Users, Clients, and Report, and provides several API routes 
for interacting with the Users and Clients models.
Classes:
    Users: A model representing a user with an id, name, and age.
    Clients: A model representing a client with an id, name, mobile, description, and id number.
    Report: A model representing a report with various attributes.
Functions:
    get_users(): API route to get all users.
    get_clients(): API route to get all clients.
    search_clients_by_mobile(mobile): API route to search for a client by mobile number.
    add_client(): API route to add a new client.
Usage:
    Run this module to start the Flask web application. The application will create the necessary 
    database tables if they do not already exist and provide API endpoints for interacting with 
    the Users and Clients models.
"""
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

"""
Serial number（序号）-SN
Labor company（人力公司）-LC
Insured（被保险人）-I
Name of the insured person in danger（出险人姓名）-NIPID
Occupation name（职业名称）-ON
ID number of the insured person in danger（出险人身份证号）-IDNIPID
Mobile phone number（手机号码）-MPN
Policy number（保单号）-PN
Reporting time（报案时间）-RT
Date of occurrence（出险日期）-DOC
Time of occurrence（出险时间）-TOC
Location of occurrence（出险地址）-LOC
Description of danger（险情描述）-DOD
Accident type（事故类型）-AT
Accident cause（事故原因）-AC
Single/dual-party accident（单 / 双方事故）-S/DA
Whether there is violation（是否违规）-WV
Liability division（责任划分）-LD
Type of occurrence liability（出险责任类型）-TOL
Customer service staff（客服人员）-CSS
Case status（案件状态）-CS
Report number（报案号）-RN
Payout amount（赔付金额）-PA
Accidental medical treatment（意外医疗）-AMT
Third-party medical treatment（三者医疗）-TPMT
Third-party property（三者财产）-TPP
Allowance（津贴）-ALL
Disability（伤残）-DIS
Payout date（赔付日期）-PD
Second follow-up visit（二次回访）-SFV
Remarks（备注）-REM
Date of reporting to Ping An（报案至平安日期）-DRPA

"""
class Report(db.Model):
    SN = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    LC = db.Column(db.String(80))
    Insured = db.Column(db.String(80))
    NIPID = db.Column(db.String(80))
    ON = db.Column(db.String(80))
    IDNIPID = db.Column(db.String(80))
    MPN = db.Column(db.String(80))
    PN = db.Column(db.String(80))
    RT = db.Column(db.String(80))
    DOC = db.Column(db.String(80))
    TOC = db.Column(db.String(80))
    LOC = db.Column(db.String(2000))
    DOD = db.Column(db.String(2000))
    AT = db.Column(db.String(80))
    AC = db.Column(db.String(80))
    SDA = db.Column(db.String(80))
    WV = db.Column(db.String(80))
    LD = db.Column(db.String(80))
    TOL = db.Column(db.String(80))
    CSS = db.Column(db.String(80))
    CS = db.Column(db.String(80))
    RN = db.Column(db.String(80))
    PA = db.Column(db.String(80))
    AMT = db.Column(db.String(80))
    TPMT = db.Column(db.String(80))
    TPP = db.Column(db.String(80))
    Allowance = db.Column(db.String(80))
    Disability = db.Column(db.String(80))
    Payoutdate = db.Column(db.String(80))
    SFV = db.Column(db.String(80))
    Remarks = db.Column(db.String(2000))
    DRPA = db.Column(db.String(80))
    



        
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

@app.route('/reports', methods=['POST'])
def add_report():
        data = request.get_json()
        report = Report(
            LC=data.get('LC'),
            Insured=data.get('Insured'),
            NIPID=data.get('NIPID'),
            ON=data.get('ON'),
            IDNIPID=data.get('IDNIPID'),
            MPN=data.get('MPN'),
            PN=data.get('PN'),
            RT=data.get('RT'),
            DOC=data.get('DOC'),
            TOC=data.get('TOC'),
            LOC=data.get('LOC'),
            DOD=data.get('DOD'),
            AT=data.get('AT'),
            AC=data.get('AC'),
            SDA=data.get('SDA'),
            WV=data.get('WV'),
            LD=data.get('LD'),
            TOL=data.get('TOL'),
            CSS=data.get('CSS'),
            CS=data.get('CS'),
            RN=data.get('RN'),
            PA=data.get('PA'),
            AMT=data.get('AMT'),
            TPMT=data.get('TPMT'),
            TPP=data.get('TPP'),
            Allowance=data.get('Allowance'),
            Disability=data.get('Disability'),
            Payoutdate=data.get('Payoutdate'),
            SFV=data.get('SFV'),
            Remarks=data.get('Remarks'),
            DRPA=data.get('DRPA')
        )
        db.session.add(report)
        db.session.commit()
        return jsonify({'message': 'Report added successfully'}), 201

@app.route('/reports', methods=['GET'])
def get_reports():
    reports = Report.query.all()
    return jsonify([{
        'SN': report.SN,
        'LC': report.LC,
        'Insured': report.Insured,
        'NIPID': report.NIPID,
        'ON': report.ON,
        'IDNIPID': report.IDNIPID,
        'MPN': report.MPN,
        'PN': report.PN,
        'RT': report.RT,
        'DOC': report.DOC,
        'TOC': report.TOC,
        'LOC': report.LOC,
        'DOD': report.DOD,
        'AT': report.AT,
        'AC': report.AC,
        'SDA': report.SDA,
        'WV': report.WV,
        'LD': report.LD,
        'TOL': report.TOL,
        'CSS': report.CSS,
        'CS': report.CS,
        'RN': report.RN,
        'PA': report.PA,
        'AMT': report.AMT,
        'TPMT': report.TPMT,
        'TPP': report.TPP,
        'Allowance': report.Allowance,
        'Disability': report.Disability,
        'Payoutdate': report.Payoutdate,
        'SFV': report.SFV,
        'Remarks': report.Remarks,
        'DRPA': report.DRPA
    } for report in reports])


@app.route('/reports/search_by_mobile', methods=['POST'])
def search_reports_by_mobile_post():
        data = request.get_json()
        mobile = data.get('mobile')
        if not mobile:
            return jsonify({'message': 'Mobile number is required'}), 400
        reports = Report.query.filter_by(MPN=mobile).all()
        if not reports:
            return jsonify({'message': 'No reports found for the given mobile number'}), 404
        return jsonify([{
            'SN': report.SN,
            'LC': report.LC,
            'Insured': report.Insured,
            'NIPID': report.NIPID,
            'ON': report.ON,
            'IDNIPID': report.IDNIPID,
            'MPN': report.MPN,
            'PN': report.PN,
            'RT': report.RT,
            'DOC': report.DOC,
            'TOC': report.TOC,
            'LOC': report.LOC,
            'DOD': report.DOD,
            'AT': report.AT,
            'AC': report.AC,
            'SDA': report.SDA,
            'WV': report.WV,
            'LD': report.LD,
            'TOL': report.TOL,
            'CSS': report.CSS,
            'CS': report.CS,
            'RN': report.RN,
            'PA': report.PA,
            'AMT': report.AMT,
            'TPMT': report.TPMT,
            'TPP': report.TPP,
            'Allowance': report.Allowance,
            'Disability': report.Disability,
            'Payoutdate': report.Payoutdate,
            'SFV': report.SFV,
            'Remarks': report.Remarks,
            'DRPA': report.DRPA
        } for report in reports])

@app.route('/reports/search_by_pn', methods=['POST'])
def search_reports_by_pn():
    data = request.get_json()
    pn = data.get('PN')
    if not pn:
        return jsonify({'message': 'Policy number is required'}), 400
    reports = Report.query.filter_by(PN=pn).all()
    if not reports:
        return jsonify({'message': 'No reports found for the given policy number'}), 404
    return jsonify([{
        'SN': report.SN,
        'LC': report.LC,
        'Insured': report.Insured,
        'NIPID': report.NIPID,
        'ON': report.ON,
        'IDNIPID': report.IDNIPID,
        'MPN': report.MPN,
        'PN': report.PN,
        'RT': report.RT,
        'DOC': report.DOC,
        'TOC': report.TOC,
        'LOC': report.LOC,
        'DOD': report.DOD,
        'AT': report.AT,
        'AC': report.AC,
        'SDA': report.SDA,
        'WV': report.WV,
        'LD': report.LD,
        'TOL': report.TOL,
        'CSS': report.CSS,
        'CS': report.CS,
        'RN': report.RN,
        'PA': report.PA,
        'AMT': report.AMT,
        'TPMT': report.TPMT,
        'TPP': report.TPP,
        'Allowance': report.Allowance,
        'Disability': report.Disability,
        'Payoutdate': report.Payoutdate,
        'SFV': report.SFV,
        'Remarks': report.Remarks,
        'DRPA': report.DRPA
    } for report in reports])

@app.route('/reports/search_by_rn', methods=['POST'])
def search_reports_by_rn():
        data = request.get_json()
        rn = data.get('RN')
        if not rn:
            return jsonify({'message': 'Report number is required'}), 400
        reports = Report.query.filter_by(RN=rn).all()
        if not reports:
            return jsonify({'message': 'No reports found for the given report number'}), 404
        return jsonify([{
            'SN': report.SN,
            'LC': report.LC,
            'Insured': report.Insured,
            'NIPID': report.NIPID,
            'ON': report.ON,
            'IDNIPID': report.IDNIPID,
            'MPN': report.MPN,
            'PN': report.PN,
            'RT': report.RT,
            'DOC': report.DOC,
            'TOC': report.TOC,
            'LOC': report.LOC,
            'DOD': report.DOD,
            'AT': report.AT,
            'AC': report.AC,
            'SDA': report.SDA,
            'WV': report.WV,
            'LD': report.LD,
            'TOL': report.TOL,
            'CSS': report.CSS,
            'CS': report.CS,
            'RN': report.RN,
            'PA': report.PA,
            'AMT': report.AMT,
            'TPMT': report.TPMT,
            'TPP': report.TPP,
            'Allowance': report.Allowance,
            'Disability': report.Disability,
            'Payoutdate': report.Payoutdate,
            'SFV': report.SFV,
            'Remarks': report.Remarks,
            'DRPA': report.DRPA
        } for report in reports])


if __name__ == '__main__':
    app.run(debug=True)
