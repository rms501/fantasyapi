from pykson import IntegerField, JsonObject, StringField

class Position(JsonObject):

	position = StringField()
	position_type = StringField()
	count = IntegerField()