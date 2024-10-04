from google_calendar.commands.default import Default
from google_calendar.commands.list import List
from google_calendar.commands.calendar_list import CalendarList
from google_calendar.commands.timezones import Timezones

import typer

GoogleCalendarCli = typer.Typer()


@GoogleCalendarCli.command()
def default():
    Default().run()


@GoogleCalendarCli.command()
def list(
    type: str = typer.Option(
        "all", help="What calendar information type should be listed."
    ),
    id: str = typer.Option("primary", help="Which calendar should be listed."),
    timezone: str = typer.Option(
        "utc",
        help="Timezone, you can use 'google-calendar timezones', to check available timezones",
    ),
):
    List(type, id, timezone).run()


@GoogleCalendarCli.command()
def calendar_list():
    CalendarList().run()


@GoogleCalendarCli.command()
def timezones():
    Timezones().run()


def main():
    GoogleCalendarCli()


if __name__ == "__main__":
    main()
