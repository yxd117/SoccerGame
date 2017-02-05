from soccersimulator.mdpsoccer import SoccerTeam
from MyStrategy import StraightStrategy, RandomStrategy

team1 = SoccerTeam(name="team1",login="etu1")
team2 = SoccerTeam(name="team2",login="etu2")
team1.add("John",StraightStrategy()) 
team2.add("Paul",RandomStrategy())   #Strategie aleatoire
team2.add("Thomas",RandomStrategy())   #Strategie aleatoire