import os.path

from flask import Flask
from forum.auth import auth
from forum.comments import comments
from forum.posts import posts
from forum.subforums import subforums
# from forum.routes import rt
from os import path


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    # I think more blueprints might be used to break routes up into things like
    # post_routes
    # subforum_routes
    #
    # app.register_blueprint(rt)
    # Set globals
    from forum.models import db
    db.init_app(app)

    with app.app_context():
        # Add some routes
        if not os.path.exists('forum/lsk'):
            db.create_all()
        return app
