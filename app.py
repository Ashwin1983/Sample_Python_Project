# app.py
from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Simple Login</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .login-container {
            background: white;
            padding: 30px;
            border-radius: 10px;
            width: 300px;
            box-shadow: 0px 0px 10px rgba(0,0,0,0.2);
        }

        h2 {
            text-align: center;
        }

        input[type=text],
        input[type=password] {
            width: 100%;
            padding: 10px;
            margin: 8px 0;
        }

        button {
            width: 100%;
            padding: 10px;
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
        }

        .message {
            text-align: center;
            margin-top: 10px;
            color: blue;
        }
    </style>
</head>
<body>

<div class="login-container">
    <h2>Login</h2>

    <form method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>

        <button type="submit">Login</button>
    </form>

    {% if message %}
        <div class="message">{{ message }}</div>
    {% endif %}
</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    message = ""

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Simple hardcoded login validation
        if username == "admin" and password == "admin123":
            message = "Login Successful!"
        else:
            message = "Invalid Username or Password"

    return render_template_string(HTML_PAGE, message=message)

if __name__ == "__main__":
    app.run(debug=True)