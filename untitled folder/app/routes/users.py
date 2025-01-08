from flask import Blueprint, request, jsonify
from app import db
from app.models import User
from flasgger import swag_from

users_bp = Blueprint('users', __name__)

@users_bp.route('/signup', methods=['POST'])
@swag_from({
    'responses': {
        '201': {
            'description': 'User successfully registered',
        },
        '400': {
            'description': 'Invalid input',
        }
    }
})
def signup():
    data = request.get_json()
    new_user = User(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        password=data['password']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully!"}), 201
