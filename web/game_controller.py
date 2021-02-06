from flask import Blueprint

game_controller = Blueprint('game_controller', __name__)

@game_controller.route('/testGameId')
def test():
	return 'test'
	