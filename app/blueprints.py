from flask import Blueprint

from flask_cors import CORS

from .utils import api_success

# =============================================================================
# Blueprints and CORS setup
# =============================================================================

api_v1 = Blueprint('api_v1', __name__)
cors = CORS(api_v1, origins=['*'])  # NOTE: In production, replace with frontend subdomain

# =============================================================================
# API Routes
# =============================================================================

@api_v1.route('/hello')
def hello():
    return api_success({'message': 'Hello World!'})

# NOTE: SECTION:ROUTES: Your routes go here...

