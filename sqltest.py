# main.py

from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://sql6493319:HBs7D4M8eQ@sql6.freesqldatabase.com:3306/sql6493319"

db.init_app(app)

@app.route('/')
def index():

    sql_cmd = """
        select *
        from sql6493319.users;
        """

    query_data = db.engine.execute(sql_cmd)
    print(query_data)
    return 'ok'


if __name__ == "__main__":
    app.run()