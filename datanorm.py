import os
import sys
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def upload_to_drive(filename, credentials, token):
    creds = Credentials.from_authorized_user(token)
    service = build('drive', 'v3', credentials=creds)

    media = MediaFileUpload(filename, mimetype='text/plain')
    file_metadata = {'name': os.path.basename(filename)}
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(f"Uploaded {filename} to Google Drive with ID {file.get('id')}")

if __name__ == "__main__":
    # GitHub Actionsのログファイルのパスを指定
    log_file_path = "path_to_your_log_file.log"

    credentials = os.environ.get("CREDENTIALS")
    token = os.environ.get("TOKEN")

    if not credentials or not token:
        print("Credentials or token not provided.")
        sys.exit(1)

    upload_to_drive(log_file_path, credentials, token)
