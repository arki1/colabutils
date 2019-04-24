import os
import errno
import requests
from google.oauth2 import service_account
from colabutils import gdrive

def load_credentials(url=None, gdrivefile="mlcredential.json", localpath="/content/.google/mlcredential.json"):
  if url is None:
    credentials_localpath = gdrive.search_and_download(
        gdrivefile, localpath, "Credentials loaded successfully")
  else:
    credentials_localpath = localpath

    if not os.path.exists(os.path.dirname(credentials_localpath)):
      try:
        os.makedirs(os.path.dirname(credentials_localpath))
      except OSError as exc:  # Guard against race condition
        if exc.errno != errno.EEXIST:
          raise

    response = requests.get(url, stream=True)
    with open(credentials_localpath, 'wb') as f:
      for chunk in response.iter_content(chunk_size=1024):
        if chunk:
          f.write(chunk)

  return service_account.Credentials.from_service_account_file(
      credentials_localpath)
