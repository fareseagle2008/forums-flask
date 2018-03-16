from flask import request, abort, jsonify
from app import models
from app import app, member_store, post_store

@app.route("/api/topic/all")
def topic_get_all():
    posts = [post.__dict__() for post in post_store.get_all()]
    return jsonify(posts)

@app.route("/api/topic/show/<int:id>")
def topic_show(id):
    post = post_store.get_by_id(id)
    try:
        result = jsonify(post.__dict__())
    except AttributeError:
        result = abort(404, f"topic with id: {id} dose not exist")
    return result

@app.route("/api/topic/delete/<int:id>")
def topicDelete(id):
    try:
        post_store.delete(id)
    except ValueError:
        abort(404, f"topic with id: {id} dose not exist")

    @app.route("/api/topic/add", methods = ["POST"])
def topic_create():
    request_data = request.get_json()
    try:
        new_post = models.Post(request_data["title"], request_data["body"])
        post_store.add(new_post)
        result = jsonify(new_post.__dict__())
    except KeyError:
        result = abort(400, f"could not parse the request data")
    return result

@app.route("/api/topic/edit/<int:id>", methods = ["PUT"])
def topic_edit(id):
    request_data = request.get_json()
    updated_post = post_store.get_by_id(id)
    try:
        updated_post.title = request_data["title"]
        updated_post.body = request_data["body"]
        post_store.update(updated_post)
        result = jsonify(updated_post.__dict__())
    except AttributeError:
        result = abort(404, f"topic with id: {id} does not exist")
    except KeyError:
        result = abort(400, f"could not parse request data")
    return result

@app.errorhandler(400)
def bad_request(error):
    return jsonify(message = error.description)