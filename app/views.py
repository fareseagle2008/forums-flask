from flask import render_template, request, redirect, url_for, abort, jsonify
from app import models
from app import app, member_store, post_store


@app.route("/")
@app.route("/index")
def home():
	return render_template(	"index.html", posts = post_store.get_all())

@app.route("/topic/add", methods = ["GET", "POST"])
def topic_add():
	if request.method == "POST":
		new_post = models.Post(request.form["title"], request.form["body"])
		post_store.add(new_post)
		return redirect(url_for("home"))
	else:
		return render_template("topic_add.html")

@app.route("/topic/delete/<int:id>")
def topic_delete(id):
	try:
		post_store.delete(id)
	except ValueError:
		abort(404)
	return redirect(url_for("home"))

@app.route("/topic/update/<int:id>", methods = ["GET", "POST"])
def topic_update(id):
	updated_post = post_store.get_by_id(id)
	if updated_post is None:
		abort(404)
	if request.method == "POST":
		updated_post.title = request.form["title"]
		updated_post.body = request.form["body"]
		post_store.update(updated_post)
		return redirect(url_for("home"))
	else:
		return render_template("topic_update.html", post = updated_post)

@app.route("/topic/view/<int:id>")
def topic_view(id):
	viewed_post = post_store.get_by_id(id)
	if viewed_post is None:
		abort(404)
	return render_template("topic_show.html", post = viewed_post)

@app.route("/api/topic/all")
def topic_get_all():
	posts =  [post.__dict__() for post in post_store.get_all()]
	return jsonify(posts)

@app.route("/api/topic/add", methods = ["POST"])
def topic_create():
	request_data = request.get_json()
	new_post = models.Post(request_data["title"], request_data["body"])
	post_store.add(new_post)
	return jsonify(new_post.__dict__())

@app.route("/api/topic/show/<int:id>")
def topic_show(id):
	post = post_store.get_by_id(id)
	if post is None:
		abort(404)
	return jsonify(post.__dict__())

@app.route("/api/topic/edit/<int:id>", methods = ["GET", "POST"])
def topic_edit(id):
	request_data = request.get_json()
	updated_post = post_store.get_by_id(id)
	if updated_post is None:
		abort(404)
	if request.method == "POST":
		updated_post.title = request_data["title"]
		updated_post.body = request_data["body"]
		post_store.update(updated_post)
		return jsonify(updated_post.__dict__())
	else:
		return render_template("topic_update.html", post = updated_post)

@app.route("/api/topic/delete/<int:id>")
def topicDelete(id):
	try:
		post_store.delete(id)
	except ValueError:
		abort(404)
	return redirect(url_for("home"))