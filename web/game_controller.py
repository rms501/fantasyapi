from flask import Blueprint
from fantasyapi.service.yahoo_client import YahooClient

game_controller = Blueprint('game_controller', __name__)

@game_controller.route('/testGameId')
def test():
	return 'test' #str(type(YahooClient().fetchCurrentGameId('nfl')))