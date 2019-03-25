from googleapiclient.discovery import build

def get_range(spreadsheetId, range):
  sheetsService = build('sheets', 'v4')
  ss = sheetsService.spreadsheets()
  response = ss.values().get(
      spreadsheetId=spreadsheetId,
      range=range).execute()

  return response.get('values', [])

def update_cell(spreadsheetId, cell, newValue):
  sheetsService = build('sheets', 'v4')
  ss = sheetsService.spreadsheets()
  return ss.values().update(
      spreadsheetId=spreadsheetId,
      range=cell,
      body={'values': [[newValue]]},
      valueInputOption='USER_ENTERED').execute()
