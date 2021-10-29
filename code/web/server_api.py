from flask import Flask
from flask_restful import Resource, Api, reqparse
from scraper.web_scraper import scraper

from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

class Scrap(Resource):
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('link',required=True)

		args = parser.parse_args()
		print('>>>'*5)
		results = scraper(args['link'])	
		if results == '':
			return f"CheapBuy only supports\n \
							amazon.com\n \
							ebay.com\n \
							walmart.com\n \
							costco.com\n \
							Bjs.com\n \
							please use only these websites to search for your item.\n \
							Sorry for any inconvinience \n" , 404
		else:
			print('>>>'*5)
			print(results)
			print('<<<'*5)
			return results, 200
	pass


api.add_resource(Scrap, '/scrap')

if __name__ == '__main__':
	app.run(debug=True, port=8080, host="0.0.0.0")  # run our Flask app
