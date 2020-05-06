from flask import Flask, send_from_directory
from flask_restful import Resource, Api, reqparse
from dotenv import load_dotenv
import gspread
import os

load_dotenv()
app = Flask(__name__)
api = Api(app)


google_creds = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")


gc = gspread.service_account(filename=google_creds)
sh = gc.open("Museums")
worksheet = sh.sheet1

class MuseumsList(Resource):
    def get(self):
        museums = worksheet.get_all_records()
        return museums

api.add_resource(MuseumsList, '/')


class Museums(Resource):
    def get(self, museum_id):
        values_list = worksheet.row_values(museum_id)
        return(values_list)

api.add_resource(Museums, '/<museum_id>')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')

if __name__ == "__main__":
    app.run(debug=True)

