"""this is where my API will go: I will create a flask object here and define my routes and their functions here"""
from flask import Flask, request, jsonify

from custom_exceptions.duplicate_jersey_number_exception import DuplicateJerseyNumberException
from custom_exceptions.duplicate_team_name_exception import DuplicateTeamNameException
from data_access_layer.implementation_classes.player_dao_imp import PlayerDAOImp
from data_access_layer.implementation_classes.team_dao_imp import TeamDAOImp
from entities.players import Player
from entities.teams import Team
from service_layer.implementation_services.player_service_imp import PlayerServiceImp
from service_layer.implementation_services.team_service_imp import TeamServiceImp

app: Flask = Flask(__name__)

player_dao = PlayerDAOImp()
player_service = PlayerServiceImp(player_dao)
team_dao = TeamDAOImp()
team_service = TeamServiceImp(team_dao)


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
        return "Something went wrong: player with id {} was not deleted".format(player_id)


@app.post("/team")
def create_team():
    try:
        body = request.get_json()
        new_team = Team(
            body["teamId"],
            body["name"]
        )
        created_team = team_service.service_create_team(new_team)
        created_team_as_dictionary = created_team.create_team_dictionary()
        return jsonify(created_team_as_dictionary), 201
    except DuplicateTeamNameException as e:
        error_message = {"errorMessage": str(e)}
        return jsonify(error_message), 400


@app.get("/team/<team_id>")
def get_team_by_id(team_id: str):
    team = team_service.service_get_team_by_id(int(team_id))
    team_as_dictionary = team.create_team_dictionary()
    return jsonify(team_as_dictionary), 200


@app.get("/team")
def get_all_teams():
    teams = team_service.service_get_all_teams()
    teams_as_dictionaries = []
    for team in teams:
        dictionary_team = team.create_team_dictionary()
        teams_as_dictionaries.append(dictionary_team)
    return jsonify(teams_as_dictionaries), 200


@app.patch("/team/<player_id>")
def update_team(player_id: str):
    try:
        body = request.get_json()
        update_info = Team(
            body["teamId"],
            body["name"]
        )
        updated_player = team_service.service_update_team_information(update_info)
        updated_player_as_dictionary = updated_player.create_team_dictionary()
        return jsonify(updated_player_as_dictionary), 200
    except DuplicateTeamNameException as e:
        error_message = {"errorMessage": str(e)}
        return jsonify(error_message)


@app.delete("/team/<team_id>")
def delete_team(team_id :str):
    result = team_service.service_delete_team_information(int(team_id))
    if result:
        return "Team with id {} was deleted successfully".format(team_id)
    else:
        return "Something went wrong: team with id {} was not deleted".format(team_id)


app.run()
