import json
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
        parser.add_argument("link", required=True)

        args = parser.parse_args()
        print(">>>" * 5)
        results = scraper(args["link"])
        if results == "":
            print("Failed to find the item")
            return results, 404

        if results is None:
            print("CheapBuy only supports\n"
                  "1) amazon.com\n"
                  "2) ebay.com\n"
                  "3) walmart.com\n"
                  "4) costco.com\n"
                  "5) Bjs.com\n"
                  "please use only these websites to search for your item. Sorry for any inconvenience")
            return results, 404
        print(json.dumps(results, indent=4, sort_keys=True))
        return results, 200


api.add_resource(Scrap, "/scrap")
if __name__ == "__main__":
    app.run(debug=True, port=8080, host="127.0.0.1")  # run our Flask app
