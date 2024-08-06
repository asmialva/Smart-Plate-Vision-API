from flask import Blueprint, request, jsonify

api_bp = Blueprint('api', __name__)

vehicles_data = {
    "DL7CD5017": {
        "insurance": "Valid",
        "fastag_balance": 500,
        "PUC":"Valid",
        "registration_details": {
            "owner": "Venky Bhat",
            "model": "Maruti Omni",
            "year": 2008
        }
    },
    "DL3CBU1384": {
        "insurance": "Expired",
        "fastag_balance": 0,
        "PUC":"Valid",
        "registration_details": {
            "owner": "Jane Smith",
            "model": "Suzuki Swift",
            "year": 2010
        }
    },
    "HR26CQ6869": {
        "insurance": "Valid",
        "fastag_balance": 1000,
        "PUC":"Valid",
        "registration_details": {
            "owner": "John Doe",
            "model": "Nissan Terrano",
            "year": 2016
        }
    },
        "DL2CAT4762": {
        "insurance": "Valid",
        "fastag_balance": 200,
        "PUC":"Expired",
        "registration_details": {
            "owner": "Maruthi Raikar",
            "model": "Pajero Sport",
            "year": 2013
        }
    },
    # Add more sample data as needed
}

@api_bp.route('/vehicle/details', methods=['POST'])
def get_vehicle_details():
    data = request.get_json()
    number_plate = data.get('number_plate')
    if not number_plate:
        return jsonify({"error": "Number plate is required"}), 400

    vehicle_info = vehicles_data.get(number_plate)
    if not vehicle_info:
        return jsonify({"error": "Vehicle not found"}), 404

    return jsonify(vehicle_info)
