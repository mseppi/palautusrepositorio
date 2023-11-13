import requests

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url).json()
        players = []
        for player in response:
            players.append(player)
        return players

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()
        nat_players = []
        return_players = []
        for i in players:
            if i["nationality"]==nationality:
                nat_players.append(i)
        nat_players.sort(key=lambda x: x["goals"]+x["assists"], reverse=True)
        for i in nat_players:
            return_players.append(Player(i))
        return return_players

class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.nationality = dict["nationality"]

    
    
    def __str__(self):
        return f"{self.name:20} {self.team:3} {self.goals:2} + {self.assists:2} = {self.goals + self.assists:2}"
