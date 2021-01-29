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

	def fetchGamesByYears(self, years):
		return self.handleResponse(
			self._session.get('https://fantasysports.yahooapis.com/fantasy/v2/games;game_codes=nfl,mlb;seasons=' + self.convertYearsList(years), params=self._params)
		)

	def fetchLeague(self, game_id, league_id):
		return self.handleResponse(
			self._session.get('https://fantasysports.yahooapis.com/fantasy/v2/league/' + str(game_id) + '.l.' + str(league_id), params=self._params)
		)

	def fetchLeagueSettings(self, game_id, league_id):
		return self.handleResponse(
			self._session.get('https://fantasysports.yahooapis.com/fantasy/v2/league/' + str(game_id) + '.l.' + str(league_id) + '/settings', params=self._params)
		)

	def fetchLeagueStandings(self, game_id, league_id):
		return self.handleResponse(
			self._session.get('https://fantasysports.yahooapis.com/fantasy/v2/league/' + str(game_id) + '.l.' + str(league_id) + '/standings', params=self._params)
		)

	def fetchLeagueScoreboard(self, game_id, league_id):
		return self.handleResponse(
			self._session.get('https://fantasysports.yahooapis.com/fantasy/v2/league/' + str(game_id) + '.l.' + str(league_id) + '/scoreboard', params=self._params)
		)

	def convertListToString(self, years):
		string = ""
		for  in years:
			if years.index(year) == len(years)-1:
				yearsString += str(year)
				break
			yearsString += str(year) + ','
		return yearsString

	def handleResponse(self, response):
		content = response.content.decode('utf-8')
		response.close()
		return content
