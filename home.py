from flask import Flask,render_template,request
import sqlite3

app=Flask(__name__)

@app.route('/fun1')
def fun1():
    return 'hello world'



@app.route('/',methods=['POST','GET'])
def fun2():
    con=sqlite3.connect('create.db')
    try:
        con.execute('create table std(name,place)')
    except:
        print('table already exits')
    if request.method=='POST':
        name=request.form['name']
        place=request.form['place']
        print(name,place)
        con.execute('insert into std(name,place)values(?,?)',(name,place))
        con.commit()

        

    a=20
    return render_template('index.html',data=a)

app.run()