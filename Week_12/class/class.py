# Structure:

# - ROOT FOLDER/
# --- wsgi.py
# --- APP_FOLDER/
# ------ __init__.py
# ------ views.py (routes.py)
# ------ templates/
# --------- base.html

import os

app_name = input("Name of the app: ")
app_path = input("Path to the app (default is current dir): ")

if not app_path:
    app_path = os.getcwd() # cwd --> current working directory

os.chdir(app_path)

with open("wsgi.py", 'w') as f:
    f.write(f"""
from {app_name} import app
if __name__ == "__main__":
    app.run(debug=True)
""")

os.mkdir(app_name)
os.mkdir(os.path.join(app_name, "templates")) # So i dont have to do f"{app_name}/templates"

with open(os.path.join(app_name, "__init__.py"), 'w') as f:
    f.write(f"""
import flask
app = flask.Flask(__name__)
from . import views
""")

with open(os.path.join(app_name, "views.py"), 'w') as f:
    f.write(f"""
from . import app
@app.route("/")
def index():
    return "Hello world !"
            """)


with open(os.path.join(app_name, "templates/base.html"), 'w') as f:
    f.write(f"""
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>{{ title }}</title>
  <meta name="author" content="">
  <meta name="description" content="">
  <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
  <p>Hello, world!</p>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
</body>
</html>
            """)