
class Node():

	def __init__(self, value=None, children=[], parent=None):
		self.value = value
		self.children = children
		self.parent = parent

	def __iter__(self):
		for child in self.children:
			yield child

	def is_root(self):
		return not self.parent

	def has_children(self):
		return len(self.children) > 0

	def add_child(self, value=None, children=[], child=None):
		self.children.append(child if child else Node(value, children, self))