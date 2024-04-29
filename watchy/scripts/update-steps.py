import sys
from os import path
import pandas as pd


def stats(file_csv: str, hour: str, steps: int):
    steps_csv = [steps]
    hour_csv = [hour]

    ##################################################################################
    # CSV exist
    if path.exists(file_csv):

        csv_file = pd.read_csv(file_csv)
        
        steps_csv = csv_file["steps"].tolist()
        hour_csv = csv_file["hour"].tolist()

        test = 0
        for i in range(len(hour_csv)):
            if str(hour) == str(hour_csv[i]):
                steps_csv[i] += steps
                test = 1

        if test == 0:
            steps_csv.append(steps)
            hour_csv.append(hour)

    csv_file = {'steps': steps_csv, 'hour': hour_csv}
    df = pd.DataFrame(csv_file)
    df.to_csv(file_csv, index=False, header=["steps", "hour"])


##################################################################################
# Launch
if sys.argv[1] == "steps":
    hours_list = sys.argv[3].split(',')
    steps_list = sys.argv[4].split(',')
    for hour, steps in zip(hours_list, steps_list):
        stats(file_csv=f"steps/steps_{sys.argv[2]}.csv", hour=hour, steps=int(steps))
