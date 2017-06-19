from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<DOCTYPE! html>
<html>
<head>
    <style>
        form, textarea {
            width: 540px;
        }
        form {
            background: #eee;
            padding: 20px;
            margin: 0 auto;
            font: 16px sans-serif;
            border-radius: 10px;
        }
        textarea {
            margin: 10px 0;
            height: 120px;
        }
    </style>
</head>
<body>
    <form method='POST'>
        <label>Rotate by:
            <input type='text' name='rot' value=0>
        </label>
        <textarea name='text'></textarea>
        <input type='submit' value='Submit Query'> 
    </form>
</body>
</html>
"""

@app.route("/")
def index():
    return form

app.run()