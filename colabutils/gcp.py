from google.oauth2 import service_account
from colabutils import gdrive

def load_credentials(gdrivefile="mlcredential.json", localpath="/content/.google/mlcredential.json"):
  credentials_localpath = gdrive.search_and_download(
      gdrivefile, localpath)

  return service_account.Credentials.from_service_account_file(
    credentials_localpath)
