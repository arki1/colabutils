# colabutils
Google Colaboratory Python Utilities

## installing

In order to use this package in your Colaboratory Notebook, include this piece of code in the top of your notebook:

```
!pip install colabutils
```

## gdrive.search_and_download

You can use this method to search the current user Google Drive for a specific file and download it to your environment local path. Very useful when your GCP credentials file is shared with the user in his/her google drive.

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

## webcam.take_and_display_photo

Takes a photo using the webcam and saves it in the environment local path. Depends on the user allowing the browser to access the camera. Returns the image content (from a `.read()` on that file).

If no filename parameter is provided, default file name used in the process is photo.jpg.

Example:

```python
from colabutils import webcam
image_content = webcam.take_and_display_photo()
```

## gcp.load_credentials

Tries to look for a file named `mlcredential.json` in the current user's Google Drive. Returns a service account credential object based on this file.

Example:

```python
from colabutils import gcp
creds = gcp.load_credentials()
```

A custom filename can be provided, such as below:

```python
creds = gcp.load_credentials("custom_credential.json")
```

Then just use this in a GCP service client, such as Vision API:

```python
from google.cloud import vision
client = vision.ImageAnnotatorClient(credentials=creds)
```

## sending new versions to PyPI

Make sure you have the latest versions of `setuptools`, `wheel` and `twine` installed:

```
python3 -m pip install --user --upgrade setuptools wheel twine
```

Run this to generate the new version on the `/dist` folder.
```
python3 setup.py sdist bdist_wheel
```

Run this to upload the contents of the `/dist` folder to PyPI.

```
python3 -m twine upload dist/*
```
