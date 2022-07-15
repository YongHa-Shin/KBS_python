import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

class oauth2_set:

    def __init__(self, CLIENT_SECRET_FILE, SCOPES):
        self.CLIENT_SECRET_FILE = CLIENT_SECRET_FILE
        self.SCOPES = SCOPES
        self.credentials = None
    
    def local_server_oauth2_set(self):
        # token.pickle stores the user's credentials from previously successful logins
        if os.path.exists('token.pickle'):
            print('Loading Credentials From File...')
            with open('token.pickle', 'rb') as token:
                self.credentials = pickle.load(token)

        # If there are no valid credentials available, then either refresh the token or log in.
        if not self.credentials or not self.credentials.valid:
            if self.credentials and self.credentials.expired and self.credentials.refresh_token:
                print('Refreshing Access Token...')
                self.credentials.refresh(Request())
            else:
                print('Fetching New Tokens...')
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.CLIENT_SECRET_FILE,
                    self.SCOPES
                )

                flow.run_local_server(port=8080, prompt='consent',
                                    authorization_prompt_message='')
                self.credentials = flow.credentials

                # Save the credentials for the next run
                with open('token.pickle', 'wb') as f:
                    print('Saving Credentials for Future Use...')
                    pickle.dump(self.credentials, f)

        print(self.credentials)
        return self.credentials