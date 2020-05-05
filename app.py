from flask import Flask
from flask_restful import Resource, Api, reqparse
import gspread

app = Flask(__name__)
api = Api(app)
# MUSEUMS = {
#     '0': {'name': 'Pen Museum', 'address': 'Unit 3, The Argent Centre, 60 Frederick Street, Birmingham,	B1 3H', 'url': 'https://penmuseum.org.uk/'},
#     '1': {'name': 'Coffin Works', 'address': '13-15 Fleet Street, Jewellery Quarter, Birmingham	B3 1JP', 'url': 'http://www.coffinworks.org/'},
#     '2': {'name': 'Dog Collar Museum', 'address': 'Leeds Castle, Maidstone, Kent, ME17 1PL', 'url': 'https://www.leeds-castle.com/Visit/Attractions/The+Castle+%26amp%3B+Exhibitions/'},
#     '3': {'name': 'Derwent Pencil Museum', 'address': 'Cumberland Pencil Company, Derwent House, Lillyhall Business Park, Workington, Cumbria, CA14 4HS', 'url': 'https://www.derwentart.com/en/gb/7523/derwent-pencil-museum'},
#     '4': {'name': 'Cuckooland', 'address': 'The Old School, Chester Road, Tabley, Cheshire 	WA16 0HL', 'url': 'http://www.cuckoolandmuseum.com/'},
#     '5': {'name': 'House of Marbles', 'address': 'The Old Pottery, Pottery Road, Bovey Tracey, Devon, TQ13 9DS', 'url': 'https://www.houseofmarbles.com/'},
#     '6': {'name': 'British Lawnmover Museum', 'address': '106-112 Shakespeare Street, Southport, Merseyside, PR8 5AJ', 'url': 'http://www.lawnmowerworld.co.uk/'},
#     '7': {'name': 'The Fan Museum', 'address': '12 Crooms Hill, Greenwich, London, SE10 8ER', 'url': 'https://www.thefanmuseum.org.uk/'},
#     '8': {'name': 'The Cinema Museum', 'address': '2 Dugard Way (off Renfrew Road), London, SE11 4TH', 'url': 'http://www.cinemamuseum.org.uk/'},
#     '9': {'name': 'Shell Grotto', 'address': 'Grotto Hill, Margate, Kent, CT9 2BU', 'url': 'http://shellgrotto.co.uk/'},
# }


class MuseumsList(Resource):
    def get(self):
        gc = gspread.service_account()
        sh = gc.open("Museums")
        worksheet = sh.sheet1
        list_of_lists = worksheet.get_all_values()
        return list_of_lists

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

