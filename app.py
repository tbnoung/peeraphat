#coding=utf-8
from dbConfig import *
from src.user import *
############################################################
# @app.route('/insertuser', methods=['POST'])
# def APIInsertUser():
#     return insertuser()
############################################################






# @app.route('/place_no', methods=['GET'])
# @connect_sql()
# def place_no():
#     sql = "SELECT MAX(id) FROM user"
#     cursor.execute(sql,(username))
#     print(cursor.description)
#     data = cursor.fetchall()
#     columns = [column[0] for column in cursor.description]
#     return jsonify(columns)
@app.route('/testtest', methods=['GET'])
def testtest():
    return 'success'


@app.route('/123', methods=['GET'])
def abc():
    return '123'
# @app.route('/getName21', methods=['POST'])
# @connect_sql()
# def getName21(cursor):
#     try:
#         # data = request.json
#         sql = "SELECT * FROM user"
#         cursor.execute(sql)
#         columns = [column[0] for column in cursor.description]
#         result = cursor.fetchall()
#         jsonResult = toJson(result,columns)
#         return jsonify(result)
#     except Exception as e:
#         current_app.logger.info(e)
# ----------------------insert product---------------------------
@app.route('/inserproduct', methods=['POST'])
@connect_sql()
def inserproduct(cursor):
    try:
        getData = request.json
        idbill = getData['idbill']
        sql = """SELECT * from bill where idbill=%s """
        cursor.execute(sql, (idbill))
        columns = [column[0] for column in cursor.description]
        result = cursor.fetchall()
        jsonResult = toJson(result, columns)
        print(len(jsonResult))
        if len(jsonResult) == 0:
            return {"message": "fail"}
        else:
            # data = {"data": jsonResult, "message": "success"}
            sql = "SELECT * FROM product"
            cursor.execute(sql)
            columns = [column[0] for column in cursor.description]
            result = cursor.fetchall()
            jsonResult = toJson(result, columns)
            # getData = request.json
            idproduct = 'AAA' + str(len(jsonResult) + 1)
            time = getData['time']
            brand = getData['brand']
            generation = getData['generation']
            firstname = getData['firstname']
            lastname = getData['lastname']
            mail = getData['mail']
            tel = getData['tel']
            reasoning = getData['reasoning']
            sql = """INSERT INTO product(idproduct, time, brand,generation,firstname,lastname,mail,tel,reasoning)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql, (idproduct, time, brand, generation, firstname, lastname, mail,tel,reasoning))
            return {'message': 'success'}
    except Exception as e:
        return jsonify(e)
# ----------------------search bill---------------------------
@app.route('/searchbill', methods=['POST'])
@connect_sql()
def searchbill(cursor):
    try:
        getData = request.json
        idbill = getData['idbill']
        sql = """SELECT * from bill where idbill=%s """
        cursor.execute(sql, (idbill))
        columns = [column[0] for column in cursor.description]
        result = cursor.fetchall()
        jsonResult = toJson(result, columns)
        print(len(jsonResult))
        if len(jsonResult) == 0:
            data = {"message": "fail"}
        else:
            data = {"data": jsonResult, "message": "success"}
        return jsonify(data)
        # return jsonify(jsonResult)
        # return jsonify({"data":jsonResult,"Detail":jsonResult,"message":"success"})
    except Exception as e:
        return jsonify(e)
# ----------------------insert bill---------------------------
@app.route('/insertbill', methods=['POST'])
@connect_sql()
def insertbill(cursor):
    try:
        sql = "SELECT * FROM bill"
        cursor.execute(sql)
        columns = [column[0] for column in cursor.description]
        result = cursor.fetchall()
        jsonResult = toJson(result, columns)
        getData = request.json
        idbill = 'bill' + str(len(jsonResult) + 1)
        time = getData['time']
        brand = getData['brand']
        generation = getData['generation']
        sql = """INSERT INTO bill(idbill, time, brand,generation)VALUES (%s,%s,%s,%s)"""
        cursor.execute(sql, (idbill, time, brand,generation))
        return {'message': 'success'}
    except Exception as e:
        return jsonify(e)
# -------------------------------get getorder--------------------------------
@app.route('/getbill', methods=['POST'])
@connect_sql()
def getbill(cursor):
    try:
        # data = request.json
        sql = "SELECT * FROM bill"
        cursor.execute(sql)
        columns = [column[0] for column in cursor.description]
        result = cursor.fetchall()
        jsonResult = toJson(result, columns)
        print('bill' + str(len(jsonResult) + 1))
        return jsonify(jsonResult)
        # return 'success'
    except Exception as e:
        current_app.logger.info(e)
# -------------------------------get getitem--------------------------------
@app.route('/getitem', methods=['POST'])
@connect_sql()
def getitem(cursor):
    try:
        # data = request.json
        sql = "SELECT * FROM product"
        cursor.execute(sql)
        columns = [column[0] for column in cursor.description]
        result = cursor.fetchall()
        jsonResult = toJson(result, columns)
        return jsonify(jsonResult)
        # return 'success'
    except Exception as e:
        current_app.logger.info(e)
# -------------------------------get username--------------------------------
@app.route('/getdata', methods=['POST'])
@connect_sql()
def getName21(cursor):
    try:
        # data = request.json
        sql = "SELECT * FROM username"
        cursor.execute(sql)
        columns = [column[0] for column in cursor.description]
        result = cursor.fetchall()
        jsonResult = toJson(result,columns)
        return jsonify(jsonResult)
        # return 'success'
    except Exception as e:
        current_app.logger.info(e)
# -------------------------------API Login--------------------------------
@app.route('/login', methods=['POST'])
@connect_sql()
def login(cursor):
    try:
        getData = request.json
        username = getData['username']
        password = getData['password']
        sql = """SELECT * from 
        username where username=%s and password=%s"""
        cursor.execute(sql,(username,password))
        columns = [column[0] for column in cursor.description]
        result = cursor.fetchall()
        jsonResult = toJson(result,columns)
        print(len(jsonResult))
        if len(jsonResult) == 0:
            data = {"message":"fail"} 
        else :
            data = {"data":jsonResult,"message":"success"}
        return jsonify(data)
        # return jsonify(jsonResult) 
        # return jsonify({"data":jsonResult,"Detail":jsonResult,"message":"success"})
    except Exception as e:
        return jsonify(e)
# -------------------------------API INSERT INTO TABLE--------------------------------
@app.route('/insertdata', methods=['POST'])
@connect_sql()
def InsertData(cursor):
    try:
        getData = request.json
        username = getData['username']
        password = getData['password']
        nametitle = getData['nametitle']
        firstname = getData['firstname']
        lastname = getData['lastname']
        mail = getData['mail']
        tel = getData['tel']
        sql = """
        INSERT INTO username(username, password, nametitle,firstname,lastname,mail,tel)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """
        cursor.execute(sql, (username, password, nametitle,firstname, lastname, mail, tel))
        return {'message':'success'}
    except Exception as e:
        return jsonify(e)
# #############################################################
# @app.route('/hello/<firstname>/<lastname>', methods=['GET'])
# @connect_sql()
# def hello(cursor, firstname, lastname):
#     sql = "SELECT * FROM test WHERE firstname=%s AND lastname=%s"
#     cursor.execute(sql,(firstname, lastname))
#     print(cursor.description)
#     data = cursor.fetchall()
#     columns = [column[0] for column in cursor.description]
#     result = toJson(data,columns)
#     return jsonify(result)

# @app.route('/getName2', methods=['POST'])
# def getName2():
#     # data = request.json
#     connection = mysql.connect()
#     cursor = connection.cursor()
#     sql = "SELECT * FROM test"
#     cursor.execute(sql)
#     columns = [column[0] for column in cursor.description]
#     result = toJson(cursor.fetchall(),columns)
#     connection.commit()
#     connection.close()
#     return jsonify(result)

# @app.route('/getName', methods=['POST'])
# @connect_sql()
# def getName(cursor):
#     data = request.json
#     sql = "SELECT * FROM test WHERE firstname=%s AND lastname=%s"
#     cursor.execute(sql,(data['firstname'], data['lastname']))
#     columns = [column[0] for column in cursor.description]
#     result = toJson(cursor.fetchall(),columns)
#     return jsonify({ 'res' : result})

# @app.route('/hello2', methods=['GET'])
# def hello2():
#     return jsonify(getData('hello'))

# @connect_sql()
# def getData(c, data):
#     print data
#     c.execute("SELECT * FROM test")
#     columns = [column[0] for column in c.description]
#     result = toJson(c.fetchall(),columns)
#     return result

# @app.route('/insertdata/<firstname>/<lastname>', methods=['GET'])
# @connect_sql()
# def InsertData(cursor,firstname, lastname):
#     sql = """
#     INSERT INTO test(firstname, lastname)
#     VALUES (%s,%s)
#     """
#     cursor.execute(sql, (firstname, lastname))
#     return 'success'

# @app.route('/insertdata2', methods=['POST'])
# @connect_sql()
# def InsertData2(cursor):
#     data = request.json
#     sql = """
#     INSERT INTO test(firstname, lastname)
#     VALUES (%s,%s)
#     """
#     cursor.execute(sql, (data['first'], data['last']))
#     return jsonify({ 'status' : 'success' })

# @app.route('/deletedata/<firstname>/<lastname>', methods=['GET'])
# @connect_sql()
# def deleteData(cursor,firstname, lastname):
#     sql = """
#     delete from test
#     where firstname = %s and lastname = %s
#     """
#     cursor.execute(sql, (firstname, lastname))
#     return 'success'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',threaded=True,port=5000)
