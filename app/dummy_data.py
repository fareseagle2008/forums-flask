from app import models

dummy_members = [
	models.Member("Fares AbuAmin", 31),
	models.Member("Lama Kheir", 30),
	models.Member("Ali Silan", 28)
]

dummy_posts =[
	models.Post("post1", "this is post1", dummy_members[0].id),
	models.Post("post2", "this is post2", dummy_members[0].id),
	models.Post("post3", "this is post3", dummy_members[1].id),
	models.Post("post4", "this is post4", dummy_members[1].id),
	models.Post("post5", "this is post5", dummy_members[1].id),
	models.Post("post6", "this is post6", dummy_members[2].id),
	models.Post("post7", "this is post7", dummy_members[2].id),
	models.Post("post8", "this is post8", dummy_members[2].id),
	models.Post("post9", "this is post9", dummy_members[2].id)

]

def seed_stores(member_store, post_store):
    for member in dummy_members:
        member_store.add(member)

    for post in dummy_posts:
        post_store.add(post)