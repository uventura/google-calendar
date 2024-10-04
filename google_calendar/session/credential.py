from google_calendar.environment.constants import CALENDAR_SCOPES
from google_calendar.environment.logger import Logger
import google_calendar.session.cache as cache

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials as GoogleCredentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from pathlib import Path


class Credential:
    def __init__(self):
        self._logger = Logger()
        self._token_path = cache.cache_path() / "token.json"
        self._credentials = self._define_credential()

    def get(self):
        return self._credentials

    def service(self, type="calendar", version="v3"):
        return build(type, version, credentials=self._credentials)

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
            self._logger.error(f"The path '{credential_path.resolve()}' doesn't exist.")
            exit(-1)

        flow = InstalledAppFlow.from_client_secrets_file(
            credential_path.resolve(), CALENDAR_SCOPES
        )
        return flow.run_local_server(port=0)

    def _save_token(self, credential):
        cache.save_cache_file("token.json", credential)
