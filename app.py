from flask import Flask
from fantasyapi.web.game_controller import game_controller
from fantasyapi.web.hydration_controller import hydration_controller

app = Flask(__name__)
app.register_blueprint(game_controller)
app.register_blueprint(hydration_controller)
