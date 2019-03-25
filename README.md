# colabutils
Google Colaboratory Python Utilities

## installing

```
!pip install colabutils
```

## gdrive.search_and_download

You can use this method to search the current user Google Drive for a specific file and download it to your environment local path.

Example:

```python
from colabutils import gdrive

credential_path = gdrive.search_and_download 'credential.json', '/content/.google/credential.json'
```

Note: the file doesn't need to be on the current user `My Drive` section or even the user doesn't need to be the file owner. If the file is owned by another user, but was shared with the current user, it will work all the same.

So, with the example above you could do something like that:

```python
# authenticates the colab environment with current user's credentials
from google.colab import auth
auth.authenticate_user()

# download GCP API credentials from Google Drive
from colabutils import gdrive
credential_path = gdrive.search_and_download 'credential.json', '/content/.google/credential.json'

# load credentials
from google.oauth2 import service_account
creds = service_account.Credentials.from_service_account_file(credential_path)

# use credentials to prepare a GCP service client
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
client = language.LanguageServiceClient(credentials=creds)

# make a call to the NLP API
text = u'I love python!'
document = types.Document(content=text,type=enums.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(document=document).document_sentiment

print('Text: {}'.format(text))
print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))

# output:
# Text: I love python!
# Sentiment: 0.8999999761581421, 0.8999999761581421
```
