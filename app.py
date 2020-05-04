from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)
MUSEUMS = {
    '1': {'name': 'Pen Museum', 'address': 'Unit 3, The Argent Centre, 60 Frederick Street, Birmingham,	B1 3H', 'url': 'https://penmuseum.org.uk/'},
    '2': {'name': 'Coffin Works', 'address': '13-15 Fleet Street, Jewellery Quarter, Birmingham	B3 1JP', 'url': 'http://www.coffinworks.org/'},
    '3': {'name': 'Dog Collar Museum', 'address': 'Leeds Castle, Maidstone, Kent, ME17 1PL', 'url': 'https://www.leeds-castle.com/Visit/Attractions/The+Castle+%26amp%3B+Exhibitions/'},
    '4': {'name': 'Derwent Pencil Museum', 'address': 'Cumberland Pencil Company, Derwent House, Lillyhall Business Park, Workington, Cumbria, CA14 4HS', 'url': 'https://www.derwentart.com/en/gb/7523/derwent-pencil-museum'},
    '5': {'name': 'Cuckooland', 'address': 'The Old School, Chester Road, Tabley, Cheshire 	WA16 0HL', 'url': 'http://www.cuckoolandmuseum.com/'},
    '6': {'name': 'House of Marbles', 'address': 'The Old Pottery, Pottery Road, Bovey Tracey, Devon, TQ13 9DS', 'url': 'https://www.houseofmarbles.com/'},
    '7': {'name': 'British Lawnmover Museum', 'address': '106-112 Shakespeare Street, Southport, Merseyside, PR8 5AJ', 'url': 'http://www.lawnmowerworld.co.uk/'},
    '8': {'name': 'The Fan Museum', 'address': '12 Crooms Hill, Greenwich, London, SE10 8ER', 'url': 'https://www.thefanmuseum.org.uk/'},
    '9': {'name': 'The Cinema Museum', 'address': '2 Dugard Way (off Renfrew Road), London, SE11 4TH', 'url': 'http://www.cinemamuseum.org.uk/'},
    '9': {'name': 'Shell Grotto', 'address': 'Grotto Hill, Margate, Kent, CT9 2BU', 'url': 'http://shellgrotto.co.uk/'},
}


class MuseumsList(Resource):
    def get(self):
        return MUSEUMS

api.add_resource(MuseumsList, '/')


class Museums(Resource):
    def get(self, museum_id):
        if museum_id not in MUSEUMS:
            return "Not found", 404
        else:
            return MUSEUMS[museum_id]

api.add_resource(Museums, '/<museum_id>')

if __name__ == "__main__":
    app.run(debug=True)

