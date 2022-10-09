from RPSLS_player import RPSLS_player

class P17324(RPSLS_player):
  def __init__(self):
    self.a = 0

  def shoot(self):
    rpsls = ["rock", "paper", "scissors", "lizard", "spock"]
    return rpsls[self.a]

  def update(self, result: str, competitor_shot: str):
    rpsls = ["rock", "paper", "scissors", "lizard", "spock"]
    if competitor_shot == "rock" :
      self.a = 1
    elif competitor_shot == "paper" :
      self.a = 2
    elif competitor_shot == "scissors" :
      self.a = 3
    elif competitor_shot == "lizard" :
      self.a = 4
    else :
      self.a = 0