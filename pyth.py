from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return f"<h1>Welcome, {username}!</h1>"
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        nationality = request.form['nationality']
        residence = request.form['residence']
        arrival_day = request.form['arrival_day']
        username = request.form['username']
        password = request.form['password']

        # Here you could store data in a database or a file

        return f"""
            <h1>Thanks for signing up, {name}!</h1>
            <p>Nationality: {nationality}</p>
            <p>Residence: {residence}</p>
            <p>Arrival Date: {arrival_day}</p>
            <p>Your username is: {username}</p>
            <a href='/login'>Go to login</a>
        """
    return render_template('signup.html')

@app.route('/north-shewa')
def north_shewa():
    return "<h1>North Shewa Zone Info Coming Soon!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
