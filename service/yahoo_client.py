from yahoo_oauth import OAuth2
from fantasyapi.model.UrlEnum import UrlEnum

import ast

import json

class YahooClient():

	#todo: make static

	_session = None
	_params = {
		'format': 'json'
	}

	def __init__(self):
		self._session = OAuth2(None, None, from_file='/home/rob/apps/fantasyapi/oauth2.json').session

	def fetchGame(self, game_key):
		return self.handleResponse(self._session.get('https://fantasysports.yahooapis.com/fantasy/v2/game/' + str(game_key), params=self._params))

	#valid game code values: nfl, mlb, etc.
	def fetchGames(self, game_codes, seasons=None):
		return self.handleResponse(
			self._session.get(
				'https://fantasysports.yahooapis.com/fantasy/v2/games;game_codes=' + self.convertCollectionToString(game_codes) + (self.convertSubqueryString(';seasons=', seasons) if resources else ''),
				params=self._params
			)
		)

	#league key format: <game_code or game_id>.l.<league_id>
	#valid resource values: settings, standings, scoreboard
	def fetchLeague(self, league_key, resources=None):
		return self.handleResponse(
			self._session.get(
				'https://fantasysports.yahooapis.com/fantasy/v2/league/' + str(league_key) + (self.convertSubqueryString('/', resources) if resources else ''),
				params=self._params
			)
		)

	#league key format: <game_code or game_id>.l.<league_id>
	#valid resource values: settings, standings, scoreboard
	def fetchLeagues(self, league_keys, resources=None):
		return self.handleResponse(
			self._session.get(
				'https://fantasysports.yahooapis.com/fantasy/v2/leagues;league_keys=' + self.convertCollectionToString(league_keys) + (self.convertSubqueryString(';out=', resources) if resources else ''),
				params=self._params
			)
		)

	#team key format: <game_code or game_id>.l.<league_id>.t.<team_id>
	#valid resource values: matchups (i.e. matchups;weeks=1,5) and stats (i.e. stats;type=season or stats;type=date;date=2011-07-06)
	def fetchTeam(self, team_key, resources=None):
		return self.handleResponse(
			self._session.get(
				'https://fantasysports.yahooapis.com/fantasy/v2/team/' + str(team_key) + (self.convertSubqueryString(';out=', resources) if resources else ''),
				params=self._params
			)
		)

	def convertSubqueryString(self, delimiter, resources):
		return delimiter + self.convertCollectionToString(resources)

	def convertCollectionToString(self, collection):
		string = ""
		for elem in collection:
			if collection.index(elem) == len(collection)-1:
				string += str(elem)
				break
			string += str(elem) + ','
		return string

	def handleResponse(self, response):
		content = response.content.decode('utf-8')
		response.close()
		return content
