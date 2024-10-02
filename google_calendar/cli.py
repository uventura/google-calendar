from google_calendar.credential import Credential
from googleapiclient.discovery import build

import typer

GoogleCalendarCli = typer.Typer()

@GoogleCalendarCli.command()
def basic_mode(token_path: str = "token.json", credential_path: str = "credentials.json"):
    """
    Command executed for the main Google Calendar process.

    Args:
        token_path(str): The path for the token.json file.
        credential_path(str): The path for the credential.json file.
    """

    credentials = Credential(token_path, credential_path).get()
    service = build("calendar", "v3", credentials=credentials)
    print(service)