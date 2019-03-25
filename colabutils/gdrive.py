from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import io, os

def search_and_download(filename, local_path):
    drive_service = build('drive', 'v3')
    results = drive_service.files().list(q="name = '" + filename + "'", fields="files(id)").execute()
    google_credential_file = results.get('files', [])
    
    if len(google_credential_file) == 0:
        raise ValueError("[%s] was not found" % filename)
    elif len(google_credential_file) > 1:
        print("warning: search for [%s] returned more %d items, using first" % (filename, len(google_credential_file)))

    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    request = drive_service.files().get_media(fileId=google_credential_file[0]['id'])
    fh = io.FileIO(local_path, 'wb')

    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))

    print("Saved [%s] to [%s]" % (filename, local_path))
    os.chmod(local_path, 600)
    return local_path