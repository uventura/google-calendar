from google_calendar.session.credential import Credential

from googleapiclient.discovery import build
import sys


class Default:
    def run(self):
        print(sys.argv[0])

        credentials = Credential().get()
        service = build("calendar", "v3", credentials=credentials)
        print(service)
