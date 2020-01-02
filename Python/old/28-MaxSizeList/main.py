class MaxSizeList():
	def __init__(self, max_size):
		self.max_size = max_size
		self.obj_list = []

	def push(self, obj):
		if not self.obj_list:
			self.obj_list = []

		if len(self.obj_list) == self.max_size:
			self.obj_list = self.obj_list[1:]
		self.obj_list.append(obj)

	def get_list(self):
		return self.obj_list