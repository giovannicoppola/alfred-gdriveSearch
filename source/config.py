# CONFIG file for the gDrive search workflow

import os
import sys


CREDENTIALS_PATH = os.path.expanduser(os.getenv('KEYFILE'))



iconDict = {
    "application/vnd.google-apps.document": "icons/docs.png",
    "application/vnd.google-apps.spreadsheet": "icons/sheets.png",
    "application/pdf": "icons/pdf.png",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document": "icons/word.png",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": "icons/excel.png",
    "application/vnd.google-apps.presentation": "icons/googlePres.png",
    "application/vnd.google-apps.folder": "icons/folder.png",
    "application/vnd.google-apps.unknown": "icons/unknown.png",
    "image/jpeg": "icons/jpg.png"
}



def createMIMEquery():
    GDOC_CHECK = os.path.expanduser(os.getenv('GDOC_CHECK'))
    GSHEET_CHECK = os.path.expanduser(os.getenv('GSHEET_CHECK'))
    GPRES_CHECK = os.path.expanduser(os.getenv('GPRES_CHECK'))
    PDF_CHECK = os.path.expanduser(os.getenv('PDF_CHECK'))
    MSWORD_CHECK = os.path.expanduser(os.getenv('MSWORD_CHECK'))
    MSEXCEL_CHECK = os.path.expanduser(os.getenv('MSEXCEL_CHECK'))
    JPG_CHECK = os.path.expanduser(os.getenv('JPG_CHECK'))


    
    mime_types = []
    if GDOC_CHECK == "1":
        mime_types.append('application/vnd.google-apps.document')
    if GSHEET_CHECK == "1":
        mime_types.append('application/vnd.google-apps.spreadsheet')
    if GPRES_CHECK == "1":
        mime_types.append('application/vnd.google-apps.presentation')
    if PDF_CHECK == "1":
        mime_types.append('application/pdf')
    if MSWORD_CHECK == "1":
        mime_types.append('application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    if MSEXCEL_CHECK == "1":
        mime_types.append('application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    if JPG_CHECK == "1":
        mime_types.append('image/jpeg')





    # Create the query for MIME types
    mime_type_query = " or ".join([f"mimeType='{mime_type}'" for mime_type in mime_types])

    

    return mime_type_query


def log(s, *args):
    if args:
        s = s % args
    print(s, file=sys.stderr)


