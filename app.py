import constants
import ast
import pdb
import math
import sys

teams = constants.TEAMS
players = constants.PLAYERS

num_players = len(players) / len(teams)
num_players = int(num_players)
not_experienced = []
is_experienced = []
Panthers = []
Bandits = []
Worriers = []

def clean_data():
    for player in players:
        height = player["height"].split()
        player["height"] = int(height[0])
        #saw Christopher Spagnesi post on slack for the int conversion
        if player["experience"] == "YES":
            player["experience"] = True
            is_experienced.append(player)
        if player["experience"] == "NO":
            player["experience"] = False
            not_experienced.append(player)
            #looked on gdchoices43 github for help on experience on nonexperience 
            
def team_balance():
    teams [0] = is_experienced[:3] + not_experienced[:3]
    teams [1] = is_experienced[3:6] + not_experienced[3:6]
    teams [2] = is_experienced[6:9] + not_experienced[6:9]
    #looked on gdchoices43 github for help on experience on team_balance
    
def home_screen():
    print("*" * 82)
    print(":^..^_('')_{**}_^..^_('')_{**}_^..^_('')_{**}_^..^_('')_{**}_^..^_('')_{**}_^..^:\n"
          "_________________________Pick a team to view their stats!________________________")
    print("                              If not enter exit                                  ")
    print("*" * 82)
    print("\n \n  \n:^..^_Panthers_^..^: --> A\n \n"
          ":('')_Bandits_(''): -->  B\n \n"
          ":{**}_Worriers_{**}: --> C    ")


clean_data()
team_balance()

while True:
    print("*" * 82)
    print("   Welcom to B Ball Stats where you can view your favorite players statistics!\n"
              "______________________________Do you want to proceed?_____________________________")
    proceed = input("                                        Y/N  ")
    print("*" * 82)
    print("\n \n  \n:^..^_Panthers_^..^:\n \n"
              ":('')_Bandits_(''):\n \n"
              ":{**}_Worriers_{**}:")
    if proceed.upper() == "N":
        print("\nBYE\n")
        sys.exit()
    if proceed.upper() == "Y":
        print("\nProceeding!\n")
        break
    if (proceed.upper() != "Y") or (proceed.upper() != "N"):
        print("\nTry again Y/N\n")
        continue
while True:
    home_screen()
    choose = input("\npick a team:  ")
    
    while True:
        try:
            if choose.lower() == "exit":
                print("\nBYE\n")
                sys.exit()
                
            if choose.upper() == "A":
                Panthers = teams [0]
                team1 = []
                team1_guardians = []
                team1_height = []
                height = [player["height"] for player in Panthers]
                average_height_team1 = round(sum(height) / len(Panthers), 1)
                average_height_team1 = float(average_height_team1)
                exp_player =  [player["experience"] for player in Panthers if player["experience"] == True]
                exp_player = int(len(exp_player))
                not_exp_player = [player["experience"] for player in Panthers if player["experience"] == False]
                not_exp_player = int(len(not_exp_player))
                #looked on gdchoices43 github to clear up how to average and experience vs non
                print("\n \n:^..^_Panthers Stats!_^..^:")
                print("\nThere are {} Panthers on the team".format(num_players))
                print("The Panthers average height is {}".format(average_height_team1))
                print("There are {} experienced Panthers".format(exp_player))
                print("There are {} non experienced Panthers".format(exp_player)) 
                print("\n :^..^_Player Stats!_^..^:")
                Panthers = teams [0]
                team1 = []
                team1_guardians = []
                team1_height = []
                for player in Panthers:
                    name = player["name"]
                    team1.append(str(name))
                print("\nPlayers Names:")
                print(", ".join(team1))
                #looked on gdchoices43 github to learn how to print the strings 
                for player in Panthers:
                    guardians = player["guardians"]
                    team1_guardians.append(str(guardians))
                print("\nPlayers Guardians:")
                print(", ".join(team1_guardians))
                for player in Panthers:
                    height = player["height"]
                    team1_height.append(str(height))
                print("\nHieght in inches:")
                print(", ".join(team1_height))
                more_stats = input("\n \nDo you you want to view other team stats? Y/N \n")
                if more_stats.upper() == "Y":
                    print("\nOK\n")
                    break
                    home_screen()
                    #looked on gdchoices43 github and learned how to incorperate the homescreen() function
                if more_stats.upper() == "N":
                    print("\nBYE\n")
                    sys.exit()
                if more_stats.upper() != "N":
                    print("\nNot a valid choice. Pick again.\n")
                    break 
                    home_screen()
                
            elif choose.upper() == "B":
                Bandits = teams [1]
                team2 = []
                team2_guardians = []
                team2_height = []
                height = [player["height"] for player in Bandits]
                average_height_team1 = round(sum(height) / len(Bandits), 1)
                average_height_team1 = float(average_height_team1)
                exp_player =  [player["experience"] for player in Bandits if player["experience"] == True]
                exp_player = int(len(exp_player))
                not_exp_player = [player["experience"] for player in Bandits if player["experience"] == False]
                not_exp_player = int(len(not_exp_player))
                #looked on gdchoices43 github to clear up how to average and experience vs non
                print("\n \n:('')_Bandits Stats!_(''):")
                print("\nThere are {} Bandits on the team".format(num_players))
                print("The Bandits average height is {}".format(average_height_team1))
                print("There are {} experienced Bandits".format(exp_player))
                print("There are {} non experienced Bandits".format(exp_player)) 
                print("\n :('')_Player Stats!_(''):")
                for player in Bandits:
                    name = player["name"]
                    team2.append(str(name))
                print("\nPlayers Names:")
                print(", ".join(team2))
                for player in Bandits:
                    guardians = player["guardians"]
                    team2_guardians.append(str(guardians))
                print("\nPlayers Guardians:")
                print(", ".join(team2_guardians))
                for player in Bandits:
                    height = player["height"]
                    team2_height.append(str(height))
                print("\nHieght in inches:")
                print(", ".join(team2_height))
                more_stats = input("\n \nDo you you want to view other team stats? Y/N \n")
                if more_stats.upper() == "Y":
                    print("\nOK\n")
                    break
                    home_screen()
                if more_stats.upper() == "N":
                    print("\nBYE\n")
                    sys.exit()
                if (more_stats.upper() != "N") or (more_stats.upper() != "Y"):
                    print("\nNot a valid choice. Pick again.\n")
                    break 
                    home_screen()
                    
            elif choose.upper() == "C":
                Worriers = teams [2]
                team3 = []
                team3_guardians = []
                team3_height = []
                height = [player["height"] for player in Worriers]
                average_height_team1 = round(sum(height) / len(Worriers), 1)
                average_height_team1 = float(average_height_team1)
                exp_player =  [player["experience"] for player in  Worriers if player["experience"] == True]
                exp_player = int(len(exp_player))
                not_exp_player = [player["experience"] for player in  Worriers if player["experience"] == False]
                not_exp_player = int(len(not_exp_player))
                #looked on gdchoices43 github to clear up how to average and experience vs non
                print("\n \n:{**}_ Worriers Stats!_{**}:")
                print("\nThere are {}  Worriers on the team".format(num_players))
                print("The Worriers average height is {}".format(average_height_team1))
                print("There are {} experienced  Worriers".format(exp_player))
                print("There are {} non experienced  Worriers".format(exp_player)) 
                print("\n :{**}_Player Stats!_{**}:")
                for player in  Worriers:
                    name = player["name"]
                    team3.append(str(name))
                print("\nPlayers Names:")
                print(", ".join(team3))
                for player in  Worriers:
                    guardians = player["guardians"]
                    team3_guardians.append(str(guardians))
                print("\nPlayers Guardians:")
                print(", ".join(team3_guardians))
                for player in  Worriers:
                    height = player["height"]
                    team3_height.append(str(height))
                print("\nHieght in inches:")
                print(", ".join(team3_height))
                more_stats = input("\n \nDo you you want to view other team stats? Y/N \n")
                if more_stats.upper() == "Y":
                    print("\nOK\n")
                    break
                    home_screen()
                if more_stats.upper() == "N":
                    print("\nBYE\n")
                    sys.exit()
                if (more_stats.upper() != "N") or (more_stats.upper() != "Y"):
                    print("\nNot a valid choice. Pick again.\n")
                    break 
                    home_screen()
                
                elif (choose.upper() != "A") or (choose.upper() != "B") or (choose.upper() != "C"):
                    print("\nNot a valid selection")
                    break
                    home_screen()
            if (choose.upper() != "A") or (choose.upper() != "B") or (choose.upper() != "C"):
                raise ValueError("That is not a valid selection. Try again.")
        except ValueError as err:
            print("\n{} \n".format(err))
            break
            home_screen()
                    

if __name__=='__main__':
    print(players [0])  
                
    
    
    
    
    
    
    
    
    
    
    
    
    
    
