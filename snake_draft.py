def invert_array(array):
  inverted = []
  for i in range(len(array)):
    inverted.append(array.pop())
  return inverted

def snake_draft(ordered_players, people_per_team):
    number_teams = len(ordered_players)//people_per_team
    teams = []
    for _ in range(number_teams):
        teams.append([])
    
    while len(ordered_players) > 0:
        for team in teams:
            team.append(ordered_players.pop(0))
        teams = invert_array(teams)
    
    return teams

people = []
snake_draft(people, 3)