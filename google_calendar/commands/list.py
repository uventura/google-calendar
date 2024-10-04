from google_calendar.session.credential import Credential
from google_calendar.calendar.event import Event
from google_calendar.commands.timezones import Timezones

from rich.console import Console
from rich.table import Table
import pytz

import datetime


class List:
    def __init__(self, type: str, id: str, timezone: str):
        self._service = Credential().service()
        self._type = type
        self._id = id
        self._timezone = pytz.timezone(Timezones().get_timezone_name(timezone))

    def run(self):
        console = Console()

        table = Table(
            show_header=True,
            header_style="bold magenta",
            highlight=True,
            show_lines=True,
            show_edge=True,
        )
        table.add_column("Type", justify="center")
        table.add_column("Date", style="dim")
        table.add_column("Hour", style="dim")
        table.add_column("Title")
        table.add_column("Description", max_width=30)
        table.add_column("Link", overflow="fold")

        events = self.get_current_events()
        for event in events:
            table.add_row(
                "Event",
                event.date,
                event.hour,
                event.title,
                event.description,
                f"[link={event.link}]link[/link]",
            )

        console.print(table)

    def get_current_events(self):
        now = datetime.datetime.now(datetime.timezone.utc).isoformat()

        events_result = (
            self._service.events()
            .list(
                calendarId=self._id,
                timeMin=now,
                maxResults=10,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )

        events = []
        for event in events_result.get("items", []):
            date = self._get_date(event)
            fdate = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
            fdate = fdate.astimezone(self._timezone)

            title = event.get("summary", "")
            description = event.get("description", "No description provided.")
            link = event.get("htmlLink", "None")

            events.append(
                Event(
                    fdate.strftime("%d/%m/%Y"),
                    fdate.strftime("%H:%M:%S"),
                    title,
                    description,
                    link,
                )
            )

        if not events:
            events.append(Event("None", "None", "None", "None", "None"))

        return events

    def _get_date(self, event):
        date = event["start"].get("dateTime", None)
        if not date:
            date = event["end"].get("date", "")
            return date + "T00:00:00Z"
        return date
