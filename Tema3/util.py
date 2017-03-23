import sys

class ListStream:
	def __init__(self):
		self.data = []
	def write(self, s):
		#print(s)
		self.data.append(s)

