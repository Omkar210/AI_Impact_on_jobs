from flask import Flask, render_template, request, redirect
import mysql.connector as mysql

try:
    db = mysql.connect(
      host="127.0.0.1",
      user="root",
      password="1234",
      database="ai_impact",
      auth_plugin='mysql_native_password'
    )
    if db.is_connected():
        print("Successfully connected to the database")
except Exception as e:
    print(f"Error: {e}")

app = Flask(__name__)

cursor = db.cursor()
# READ (View all jobs)
@app.route('/')
def index():
    cursor.execute("SELECT * FROM jobs1")
    data = cursor.fetchall()
    return render_template("index.html", jobs=data)

# CREATE (Add job)
@app.route('/add', methods=['POST'])
def add():
    data = request.form

    cursor.execute("""
        INSERT INTO jobs1 
        (Job_Title, Average_Salary, Years_Experience, Education_Level,
         AI_Exposure_Index, Tech_Growth_Factor, Automation_Probablity_2030, Risk_Category)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """, (
        data['job_title'],
        data['salary'],
        data['experience'],
        data['education'],
        data['ai_index'],
        data['growth'],
        data['automation'],
        data['risk']
    ))

    db.commit()
    return redirect('/')

# DELETE
@app.route('/delete/<string:title>')
def delete(title):
    cursor.execute("DELETE FROM jobs1 WHERE Job_Title=%s", (title,))
    db.commit()
    return redirect('/')

# UPDATE (Edit)
@app.route('/update/<string:title>', methods=['POST'])
def update(title):
    data = request.form

    cursor.execute("""
        UPDATE jobs1 SET 
        Average_Salary=%s,
        Years_Experience=%s,
        Education_Level=%s,
        AI_Exposure_Index=%s,
        Tech_Growth_Factor=%s,
        Automation_Probablity_2030=%s,
        Risk_Category=%s
        WHERE Job_Title=%s
    """, (
        data['salary'],
        data['experience'],
        data['education'],
        data['ai_index'],
        data['growth'],
        data['automation'],
        data['risk'],
        title
    ))

    db.commit()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)