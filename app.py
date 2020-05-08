from flask import Flask, abort, jsonify, send_from_directory
from flask_restful import Resource, Api, reqparse
from dotenv import load_dotenv
import gspread
import os

load_dotenv()
app = Flask(__name__)
api = Api(app)

api_base = '/api/museums'

#Load env Fil
google_creds = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")

gc = gspread.service_account(filename=google_creds)
sh = gc.open("Museums")
worksheet = sh.sheet1
museums = worksheet.get_all_records()

class MuseumsList(Resource):
    def get(self):
        return museums

api.add_resource(MuseumsList, api_base + '/')


class Museums(Resource):
    def get(self, museum_id):

        if museum_id.isnumeric() == False:
            abort(422, description="Unprocessable Entity")

        return museums[int(museum_id)]

api.add_resource(Museums, api_base + '/<museum_id>')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')


@app.errorhandler(404)
def invalid_route(e):
    return jsonify({'errorCode' : 404, 'message' : 'Route not found'})

@app.errorhandler(422)
def unprocessable_entity(e):
    return jsonify({'errorCode' : 422, 'message' : 'Unprocessable Entity'})

if __name__ == "__main__":
    app.run(debug=True)

