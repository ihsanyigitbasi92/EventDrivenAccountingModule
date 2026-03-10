
"""
Define API routes for the application.
"""

from flask import Blueprint, jsonify
from app.controllers import account_controller

def setup_routes(app):
    main_bp = Blueprint('main', __name__)

    @main_bp.route('/accounts', methods=['GET'])
    def get_accounts():
        return account_controller.get_accounts()

    app.register_blueprint(main_bp)
