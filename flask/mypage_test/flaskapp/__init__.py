from flask import Flask, render_template,request,url_for, redirect
import pymysql,json

app=Flask(__name__)
app.debug=True
@app.route("/tutor_mypage",methods=["POST","GET"])
#_내 강의목록
def tutor_lecture():
    db = pymysql.connect(host='127.0.0.1',
        port=3306,
        user='admin',
        passwd='0507',
        db='attendance',
        charset='utf8')
    cursor=db.cursor()

    query = "SELECT CLASS_INFO.CLASS_NAME FROM CLASS_INFO WHERE TUTOR_INFO.TUTOR_ID=CLASS_INFO.TUTOR_ID;"

    cursor.execute(query)
    data=(cursor.fetchall())

    query="SELECT TUTEE_INFO.NAME,ATTENDANCE.PASS_TIME,ATTENDANCE.STATUS FROM TUTEE_INFO,ATTENDANCE WHERE ATTENDANCE.MAPPING_ID = TUTEE_CLASS_MAPPING.MAPPING_ID AND TUTEE_CLASS_MAPPING.TUTEE_ID=TUTEE_INFO.TUTEE_ID AND CLASS_INFO.CLASS_ID=TUTEE_CLASS_MAPPING.CLASS_ID AND CLASS_INFO.CLASS_NAME='linux'"

    cursor.execute(query)
    data2=(cursor.fetchall())

    cursor.close()
    db.close()

    datalist=[]       #튜터마이페이지>강의리스트
    for row in data:
        if row :  #튜터 마페, 강의목록
            dic={'CLASS_INFO.CLASS_NAME':row[0:]}
            datalist.append(dic)

    for row in data2:
        if row : 
            dic={'TUTEE_INFO.NAME':row[0:],'ATTENDANCE.PASS_TIME':row[0:],'ATTENDANCE.STATUS':row[0:]}
            datalist.append(dic)

    return json.dumps(datalist)