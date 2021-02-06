from pykson import JsonObject, StringField

class Game(JsonObject):

	game_key = StringField()
	game_id	= StringField()
	name = StringField()
	code = StringField()
	url = StringField()
	season = StringField()