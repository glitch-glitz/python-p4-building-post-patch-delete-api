# #!/usr/bin/env python3

# from flask import Flask, request, make_response
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# from models import db, User, Review, Game

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.json.compact = False

# migrate = Migrate(app, db)

# db.init_app(app)

# @app.route('/')
# def index():
#     return "Index for Game/Review/User API"

# @app.route('/games')
# def games():

#     games = []
#     for game in Game.query.all():
#         game_dict = {
#             "title": game.title,
#             "genre": game.genre,
#             "platform": game.platform,
#             "price": game.price,
#         }
#         games.append(game_dict)

#     response = make_response(
#         games,
#         200
#     )

#     return response

# @app.route('/games/<int:id>')
# def game_by_id(id):
#     game = Game.query.filter(Game.id == id).first()
    
#     game_dict = game.to_dict()

#     response = make_response(
#         game_dict,
#         200
#     )

#     return response

# @app.route('/reviews')
# def reviews():

#     reviews = []
#     for review in Review.query.all():
#         review_dict = review.to_dict()
#         reviews.append(review_dict)

#     response = make_response(
#         reviews,
#         200
#     )

#     return response

# @app.route('/users')
# def users():

#     users = []
#     for user in User.query.all():
#         user_dict = user.to_dict()
#         users.append(user_dict)

#     response = make_response(
#         users,
#         200
#     )

#     return response

# if __name__ == '__main__':
#     app.run(port=5555, debug=True)


#!/usr/bin/env python3

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, User, Review, Game

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route("/")
def index():
    return "Index for Game/Review/User API"


@app.route("/games")
def games():
    games = [game.to_dict() for game in Game.query.all()]
    return jsonify(games), 200


@app.route("/games/<int:id>")
def game_by_id(id):
    game = Game.query.filter(Game.id == id).first()
    if not game:
        return jsonify({"error": "Game not found"}), 404
    return jsonify(game.to_dict()), 200


@app.route("/reviews")
def reviews():
    reviews = [review.to_dict() for review in Review.query.all()]
    return jsonify(reviews), 200


@app.route("/users")
def users():
    users = [user.to_dict() for user in User.query.all()]
    return jsonify(users), 200


if __name__ == "__main__":
    app.run(port=5555, debug=True)
