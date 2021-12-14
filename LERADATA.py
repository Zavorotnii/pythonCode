import requests
import json

url_LeraDataApi = "https://...................../api.php"
varParams = {
    "token": ".........................",
    "intUserID": ".........................",
    "varGln": ".........................",
    "params": {}
}


# STREAM LERADATA
def streamLeradata(local_file, method, params):
    with requests.post(url_LeraDataApi, stream=True, files={method: (None, json.dumps(params))}) as r:
        r.raise_for_status()
        with open(local_file, "wb") as f:
            for chunk in r.iter_content(chunk_size=1024):
                print(chunk)
                f.write(chunk)
    return local_file


# GET USER MANUAL
def get_s_leradata():
    local_file = "s_leradata.json"
    method = "edi_getDocType"
    params = varParams
    streamLeradata(local_file, method, params)


# GET DOCUMENT FOR PERIOD
def getDocForPeriod():
    local_file = "DocForPeriod.json"
    method = "edi_getDocument"
    params = varParams
    params["params"] = {"docType": "order", "dateFrom": "2021-11-15", "dateTo": "2021-11-15"}
    streamLeradata(local_file, method, params)


# GET STATUS
def getDocForPeriod_STATUS():
    local_file = "DocForPeriodSTATUS.json"
    method = "edi_getStatusDoc"
    params = varParams
    params["params"] = {"docType": "desadv"}
    streamLeradata(local_file, method, params)


# getDocForPeriod()
get_s_leradata()
