from fantasyapi.service.clients.yahoo_client import YahooClient
from fantasyapi.model.yahoo.game import Game
from fantasyapi.model.yahoo.league import League
from pykson import Pykson

class YahooExtractor():

	def __init__(self):
		self._pykson = Pykson()
	
	def extractGame(self, game_key):
		return self._pykson.from_json(self._unwrapPayload(YahooClient.fetchGame(game_key)).get('game').pop(), Game, accept_unknown=True)

	def extractGames(self, game_codes, seasons=None):
		return self._convertPayloadJsonToObjects(self._unwrapPayload(YahooClient.fetchGames(game_codes, seasons)).get('games'), 'game', Game)

	def extractLeague(self, league_key, resoure=None):
		payload = self._unwrapPayload(YahooClient.fetchLeague(league_key, resoure)).get('league')

		if (resource == 'settings'):
			
			#setting extraction logic here
		else if (resource == 'standings'):
			#standing extraction logic here
		else if (resource == 'scoreboard'):
			#scoreboard extraction logic here
			
		return self._pykson.from_json(self._unwrapPayload(YahooClient.fetchLeague(league_key, resoure)).get('league').pop(), League, accept_unknown=True)

	def extractLeagues(self, league_keys, resources=None):
		payload = self._unwrapPayload(YahooClient.fetchLeagues(league_keys, resources).get('leagues'))
		return self._convertPayloadJsonToObjects(payload, 'league', League)

	def _convertPayloadJsonToObjects(self, payload, wrapper, objectClass):
		return [self._pykson.from_json(payload.get(i).get(wrapper).pop(), objectClass, accept_unknown=True) for i in payload.keys() if i != 'count']		

	def _unwrapPayload(self, object):
		return object.get('fantasy_content')
