from soccersimulator.mdpsoccer import SoccerTeam
from MyStrategy import StraightStrategy, RandomStrategy

team1 = SoccerTeam(name="team1",login="etu1")
team2 = SoccerTeam(name="team2",login="etu2")
team1.add("John",StraightStrategy2()) 
team2.add("Paul",StraightStrategy1())   
team2.add("Thomas",StraightStrategy2()) 