from google_calendar.session.credential import Credential
from google_calendar.calendar.event import Event

from googleapiclient.discovery import build
from rich.console import Console
from rich.table import Table

import datetime


class List:
    def __init__(self, type: str):
        credential = Credential().get()
        self._service = build("calendar", "v3", credentials=credential)
        self._type = type

    def run(self):
        console = Console()

        table = Table(show_header=True, header_style="bold magenta", highlight=True)
        table.add_column("Type", justify="center")
        table.add_column("Date", style="dim")
        table.add_column("Hour", style="dim")
        table.add_column("Title")

        events = self.get_current_events()
        for event in events:
            table.add_row("Event", event.date, event.hour, event.title)

        console.print(table)

    def get_current_events(self):
        now = datetime.datetime.now(datetime.timezone.utc).isoformat()

        events_result = (
            self._service.events()
            .list(
                calendarId="primary",
                timeMin=now,
                maxResults=10,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )

        events = []
        for event in events_result.get("items", []):
            date = event["start"].get("dateTime")
            fdate = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")

            title = event["summary"]

            events.append(
                Event(
                    fdate.strftime("%d/%m/%Y"),
                    fdate.strftime("%H:%M:%S"),
                    title,
                )
            )

        if not events:
            events.append(Event("None", "None"))

        return events
