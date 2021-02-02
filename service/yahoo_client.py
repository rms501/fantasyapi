from yahoo_oauth import OAuth2

import json

class YahooClient():

	#league key format: <game_code or game_id>.l.<league_id>
	#team key format: <game_code or game_id>.l.<league_id>.t.<team_id>
	#player key format: <game_code or game_id>.p.<player_id>
	#transaction key format - completed transactions: <game_code or game_id>.l.<league_id>.tr.<transaction_id>
	#transaction key format - waiver claims: <game_code or game_id>.l.<league_id>.w.c.<claim_id>
	#transaction key format - pending trades: <game_code or game_id>.l.<league_id>.pt.<pending_trade_id>

	_oauth = OAuth2(None, None, from_file='/home/rob/apps/fantasyapi/oauth2.json')
	_params = {
		'format': 'json'
	}

	def __init__(self):
		raise RuntimeError('Cannot instantiate YahooClient class.')

	@classmethod
	def fetchGame(cls, game_key):
		return cls._handleResponse(cls._get('https://fantasysports.yahooapis.com/fantasy/v2/game/' + str(game_key), params=cls._params))

	#valid game code values: nfl, mlb, etc.
	@classmethod
	def fetchGames(cls, game_codes, seasons=None):
		return cls._handleResponse(
			cls._get(
				'https://fantasysports.yahooapis.com/fantasy/v2/games;game_codes=' + cls._convertCollectionToString(game_codes) + (cls._convertSubqueryString(';seasons=', seasons) if resources else ''),
				params=cls._params
			)
		)

	#valid resource values: settings, standings, scoreboard
	@classmethod
	def fetchLeague(cls, league_key, resources=None):
		return cls._handleResponse(
			cls._get(
				'https://fantasysports.yahooapis.com/fantasy/v2/league/' + str(league_key) + (cls._convertSubqueryString('/', resources) if resources else ''),
				params=cls._params
			)
		)

	#valid filter values: position, status, search, sort, sort_type, sort_season, sort_date, sort_week, start, and count)
	@classmethod
	def fetchLeaguePlayers(cls, league_key, filter=None):
		return cls._handleResponse(
			cls._get(
				'https://fantasysports.yahooapis.com/fantasy/v2/league/' + str(league_key) + '/players;' + filter,
				params=cls._params
			)
		)

	#valid resource values: settings, standings, scoreboard
	@classmethod
	def fetchLeagues(cls, league_keys, resources=None):
		return cls._handleResponse(
			cls._get(
				'https://fantasysports.yahooapis.com/fantasy/v2/leagues;league_keys=' + cls._convertCollectionToString(league_keys) + (cls._convertSubqueryString(';out=', resources) if resources else ''),
				params=cls._params
			)
		)

	#valid resource values: matchups (i.e. matchups;weeks=1,5) and stats (i.e. stats;type=season or stats;type=date;date=2011-07-06)
	@classmethod
	def fetchTeam(cls, team_key, resources=None):
		return cls._handleResponse(
			cls._get(
				'https://fantasysports.yahooapis.com/fantasy/v2/team/' + str(team_key) + (cls._convertSubqueryString(';out=', resources) if resources else ''),
				params=cls._params
			)
		)

	#valid resource values: matchups (i.e. matchups;weeks=1,5) and stats (i.e. stats;type=season or stats;type=date;date=2011-07-06)
	@classmethod
	def fetchTeams(cls, team_keys, resources=None):
		return cls._handleResponse(
			cls._get(
				'https://fantasysports.yahooapis.com/fantasy/v2/teams;team_keys=' + cls._convertCollectionToString(team_keys) + (cls._convertSubqueryString(';out=', resources) if resources else ''),
				params=cls._params
			)
		)

	#valid date value format: YYYY-MM-DD
	@classmethod
	def fetchRoster(cls, team_key, week=None, date=None):
		if (week and date):
			raise ValueError('fetchRoster method cannot take a week and date input.')

		return cls._handleResponse(
			cls._get(
				'https://fantasysports.yahooapis.com/fantasy/v2/team/' + str(team_key) + '/roster' + (cls._convertSubqueryString(';week=', week) if week else '') + (cls._convertSubqueryString(';date=', date) if date else ''),
				params=cls._params
			)
		)

	#valid resources values: stats
	@classmethod
	def fetchPlayer(cls, player_key, resources=None):
		return cls._handleResponse(
			cls._get(
				'https://fantasysports.yahooapis.com/fantasy/v2/player/' + str(player_key) + (cls._convertSubqueryString(';out=', resources) if resources else ''),
				params=cls._params
			)
		)

	#valid resources values: stats
	@classmethod
	def fetchPlayers(cls, player_keys, resources=None):
		return cls._handleResponse(
			cls._get(
				'https://fantasysports.yahooapis.com/fantasy/v2/players;player_keys=' + cls._convertCollectionToString(player_keys) + (cls._convertSubqueryString(';out=', resources) if resources else ''),
				params=cls._params
			)
		)

	@classmethod
	def fetchTransaction(cls, transaction_key):
		return cls._handleResponse(
			cls._get(
				'https://fantasysports.yahooapis.com/fantasy/v2/transaction/' + str(transaction_key),
				params=cls._params
			)
		)

	@classmethod
	def fetchTransactions(cls, transaction_keys):
		return cls._handleResponse(
			cls._get(
				'https://fantasysports.yahooapis.com/fantasy/v2/transactions;transaction_keys=' + cls._convertCollectionToString(transaction_keys),
				params=cls._params
			)
		)

	@classmethod
	def fetchUsers(cls, use_login):
		return cls._handleResponse(
			cls._get(
				'https://fantasysports.yahooapis.com/fantasy/v2/users;use_login=' + str(use_login),
				params=cls._params
			)
		)

	@classmethod
	def _convertSubqueryString(cls, delimiter, filters):
		return delimiter + cls._convertCollectionToString(filters)

	@classmethod
	def _convertCollectionToString(cls, collection):
		string = ""
		for elem in collection:
			if collection.index(elem) == len(collection)-1:
				string += str(elem)
				break
			string += str(elem) + ','
		return string

	@classmethod
	def _handleResponse(cls, response):
		content = json.loads(response.content.decode('utf-8').replace('\n', ''))
		response.close()
		return content

	@classmethod
	def _get(cls, url, params):
		if not cls._oauth.token_is_valid:
			cls._oauth.refresh_access_token()

		return cls._oauth.session.get(url, params=params)
