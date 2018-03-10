import datetime
class Member:
	def __init__(self, name, age):
		self.id = 0
		self.name = name
		self.age = age
		self.posts = []

	def __str__(self):
		return f"Name: {self.name}, Age: {self.age}"

	def __dict__(self):
		return{
			"id": self.id,
			"name": self.name,
			"age": self.age,
			"posts": self.posts
		}

class Post:
	def __init__(self, title, body, member_id=0):
		self.id = 0
		self.title = title
		self.body = body
		self.member_id = member_id
		self.creation_date = datetime.datetime.now()
		
	def __str__(self):
		return f"Title: {self.title}, Body: {self.body}, at: {self.creation_date}"

	def __dict__(self):
		return {
			"id": self.id,
			"title": self.title,
			"body": self.body,
			"member_id": self.member_id,
			"creation_date": self.creation_date
		}

