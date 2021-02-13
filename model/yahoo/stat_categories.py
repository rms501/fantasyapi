from pykson import JsonObject, ObjectListField

class StatCategories(JsonObject):

	stats = ObjectListField(StatCategoriesStat)