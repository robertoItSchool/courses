# Define a class for a football team, only the starting eleven (no substitutes/reserves)
# it can contain 3-5 defenders, 3-5 midfield players and 1-3 strikers; it has to have 11 players in total, 1 goalkeeper
# all players have stats from 1-10 (1 bad, 10 perfect)
# goalkeepers: communication, aerial reach, reflexes, passing, concentration, stamina, strength
# defenders: communication, tackling, heading, passing, concentration, stamina, strength
# midfielders: players: tackling, dribbling, heading, passing, stamina, strength
# strikers: dribbling, finishing, heading, passing, composure, stamina, strength, concentration
# create 3 teams of players, one with good players, one with medium players & one with weak players

import random


class PlayerStats:
  def __init__(self, passing, stamina):
    self.passing = passing
    self.stamina = stamina


class DefensivePlayerStats(PlayerStats):
  def __init__(self, communication, concentration, passing, stamina):
    self.communication = communication
    self.concentration = concentration
    # call the parent constructor - Player
    super().__init__(passing, stamina)


class Goalkeeper:
  # the constructor
  def __init__(self, communication, reflexes, passing, stamina, concentration):
    # save value to object
    self.reflexes = reflexes
    # create a DefensivePlayerStats object
    self.stats = DefensivePlayerStats(communication, concentration, passing, stamina)


class Defender:
  # the constructor
  def __init__(self, communication, tackling, passing, stamina, concentration):
    # save values to object
    self.tackling = tackling
    # create a DefensivePlayerStats object
    self.stats = DefensivePlayerStats(communication, concentration, passing, stamina)


class Midfielder:
  def __init__(self, dribbling, tackling, passing, stamina):
    # save to object
    self.dribbling = dribbling
    self.tackling = tackling
    self.stats = PlayerStats(passing, stamina)


class GoodMidfielder(Midfielder):
  def __init__(self):
    d, t, p, s = random.randint(7, 10), random.randint(6, 10), random.randint(9, 10), random.randint(8, 10)
    super().__init__(d, t, p, s)


class Team:
  def __init__(self, goalkeeper, defenders, midfielders):
    self.goalkeepers = goalkeeper
    self.defenders = defenders
    self.midfielders = midfielders

  def show(self):
    output = self.__dict__
    for player_type, list_players in output.items():
      print(player_type)
      for player in list_players:
        print(player)
        print(player.__dict__)
        print(player.stats.__dict__)



gk1 = Goalkeeper(8, 5, 3, 4, 8)
cb1 = Defender(6, 7, 2, 8, 2)
cb2 = Defender(9, 5, 3, 7, 6)
md1 = Midfielder(10, passing=1, stamina=8, tackling=2)
md2 = Midfielder(tackling=6, passing=6, stamina=5, dribbling=10)

i = 0
list_defenders = []
while i < 5:
  x0, x1, x2, x3, x4 = random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), \
                       random.randint(1,10), random.randint(1, 10)
  new_defender = Defender(x0, x1, x2, x3, x4)
  list_defenders.append(new_defender)
  i += 1

list_mids = 3 * [GoodMidfielder()]

team = Team([gk1], list_defenders, list_mids)
team.show()

# f = open('file', newline='')
