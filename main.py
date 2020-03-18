import time
import datetime
import argparse 
import os

def setParameters():
    parser = argparse.ArgumentParser()
    parser.add_argument("-w","--workDuration", help="Set work time (minutes)", default=60, type=int)
    parser.add_argument("-b","--breakDuration", help="Set break time (minutes)", default =5, type=int)
    args = parser.parse_args()

    return args.workDuration, args.breakDuration
    

def countdown(workMinutes: int):
    workSeconds = workMinutes * 60
    while(workSeconds > 0):
        print(datetime.timedelta(seconds=workSeconds))
        time.sleep(1)
        workSeconds = workSeconds -1

def checkNextTurn(workDuration: int, breakDuration: int):
    
    description = f"""
    "What's next? 
    1 for work.
    2 for break. 
    Enter to exit"
    """
    option:str = input(description)
    if option == "1":
        countdown(workDuration)
        notify("Section finished", "Work has finished! Ready for next?")
    elif option == "2":
        countdown(breakDuration)
        notify("Section finished", "Break has finished! Ready for next?")
    else:
        print("Have a good time off!")
        exit()


def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))
    os.system("osascript -e 'say \"Finished!\"'")


workDuration, breakDuration = setParameters()
while(True):

    checkNextTurn(workDuration, breakDuration)