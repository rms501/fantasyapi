from flask import Blueprint, request, jsonify

hydration_controller = Blueprint('hydration_controller', __name__)

@hydration_controller.route('/hydrate/gameIds', methods=['POST'])
def hydrate_game_ids():
	return 'test'
	