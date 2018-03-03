import datetime
class Member:
	def __init__(self, name, age):
		self.id = id
		self.name = name
		self.age = age
		self.posts = []

	def __str__(self):
		return f"Name: {self.name}, Age: {self.age}"

class Post:
	def __init__(self, title, body, member_id=0):
		self.id = id
		self.title = title
		self.body = body
		self.member_id = member_id
		self.creation_date = datetime.datetime.now()
		
	def __str__(self):
		return f"Title: {self.title}, Body: {self.body}, at: {self.creation_date}"

