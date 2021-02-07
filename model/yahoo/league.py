from pykson import JsonObject, StringField, IntegerField

class League(JsonObject):

	league_key = StringField()
	league_id = StringField()
	name = StringField()
	url = StringField()
	draft_status = StringField()
	num_teams = IntegerField()
	scoring_type = StringField()
	current_week = StringField()
	start_week = StringField()
	start_date = StringField()
	end_week = StringField()
	end_date = StringField()
	is_finished = IntegerField()
	game_code = StringField()
	season = StringField()