import itertools, copy, datetime

class BaseStore():
	def __init__(self, data_provider, last_id):
		self._data_provider = data_provider
		self._last_id = last_id

	def get_all(self):
		return self._data_provider

	def add(self, item_instance):
		item_instance.id = self._last_id
		self._data_provider.append(item_instance)
		self._last_id += 1

	def get_by_id(self, id):
		all_items = self.get_all()
		result = None
		for item_instance in all_items:
			if item_instance.id == id:
				result = item_instance
				break
		return result

	def update(self, item_instance):
		result = item_instance
		all_items = self.get_all()
		for index, current_item in enumerate(all_items):
			if current_item.id == item_instance.id:
				all_items[index] = item_instance
		return result

	def delete(self, id):
		item_instance = self.get_by_id(id)
		self._data_provider.remove(item_instance)

	def entity_exists(self, item_instance):
		result = True
		if self.get_by_id(item_instance.id) is None:
			result = False
		return result




class MemberStore(BaseStore):
	members = []
	last_id = 1

	def __init__(self):
		super().__init__(MemberStore.members, MemberStore.last_id)


	def get_by_name(self, name):
		return (member for member in self.get_all() if member.name == name)


	def get_member_with_post(self, all_posts):
		all_members = copy.deepcopy(self.get_all())
		for member, post in itertools.product(all_members, all_posts):
			if member.id == post.member_id:
				member.posts.append(post)
		for member in all_members:
			yield member

	def get_top_two(self, all_posts):
		all_members = list(self.get_member_with_post(all_posts))
		all_members.sort(key=lambda top: len(top.posts), reverse=True)
		yield all_members[0]
		yield all_members[1]





class PostStore(BaseStore):
	posts = []
	last_id = 1

	def __init__(self):
		super().__init__(PostStore.posts, PostStore.last_id)

	def get_key(self, post):
		return post.creation_date

	def get_posts_by_date(self):
		all_posts = list(self.get_all())
		all_posts.sort(key=self.get_key, reverse=True)
		return all_posts




		
