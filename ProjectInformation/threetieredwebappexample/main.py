"""this is where my API will go: I will create a flask object here and define my routes and their functions here"""
from flask import Flask, request, jsonify

from custom_exceptions.duplicate_jersey_number_exception import DuplicateJerseyNumberException
from data_access_layer.implementation_classes.player_dao_imp import PlayerDAOImp
from entities.players import Player
from service_layer.implementation_services.player_service_imp import PlayerServiceImp

app: Flask = Flask(__name__)

player_dao = PlayerDAOImp()
player_service = PlayerServiceImp(player_dao)


# create player method
@app.post("/player")
def create_player_entry():
    try:
        player_data = request.get_json()
        new_player = Player(
            player_data["firstName"],
            player_data["lastName"],
            player_data["jerseyNumber"],
            player_data["playerId"],
            player_data["teamId"]
        )
        player_to_return = player_service.service_create_player_entry(new_player)
        player_as_dictionary = player_to_return.make_player_dictionary()
        player_as_json = jsonify(player_as_dictionary)
        return player_as_json
    except DuplicateJerseyNumberException as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


# get player information
def get_player_information():
    pass


# get all player information
def get_all_players_information():
    pass


# update player information
def update_player_information():
    pass


# delete player information

def delete_player_information():
    pass


app.run()
