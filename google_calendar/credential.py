from google_calendar.environment import CALENDAR_SCOPES

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials as GoogleCredentials
from google_auth_oauthlib.flow import InstalledAppFlow

import os


class Credential:
    def __init__(self, token_path: str, credential_path: str):
        self._token_path = token_path
        self._credential_path = credential_path

        self._credentials = self._define_credentials()
        self._save_token()

    def get(self):
        return self._credentials

    def _define_credentials(self):
        creds = None

        if os.path.exists(self._token_path):
            creds = GoogleCredentials.from_authorized_user_file(
                self._token_path, CALENDAR_SCOPES
            )

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self._credential_path, CALENDAR_SCOPES
                )
                creds = flow.run_local_server(port=0)
        return creds

    def _save_token(self):
        with open(self._token_path, "w") as token:
            token.write(self._credentials.to_json())
