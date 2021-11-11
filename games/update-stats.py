import sys
from os import path
import pandas as pd
import datetime


def stats(csv, winner):
    file_csv = csv
    date_x = datetime.datetime.now()
    date_day = str(date_x.month) + '-' + str(date_x.year)

    ##################################################################################
    # CSV exist
    if path.exists(file_csv):

        csv_file = pd.read_csv(file_csv)
        
        robot_csv = csv_file["robot"].tolist()
        human_csv = csv_file["human"].tolist()
        date_csv = csv_file["date"].tolist()

        test = 0
        for i in range(len(date_csv)):
            if date_day == date_csv[i]:
                if winner == "robot":
                    robot_csv[i] += 1
                else:
                    human_csv[i] += 1
                test = 1

        if test == 0:
            if winner == "robot":
                robot_csv.append(1)
                human_csv.append(0)
            else:
                robot_csv.append(0)
                human_csv.append(1)
            date_csv.append(date_day)

        csv_file = {'robot': robot_csv, 'human': human_csv, 'date': date_csv}
        df = pd.DataFrame(csv_file)
        df.to_csv(file_csv, index=False, header=["robot", "human", "date"])

    ##################################################################################
    # CSV doesn't exist
    if not path.exists(file_csv):
        print("CSV doesn't exist !")

        
if sys.argv[1] == "qpokemon":
  stats(csv="stats/qpokemon_results.csv", winner=sys.argv[2])
if sys.argv[1] == "qnim":
  stats(csv="stats/qnim_results.csv", winner=sys.argv[2])
