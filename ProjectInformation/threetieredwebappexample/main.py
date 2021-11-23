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
@app.get("/player/<player_id>")
def get_player_information(player_id: str):
    result = player_service.service_get_player_information(int(player_id))
    result_as_dictionary = result.make_player_dictionary()
    result_as_json = jsonify(result_as_dictionary)
    return result_as_json


# get all player information
@app.get("/player")
def get_all_players_information():
    players_as_players = player_service.service_get_all_players_information()
    players_as_dictionary = []
    for players in players_as_players:
        dictionary_player = players.make_player_dictionary()
        players_as_dictionary.append(dictionary_player)
    return jsonify(players_as_dictionary)


# update player information NEED TO REIMPLEMENT THE SERVICE LOGIC FOR THIS ROUTE
@app.patch("/player/<player_id>")
def update_player_information(player_id: str):
    try:
        player_data = request.get_json()
        new_player = Player(
            player_data["firstName"],
            player_data["lastName"],
            player_data["jerseyNumber"],
            int(player_id),
            player_data["teamId"]
        )
        updated_player = player_service.service_update_player_information(new_player)
        return "Player updated successfully, the player info is now " + str(updated_player)
    except DuplicateJerseyNumberException as e:
        return str(e)


# delete player information
@app.delete("/player/<player_id>")
def delete_player_information(player_id: str):
    result = player_service.service_delete_player_information(int(player_id))
    if result:
        return "Player with id {} was deleted successfully".format(player_id)
    else:
        # this will run if the player we try to delete is not in the database. Ideally we would
        # instead use a try except block, but this works for now
        return "Something went wrong: player with id {} was not deleted".format(player_id)


app.run()
