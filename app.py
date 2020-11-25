from flask import Flask
from main.routes import main
from plan.routes import plan

app = Flask(__name__)


app.register_blueprint(main)
app.register_blueprint(plan)


if __name__ == '__main__':
    app.run(debug=True)
