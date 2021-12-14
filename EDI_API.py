import requests
import json

urlAuth = "https://.........................../Authorize"
data = {
    "varLogin": ".......",
    "varPassword": "......."
}


def authEDI():
    auth = requests.post(urlAuth, json=data)
    varToken = json.loads(auth.text)['varToken']
    token = str(varToken)
    print(varToken)
    # GetDocContent(token)
    GetEdiDocs(token)


def GetEdiDocs(token):
    print(token)
    url = "https://........................../GetEdiDocs"
    getDocsJson = {
        "doc_type": "Order",
        "timefrom": "2021-11-15 00:00:00",
        "timeto": "2021-11-15 23:00:00",
        "limit": 300,
        "varToken": token
    }
    getDocs = requests.post(url, json=getDocsJson)
    print(getDocs.status_code)
    print(getDocs.text)
    js_obj = json.loads(getDocs.text)
    print(len(js_obj['docs']))


def GetDocContent(token):
    print(token)
    url = "https://........................../GetEdiDocBody"
    getDocsContentJson = {
        "intDocID": 3768557,
        "varToken": token
    }
    getContent = requests.post(url, headers={"Accept": "application/xml"}, json=getDocsContentJson)
    print(getContent.text)


authEDI()
