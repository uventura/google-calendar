from google_calendar.commands.default import Default
from google_calendar.commands.list import List

import typer

GoogleCalendarCli = typer.Typer()


@GoogleCalendarCli.command()
def default():
    Default().run()


@GoogleCalendarCli.command()
def list(
    type: str = typer.Option(
        "all", help="What calendar information type should be listed"
    )
):
    List(type).run()


def main():
    GoogleCalendarCli()


if __name__ == "__main__":
    main()
