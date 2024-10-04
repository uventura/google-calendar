from google_calendar.session.credential import Credential

from googleapiclient.discovery import build
from rich.console import Console
from rich.table import Table


class CalendarList:
    def __init__(self):
        credential = Credential().get()
        self._service = build("calendar", "v3", credentials=credential)

    def run(self):
        console = Console()

        table = Table(show_header=True, header_style="bold magenta", highlight=True)
        table.add_column("Id", justify="center")
        table.add_column("Summary", justify="center")
        table.add_column("Primary", justify="center")

        calendars_result = (
            self._service.calendarList()
            .list(
                maxResults=10,
                showHidden=True,
            )
            .execute()
        )

        for calendar in calendars_result.get("items"):
            primary = "Yes" if calendar.get("primary") else "No"
            table.add_row(calendar.get("id"), calendar.get("summary"), primary)

        if not calendars_result.get("items"):
            table.add_row("None", "None", "None")

        console.print(table)
