from app import models
from app import stores
import datetime

def create_members():
	member1 = models.Member("Fares AbuAmin", 31)
	member2 = models.Member( "Lama Kheir", 30)
	member3 = models.Member("Ali Silan", 28)
	print(member1)
	print(member2)
	print(member3)
	print("=" * 40)

	return member1, member2, member3

def store_should_add_model(member_instance, member_store):
	for Member in member_instance:
		member_store.add(Member)

def print_all_members(member_store):
	print("=" * 40)
	for Member in member_store.get_all():
		print(Member)
	print("=" * 40)

def stores_similar():
	member_store1 = stores.MemberStore()
	member_store2 = stores.MemberStore()
	if member_store1.get_all() is member_store2.get_all():
		print("same stores")

def same_retrieved_objects(member_store, member):
	member_retrieved = member_store.get_by_id(member.id)
	if member is member_retrieved:
		print("tow members matching")
def update_object(member_store, member):
	member_copy = models.Member(member.name, member.age)
	member_copy.id = 2
	if member_copy is not member:
		print("member and member_copy are not the same")
	print(member_copy)
	member_copy.name = "Wafaa"
	member_store.update(member_copy)
	print(member_store.get_by_id(member.id))

def deleteing():
	try:
		member_store.delete(1)
	except ValueError:
		print("It should be an existence entity before deleting !")

def store_should_get_members_by_name(member_store):
	print("*" * 40)
	print("Getting by name:")
	members_by_name_retrieved = member_store.get_by_name("Lama Kheir")
	print(members_by_name_retrieved)

def create_posts(member_instance):
	post1 = models.Post("post1", "this is post1", member_instance[0].id)
	post2 = models.Post("post2", "this is post2", member_instance[0].id)
	post3 = models.Post("post3", "this is post3", member_instance[1].id)
	post4 = models.Post("post4", "this is post4", member_instance[1].id)
	post5 = models.Post("post5", "this is post5", member_instance[1].id)
	post6 = models.Post("post6", "this is post6", member_instance[2].id)
	post7 = models.Post("post7", "this is post7", member_instance[2].id)
	post8 = models.Post("post8", "this is post8", member_instance[2].id)
	post9 = models.Post("post9", "this is post9", member_instance[2].id)

	print(post1)
	print(post2)
	print(post3)
	print("=" * 40)

	return post1, post2, post3, post4, post5, post6, post7, post8, post9

def store_should_add_post(post_instance, post_store):
	for post in post_instance:
		post_store.add(post)

def store_should_get_members_with_posts(member_store, post_store):
	members_with_posts = member_store.get_member_with_post(post_store.get_all())
	for member_with_posts in members_with_posts:
		print(f"{member_with_posts} has posts:")
		for post in member_with_posts.posts:
			print(f"\t{post}")
		print("=" * 10)

def store_should_get_top_two(member_store, post_store):
	top_two_members = member_store.get_top_two(post_store.get_all())
	for member_with_posts in top_two_members:
		print(f"{member_with_posts} has posts:")
		for post in member_with_posts.posts:
			print(f"\t{post}")

def store_should_get_posts_by_date(post_store):
	print("=" * 30 + "posts by date" + "=" * 30)
	all_posts = post_store.get_posts_by_date()
	for post in all_posts:
		print(f"\t{post}")



member_instance = create_members()
member1, member2, member3 = member_instance
member_store = stores.MemberStore()
store_should_add_model(member_instance, member_store)
stores_similar()
print_all_members(member_store)
same_retrieved_objects(member_store, member2)
update_object(member_store, member2)
deleteing()
store_should_get_members_by_name(member_store)
post_instance = create_posts(member_instance)
post1, post2, post3, post4, post5, post6, post7, post8, post9 = post_instance
post_store = stores.PostStore()
store_should_add_post(post_instance, post_store)
store_should_get_members_with_posts(member_store, post_store)
store_should_get_top_two(member_store, post_store)
store_should_get_posts_by_date(post_store)


