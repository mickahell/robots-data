import sys
from os import path
import pandas as pd


def team_stats(csv, pokemon, has_win):
    file_csv = csv

    pokemon_csv = []
    win_csv = []
    loose_csv = []

    ##################################################################################
    # CSV exist
    if path.exists(file_csv):

        csv_file = pd.read_csv(file_csv, header=None)

        for data in range(len(csv_file[0])):
            pokemon_csv.append(csv_file[0][data])
            win_csv.append(csv_file[1][data])
            loose_csv.append(csv_file[2][data])

        for i in range(len(pokemon_csv)):
            if pokemon == pokemon_csv[i]:
                if has_win == "yes":
                    win_csv[i] += 1
                else:
                    loose_csv[i] += 1

        csv_file = {"pokemon": pokemon_csv, "win": win_csv, "loose": loose_csv}
        df = pd.DataFrame(csv_file)
        df.to_csv(file_csv, index=False, header=None)

    ##################################################################################
    # CSV doesn't exist
    if not path.exists(file_csv):
        print("CSV doesn't exist !")


print("Pokemon : ", sys.argv[1])
print("has win ? ", sys.argv[2])

team_stats(csv="qpokemon/team_stats.csv", pokemon=sys.argv[1], has_win=sys.argv[2])
