from rich.console import Console
from rich.table import Table
import pytz


class Timezones:
    def __init__(self):
        self._timezones = self._timezone_representation()

    def run(self):
        console = Console()

        table = Table(
            show_header=True,
            header_style="bold magenta",
        )
        table.add_column("Name")
        table.add_column("Nomenclature")

        for nomenclature, timezone in self._timezones.items():
            table.add_row(timezone, nomenclature)

        console.print(table)

    def get_timezone_name(self, nomenclature):
        return self._timezones.get(nomenclature, "utc")

    def _timezone_representation(self):
        timezones = {}
        for timezone in pytz.all_timezones:
            timezone_code = timezone.lower().split("/")
            if len(timezone_code) > 1:
                timezone_code = timezone_code[0][:3] + "." + timezone_code[-1][:3]
            else:
                timezone_code = timezone_code[0]

            timezones[timezone_code] = timezone
        return timezones
