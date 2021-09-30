from flask import Flask
from flask_restful import Resource, Api, reqparse
from web_scrapper import scrapper
import json
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
api = Api(app)

class Scrap(Resource):
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('link',required=True)

		args = parser.parse_args()

		results = scrapper(args['link'])
		print(results)
		return results, 200
	pass


api.add_resource(Scrap, '/scrap')

if __name__ == '__main__':
    app.run(debug=True)  # run our Flask app
