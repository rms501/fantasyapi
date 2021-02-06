from fantasyapi.service.clients.yahoo_client import YahooClient
from fantasyapi.model.yahoo.game import Game
from pykson import Pykson

class YahooExtractor():

	def __init__(self):
		self._pykson = Pykson()
	
	def extractGame(self, game_key):
		return self._pykson.from_json(self._unwrapPayload(YahooClient.fetchGame(game_key)).get('game').pop(), Game, accept_unknown=True)

	def extractGames(self, game_codes, seasons=None):
		payload = self._unwrapPayload(YahooClient.fetchGames(game_codes, seasons)).get('games')
		return [self._pykson.from_json(payload.get(i).get('game').pop(), Game, accept_unknown=True) for i in payload.keys() if i != 'count']

	def _unwrapPayload(self, object):
		return object.get('fantasy_content')
