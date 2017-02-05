from soccersimulator.mdpsoccer import SoccerTeam
from MyStrategy import StraightStrategy, RandomStrategy
from soccersimulator.gui import SimuGUI,show_state,show_simu
from soccersimulator.mdpsoccer import SoccerTeam, Simulation, SoccerAction



team1 = SoccerTeam(name="team1",login="etu1")
team2 = SoccerTeam(name="team2",login="etu2")
team1.add("John",StraightStrategy()) 
team2.add("Paul",RandomStrategy())   #Strategie aleatoire
team2.add("Thomas",RandomStrategy())   #Strategie aleatoire

#Creation d'une partie
simu = Simulation(team1,team2)
#Jouer et afficher la partie
show_simu(simu)
#Jouer sans afficher
simu.start()