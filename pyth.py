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
        email = request.form['email']
        password = request.form['password']
        return f"<h1>Thanks for signing up, {email}!</h1>"
    return render_template('signup.html')

@app.route('/north-shewa')
def north_shewa():
    return "<h1>North Shewa Zone Info Coming Soon!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
