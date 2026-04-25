from flask import Flask, request, session, redirect

app = Flask(__name__)
app.secret_key = "supersecretkey"

FLAG = "PSNACET{1111_br0k3n_m3}"

users = {
    "Bala": {"password": "t3at123", "role": "user"},
}

@app.route('/')
def home():
    return '''
    <h2>Login</h2>
    <form method="POST" action="/login">
        Username: <input name="username"><br>
        Password: <input name="password"><br>
        <input type="submit">
    </form>
    '''

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username in users and users[username]["password"] == password:
        session['username'] = username
        return redirect('/dashboard')
    return "Invalid credentials"

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect('/')

    return '''
    <h2>Welcome Bala</h2>
    <p>You are logged in as a normal user.</p>
    <a href="/admin?admin=false">Go to Admin Panel</a>
    <!-- Hint: Try changing something in the URL -->
    '''

@app.route('/admin')
def admin():
    admin_flag = request.args.get('admin')

    if admin_flag == "true":
        return f"<h2>Welcome Admin</h2><p>{FLAG}</p>"
    else:
        return "<h3>Access Denied</h3>"

if __name__ == '__main__':
    app.run(debug=True)
