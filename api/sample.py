from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, request, Resource # used for REST API building
import requests  # used for testing
import random
from __init__ import app, db
from model.realEstateModels import House
# from ml.RealEstateRecEngine import RecEngine
# from ai.OpenAIEngine import CollegeAIEngine
import os
from cryptography.fernet import Fernet

realestate_api = Blueprint('house', __name__, url_prefix='/api/house')


api = Api(realestate_api)


class houses:

    class _getHouses(Resource):
        def get(self):
            houses = db.session.query(House).all()
            print("Hi")
            return jsonify([house.few_details() for house in houses])
        
    api.add_resource(_getHouses, "/houses")