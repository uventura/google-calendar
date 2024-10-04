from google_calendar.session.credential import Credential

import sys


class Default:
    def run(self):
        print(sys.argv[0])

        service = Credential().service()
        print(service)
