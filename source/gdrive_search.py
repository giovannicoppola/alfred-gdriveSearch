# Authenticate and build the service
from googleapiclient.discovery import build
from google.oauth2 import service_account
import sys
import json
from time import time
from config import log, iconDict, createMIMEquery, CREDENTIALS_PATH

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

credentials = service_account.Credentials.from_service_account_file(
    CREDENTIALS_PATH, scopes=SCOPES)
drive_service = build('drive', 'v3', credentials=credentials)

MY_INPUT = sys.argv[1]

    


# Function to search for text in Google Drive documents
def search_text_in_drive(search_string, resultObj):
    mime_type_query = createMIMEquery()
    # Split the search string into individual terms
    search_terms = [term.strip() for term in search_string.split(" ")]
    
    # Construct the search terms section outside the f-string
    search_terms_query = " and ".join([f"fullText contains '{term}'" for term in search_terms])

    # Construct the query to search for all terms (AND logic)
    query = f"({search_terms_query}) and ({mime_type_query})"
    

    results = drive_service.files().list(q=query, fields="files(id, name,webViewLink,mimeType)").execute()
    items = results.get('files', [])
    if not items:
        
        resultObj["items"].append({
            "title": f"No documents found containing '{search_string}'.",
            'subtitle': "Try another search!"
             
                }) 
    else:
        totResults = len(items)
        resultCount = 0
        for item in items:
            resultCount += 1
            resultObj["items"].append({
            "title": item['name'],
            'subtitle': f"{resultCount}/{totResults} ↩️ to open in browser, ⌘ to copy file name to clipboard",
            'valid': True,
            'mods': {
                    
                "cmd": {
                    "valid": True,
                    "arg": item['name'],
                    "subtitle": "Copy file name to clipboard"
                        }
                
                },
            'icon': {
                "path": iconDict.get(item['mimeType'], "icons/unknown.png")
            },
            'arg': item['webViewLink']
            })
    return resultObj
            




def main():
    main_start_time = time()
    result = {"items": []}
    # Search for specific text in Google Drive documents
    search_string = MY_INPUT
    if len(search_string) > 2:
        result = search_text_in_drive(MY_INPUT,result)

    
    else:
        result["items"].append({
            "title": "Please enter at least 3 characters",
            'subtitle': "3️⃣"
             
                }) 
    print (json.dumps(result))
    main_timeElapsed = time() - main_start_time
    log(f"\nscript duration: {round (main_timeElapsed,3)} seconds")

if __name__ == '__main__':
    main()
    
