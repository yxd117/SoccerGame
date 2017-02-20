from soccersimulator.mdpsoccer import SoccerTeam
from MyStrategy import RandomStrategy, StraightStrategy1, StraightStrategy2, StraightStrategy3, DefendStrategy
def get_team(i):
	team = SoccerTeam(name="team",login="etu1")
	if i == 1:
		team.add("Mike",StraightStrategy1())
	elif i == 2:
		team.add("Mike",StraightStrategy1())
		team.add("Paul",DefendStrategy(0))
	elif i == 4:
		team.add("Mike",DefendStrategy(1))
		team.add("Paul",DefendStrategy(2))	
		team.add("Thomas",StraightStrategy1())
		team.add("Jim",StraightStrategy1())
	return team
