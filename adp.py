import os
import pymysql
import config
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

# SQL script to create the Users table in MySQL
    CREATE TABLE Users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(80) NOT NULL,
        age INT
    );

     CREATE TABLE Report (
        SN INT AUTO_INCREMENT PRIMARY KEY,
        LC VARCHAR(80),
        Insured VARCHAR(80),
        NIPID VARCHAR(80),
        ON VARCHAR(80),
        IDNIPID VARCHAR(80),
        MPN VARCHAR(80),
        PN VARCHAR(80),
        RT VARCHAR(80),
        DOC VARCHAR(80),
        TOC VARCHAR(80),
        LOC VARCHAR(2000),
        DOD VARCHAR(2000),
        AT VARCHAR(80),
        AC VARCHAR(80),
        SDA VARCHAR(80),
        WV VARCHAR(80),
        LD VARCHAR(80),
        TOL VARCHAR(80),
        CSS VARCHAR(80),
        CS VARCHAR(80),
        RN VARCHAR(80),
        PA VARCHAR(80),
        AMT VARCHAR(80),
        TPMT VARCHAR(80),
        TPP VARCHAR(80),
        Allowance VARCHAR(80),
        Disability VARCHAR(80),
        Payoutdate VARCHAR(80),
        SFV VARCHAR(80),
        Remarks VARCHAR(2000),
        DRPA VARCHAR(80)
    );

    CREATE TABLE Clients (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(80) NOT NULL,
        mobile VARCHAR(80) NOT NULL,
        descript VARCHAR(80) NOT NULL,
        idno VARCHAR(80) NOT NULL
    );
主机:sh-cynosdbmysql-grp-432jkmc0.sql.tencentcdb.com 端口:20498
"""
from flask_sqlalchemy import SQLAlchemy

pymysql.install_as_MySQLdb()

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] =  f'mysql://{config.DB_USERNAME}:{config.DB_PASSWORD}@sh-cynosdbmysql-grp-432jkmc0.sql.tencentcdb.com:20498/adp_pa'
db = SQLAlchemy(application)


# 定义数据模型
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

事件类型（轻微/一般/重大） - AT
骑手姓名 -  NIPID 
骑手身份证号码 - IDNIPID
骑手联系方式（手机号码）- MPN
骑手隶属站点 - PN
入职时间 - OOC
事发时间 - TOC
事发地点（省市区具体道路位置）-LOC
事发经过描述-DOD
是否是交通事故，如是：是否报警 -AT
报警后是否有现场责任认定结果或责任认定结果-LD
骑手本人是否受伤？目前伤情（诊断结果）-AMT
是否涉及第三方受伤？目前伤情（诊断结果）-TPMT
是否涉及第三方财损，目前大致财损情况-TPP

incident_data = {
    "AT": "一般",
    "NIPID": "张三",
    "IDNIPID": "310111111111111111",
    "MPN": "186213333333",
    "PN": "上海黄埔",
    "OOC": "2000-01",
    "TOC": "2024.10.10 10:10",
    "LOC": "上海市嘉定区andrew路",
    "DOD": "骑手张三在上海市嘉定区andrew路上骑车时，被一辆小汽车撞倒",
    "AT2": "属于交通事故，已报警",
    "LD": "报警后交警到达现场，认定小汽车承担50%责任，骑手承担50%责任",
    "AMT": "骑手受伤，手臂骨折",
    "TPMT": "无第三方手上",
    "TPP": "小汽车剐蹭，一个漆面300元"
}
"""



@application.route('/')
def welcome():
        return "Welcome to Nuts!"


   
# 创建数据库表（如果不存在）
with application.app_context():
    db.create_all()


# API 路由，返回所有用户
@application.route('/users', methods=['GET'])
def get_users():
    users = Users.query.all()
    return jsonify([{'id': user.id, 'name': user.name,'age':user.age} for user in users])

@application.route('/clients', methods=['GET'])
def get_clients():
    clients = Clients.query.all()
    return jsonify([{'idno': client.idno, 'name': client.name,'mobile':client.mobile,'descript':client.descript} for client in clients])

@application.route('/clients/<mobile>', methods=['GET'])
def search_clients_by_mobile(mobile):
    client = Clients.query.filter_by(mobile=mobile).first()
    if client:
        return jsonify({'id': client.id, 'name': client.name, 'mobile': client.mobile, 'descript': client.descript})
    else:
        return jsonify({'message': 'Client not found'})

@application.route('/clients', methods=['POST'])
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

@application.route('/reports', methods=['POST'])
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

@application.route('/reports', methods=['GET'])
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


@application.route('/reports/search_by_mobile', methods=['POST'])
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

@application.route('/reports/search_by_pn', methods=['POST'])
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

@application.route('/reports/search_by_rn', methods=['POST'])
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



@application.route('/reports_page', methods=['GET'])
def reports_page():
    reports = Report.query.all()
    reports_list = [{
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
    } for report in reports]

    html = '''
    <html>
    <head>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 20px;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin-bottom: 20px;
                font-size: 12px;
            }
            th, td {
                border: 1px solid #ddd;
                padding: 4px;
                text-align: left;
            }
            th {
                background-color: #f2f2f2;
                color: #333;
            }
            tr:nth-child(even) {
                background-color: #f9f9f9;
            }
            tr:hover {
                background-color: #f1f1f1;
            }
            h1 {
                color: #333;
            }
            .table-container {
                max-height: 1000px;
                overflow-y: auto;
                border: 1px solid #ddd;
            }
        </style>
    </head>
    <body>
        <h1>Reports</h1>
        <div class="table-container">
            <table>
                <tr>
                    <th>SN</th>
                    <th>LC</th>
                    <th>Insured</th>
                    <th>NIPID</th>
                    <th>ON</th>
                    <th>IDNIPID</th>
                    <th>MPN</th>
                    <th>PN</th>
                    <th>RT</th>
                    <th>DOC</th>
                    <th>TOC</th>
                    <th>LOC</th>
                    <th>DOD</th>
                    <th>AT</th>
                    <th>AC</th>
                    <th>SDA</th>
                    <th>WV</th>
                    <th>LD</th>
                    <th>TOL</th>
                    <th>CSS</th>
                    <th>CS</th>
                    <th>RN</th>
                    <th>PA</th>
                    <th>AMT</th>
                    <th>TPMT</th>
                    <th>TPP</th>
                    <th>Allowance</th>
                    <th>Disability</th>
                    <th>Payoutdate</th>
                    <th>SFV</th>
                    <th>Remarks</th>
                    <th>DRPA</th>
                </tr>
    '''

    for report in reports_list:
        html += '<tr>'
        for key, value in report.items():
            html += f'<td>{value}</td>'
        html += '</tr>'

    html += '''
            </table>
        </div>
    </body>
    </html>
    '''

    return html


if __name__ == '__main__':
    application.run(debug=True)
