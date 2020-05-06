from flask import Flask
from flask_restful import Resource, Api, reqparse
import gspread

app = Flask(__name__)
api = Api(app)


class MuseumsList(Resource):
    def get(self):
        gc = gspread.service_account()
        sh = gc.open("Museums")
        worksheet = sh.sheet1
        museums = worksheet.get_all_records()
        return museums

api.add_resource(MuseumsList, '/')


class Museums(Resource):
    def get(self, museum_id):
        gc = gspread.service_account()
        sh = gc.open("Museums")
        worksheet = sh.sheet1
        values_list = worksheet.row_values(museum_id)
        return(values_list)

api.add_resource(Museums, '/<museum_id>')

if __name__ == "__main__":
    app.run(debug=True)

