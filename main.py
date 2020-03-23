from src.log import Logger
import time
import datetime
import typer
import os
from enum import Enum
import logging

class SessionType(str, Enum):
    workTime = 1
    breakTime = 2

app = typer.Typer()

def countdown(workMinutes: int):
    workSeconds = workMinutes * 60
    while workSeconds > 0:
        print(datetime.timedelta(seconds=workSeconds))
        time.sleep(1)
        workSeconds = workSeconds - 1


def checkNextTurn(workDuration: int, breakDuration: int):

    description = f"""
    What's next? 
    1 for work.
    2 for break. 
    Enter to exit
    """
    option: str = typer.prompt(description, type=SessionType)
    if option == "1":
        workDescription:str = typer.prompt("What do you plan to do?")
        descr:str = f"""
        Started work sessions with {workDuration} minutes.
        TODO:
        {workDescription}
        """
        logging.info(descr)
        countdown(workDuration)
        notify("Section finished", "Work has finished! Ready for next?")
    elif option == "2":
        countdown(breakDuration)
        notify("Section finished", "Break has finished! Ready for next?")
    else:
        print("Have a good time off!")
        exit()


def notify(title, text):
    os.system(
        f"""
              osascript -e 'say \"Finished!\"';
              osascript -e 'display alert "{text}" with title "{title}"'
              """
    )


@app.command()
def scheduler(
    workDuration: int = typer.Option(25, "-w", help="Set work time (minutes)"),
    breakDuration: int = typer.Option(5, "-b", help="Set break time (minutes)"),
):
    while True:
        checkNextTurn(workDuration, breakDuration)

if __name__ == "__main__":
    Logger()
    app()
