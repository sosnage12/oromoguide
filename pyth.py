from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Connect to your MySQL database
#db = mysql.connector.connect(
 #   host="localhost",
  #  user="root",                      # 🔁 Your MySQL username
   # password="sosna#gemechu1",       # 🔁 Your MySQL password
    #database="argadhu"               # 🔁 Your database name
#)
#cursor = db.cursor()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user_type = request.form['user_type']

        if user_type == 'tourist':
            name = request.form['name']
            age = request.form['age']
            nationality = request.form['nationality']
            residence = request.form['residence']
            arrival_day = request.form['arrival_day']
            username = request.form['username']
            password = request.form['password']

            try:
                query = """
                    INSERT INTO tourist (name, age, nationality, residence, arrival_day, username, password)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                values = (name, age, nationality, residence, arrival_day, username, password)
                cursor.execute(query, values)
                db.commit()

                return f"""
                <h2>Tourist Registered: {name}</h2>
                <p>Username: {username}<br>Nationality: {nationality}<br>Residence: {residence}<br>Arrival: {arrival_day}</p>
                <a href="/">Back to Home</a>
                """
            except Exception as e:
                return f"<h3>Error registering tourist: {str(e)}</h3>"

        elif user_type == 'tourguide':
            fullname = request.form['fullname']
            email = request.form['email']
            phone = request.form['phone']
            zone = request.form['zone']
            language = request.form['language']
            experience = request.form['experience']

            try:
                query = """
                    INSERT INTO tourguide (fullname, email, phone, zone, language, experience)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """
                values = (fullname, email, phone, zone, language, experience)
                cursor.execute(query, values)
                db.commit()

                return f"""
                <h2>Tour Guide Registered: {fullname}</h2>
                <p>Email: {email}<br>Phone: {phone}<br>Zone: {zone}<br>Language: {language}<br>Experience: {experience} years</p>
                <a href="/">Back to Home</a>
                """
            except Exception as e:
                return f"<h3>Error registering tour guide: {str(e)}</h3>"

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # You can add DB validation here
        return f"<h1>Welcome, {username}!</h1>"
    return render_template('login.html')

@app.route('/north-shewa')
def north_shewa():
    return "<h1>North Shewa Zone Info Coming Soon!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
