from google_calendar.modes.default import Default

import typer

GoogleCalendarCli = typer.Typer()


@GoogleCalendarCli.command()
def default():
    Default().run()


def main():
    GoogleCalendarCli()


if __name__ == "__main__":
    main()
