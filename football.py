# Define a class for a football team, only the starting eleven (no substitutes/reserves)
# it can contain 3-5 defenders, 3-5 midfield players and 1-3 strikers; it has to have 11 players in total, 1 goalkeeper
# all players have stats from 1-10 (1 bad, 10 perfect)
# goalkeepers: communication, aerial reach, reflexes, passing, concentration, stamina, strength
# defenders: communication, tackling, heading, passing, concentration, stamina, strength
# midfielders: players: tackling, dribbling, heading, passing, concentration, stamina, strength
# strikers: dribbling, finishing, heading, passing, composure, stamina, strength
# create 3 teams of players, one with good players, one with medium players & one with weak players

from abc import ABC, abstractmethod


class PlayerStats():
  def __init__(self, passing, stamina):
    self.passing = passing
    self.stamina = stamina


class DefensivePlayer(ABC):
  @abstractmethod
  def __init__(self, communication):
    self.communication = communication


class Goalkeeper(DefensivePlayer):
  def __init__(self, communication, reflexes, playerStats):
    # save value to object
    self.reflexes = reflexes
    # call the parents constructor
    self.stats = playerStats
    DefensivePlayer.__init__(self, communication)


class Defender(Player):
  # the constructor
  def __init__(self, communication, tackling, passing, stamina):
    self.communication = communication
    self.tackling = tackling
    # call the parent constructor
    super().__init__(passing, stamina)


class Midfielder(Player):
  def __init__(self, dribbling, tackling, passing, stamina):
    # save to object
    self.dribbling = dribbling
    self.tackling = tackling
    # call the parent constructor
    super().__init__(passing, stamina)


class Team:
  def __init__(self, x, y, z):
    self.goalkeeper = x
    self.defenders = y
    self.midfielders = z


gk1 = Goalkeeper(8, 5, PlayerStats(3, 4))
cb1 = Defender(6, 7, 2, 8)
cb2 = Defender(9, 5, 3, 7)
md1 = Midfielder(10, 1, 8, 2)
md2 = Midfielder(6, 6, 5, 10)

team = Team(z=[cb1, cb2], y=[md1, md2], x=gk1)
print(team.goalkeeper.__dict__)
