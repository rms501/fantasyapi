from yahoo_oauth import OAuth2

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
		return self._handleResponse(self._session.get('https://fantasysports.yahooapis.com/fantasy/v2/game/' + str(game_key), params=self._params))

	#valid game code values: nfl, mlb, etc.
	def fetchGames(self, game_codes, seasons=None):
		return self._handleResponse(
			self._session.get(
				'https://fantasysports.yahooapis.com/fantasy/v2/games;game_codes=' + self._convertCollectionToString(game_codes) + (self._convertSubqueryString(';seasons=', seasons) if resources else ''),
				params=self._params
			)
		)

	#league key format: <game_code or game_id>.l.<league_id>
	#valid resource values: settings, standings, scoreboard
	def fetchLeague(self, league_key, resources=None):
		return self._handleResponse(
			self._session.get(
				'https://fantasysports.yahooapis.com/fantasy/v2/league/' + str(league_key) + (self._convertSubqueryString('/', resources) if resources else ''),
				params=self._params
			)
		)

	#league key format: <game_code or game_id>.l.<league_id>
	#valid resource values: settings, standings, scoreboard
	def fetchLeagues(self, league_keys, resources=None):
		return self._handleResponse(
			self._session.get(
				'https://fantasysports.yahooapis.com/fantasy/v2/leagues;league_keys=' + self._convertCollectionToString(league_keys) + (self._convertSubqueryString(';out=', resources) if resources else ''),
				params=self._params
			)
		)

	#team key format: <game_code or game_id>.l.<league_id>.t.<team_id>
	#valid resource values: matchups (i.e. matchups;weeks=1,5) and stats (i.e. stats;type=season or stats;type=date;date=2011-07-06)
	def fetchTeam(self, team_key, resources=None):
		return self._handleResponse(
			self._session.get(
				'https://fantasysports.yahooapis.com/fantasy/v2/team/' + str(team_key) + (self._convertSubqueryString(';out=', resources) if resources else ''),
				params=self._params
			)
		)

	def fetchTeams(self, team_keys, resources=None):
		return self._handleResponse(
			self._session.get(
				'https://fantasysports.yahooapis.com/fantasy/v2/teams;team_keys=' + self._convertCollectionToString(team_keys) + (self._convertSubqueryString(';out=', resources) if resources else ''),
				params=self._params
			)
		)

	#team key format: <game_code or game_id>.l.<league_id>.t.<team_id>
	#valid date value format: YYYY-MM-DD
	def fetchRoster(self, team_key, week=None, date=None):
		if (week and date):
			raise ValueError('fetchRoster method cannot take a week and date input.')

		return self._handleResponse(
			self._session.get(
				'https://fantasysports.yahooapis.com/fantasy/v2/team/' + str(team_key) + '/roster' + (self._convertSubqueryString(';week=', week) if week else '') + (self._convertSubqueryString(';date=', date) if date else ''),
				params=self._params
			)
		)

	def _convertSubqueryString(self, delimiter, filters):
		return delimiter + self._convertCollectionToString(filters)

	def _convertCollectionToString(self, collection):
		string = ""
		for elem in collection:
			if collection.index(elem) == len(collection)-1:
				string += str(elem)
				break
			string += str(elem) + ','
		return string

	def _handleResponse(self, response):
		content = json.loads(response.content.decode('utf-8').replace('\n', ''))
		response.close()
		return content
