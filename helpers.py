import requests


def build_req(url, type, token, auth):
    if auth['enabled']:
        try:
            r = requests.get(
                url + type + "&auth=" + token,
                auth=(auth['usr'], auth['passwd'])
            )
            return(r)
        except Exception as E:
            print(E)
    else:
        try:
            r = requests.get(
                url + type + "&auth=" + token
            )
            return(r)
        except Exception as E:
            print(E)
