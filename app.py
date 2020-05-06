from flask import Flask, send_from_directory
from flask_restful import Resource, Api, reqparse
from dotenv import load_dotenv
import gspread
import os

load_dotenv()
app = Flask(__name__)
api = Api(app)

#Load env Fil
google_creds = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")

gc = gspread.service_account(filename=google_creds)
sh = gc.open("Museums")
worksheet = sh.sheet1
museums = worksheet.get_all_records()

class MuseumsList(Resource):
    def get(self):
        return museums

api.add_resource(MuseumsList, '/')


class Museums(Resource):
    def get(self, museum_id):
        return museums[int(museum_id)]

api.add_resource(Museums, '/<museum_id>')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')

if __name__ == "__main__":
    app.run(debug=True)

