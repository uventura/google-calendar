from google_calendar.session.environment import CALENDAR_SCOPES
import google_calendar.session.cache as cache

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials as GoogleCredentials
from google_auth_oauthlib.flow import InstalledAppFlow

from pathlib import Path


class Credential:
    def __init__(self):
        self._token_path = cache.cache_path() / "token.json"
        self._credentials = self._define_credential()

    def get(self):
        return self._credentials

    def _define_credential(self):
        credential = None
        if not self._token_path.exists():
            credential = self._create_credential()
            self._save_token(credential.to_json())
        else:
            credential = GoogleCredentials.from_authorized_user_file(
                self._token_path, CALENDAR_SCOPES
            )

        if credential and credential.expired and credential.refresh_token:
            credential.refresh(Request())

        return credential

    def _create_credential(self):
        credential_path = Path(input("Provide the 'credential.json' file path: "))
        if not credential_path.exists():
            print(f"The path '{credential_path.resolve()}' doesn't exist.")
            exit(-1)

        flow = InstalledAppFlow.from_client_secrets_file(
            credential_path.resolve(), CALENDAR_SCOPES
        )
        return flow.run_local_server(port=0)

    def _save_token(self, credential):
        with open(self._token_path, "w") as token:
            token.write(credential)
