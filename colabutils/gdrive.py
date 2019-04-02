from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import io, os
import zipfile

def search_and_download(filename, local_path, custom_message=""):
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
    os.chmod(local_path, 600)

    if (custom_message!=""):
        print(custom_message)
    else:
        print("Saved [%s] to [%s]" % (filename, local_path))

    return local_path


def download_and_unzip(filename, path_to):
    if not path_to.endswith("/"):
        path_to = path_to + "/"

    localfile = search_and_download(filename, path_to + filename)

    zip_ref = zipfile.ZipFile(localfile, 'r')
    zip_ref.extractall()
    zip_ref.close()

    os.remove(localfile)

    return path_to
