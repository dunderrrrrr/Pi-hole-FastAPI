from fastapi import FastAPI
import requests
from settings import url, auth, api_host, api_port
from helpers import build_req

app = FastAPI()


@app.get("/", include_in_schema=False)
def get_paths():
    uri = 'http://{}:{}/openapi.json'.format(api_host, api_port)
    r = requests.get(uri)
    return(r.json()['paths'])


@app.get("/type", tags=['System'])
async def get_type(token):
    r = build_req(url, '?type', token, auth)
    return (r.json())


@app.get("/version", tags=['System'])
def get_version(token):
    r = build_req(url, '?version', token, auth)
    return (r.json())


@app.get("/summary", tags=['Pi-Hole'])
def get_summary(token):
    r = build_req(url, '?summary', token, auth)
    return (r.json())


@app.get("/topItems", tags=['Pi-Hole'])
def top_items(token):
    r = build_req(url, '?topItems', token, auth)
    return (r.json())


@app.get("/getClientNames", tags=['Pi-Hole Clients'])
def top_clients_names(token):
    r = build_req(url, '?getClientNames', token, auth)
    return (r.json())


@app.get("/topClients", tags=['Pi-Hole Clients'])
def top_clients(token):
    r = build_req(url, '?topClients', token, auth)
    return (r.json())


@app.get("/topClientsBlocked", tags=['Pi-Hole Clients'])
def top_clients_blocked(token):
    r = build_req(url, '?topClientsBlocked', token, auth)
    return (r.json())


@app.get("/overTimeData10mins", tags=['Pi-Hole OT'])
def over_time_data_10mins(token):
    r = build_req(url, '?overTimeData10mins', token, auth)
    return (r.json())


@app.get("/overTimeDataQueryTypes", tags=['Pi-Hole OT'])
def over_time_data_query_types(token):
    r = build_req(url, '?overTimeDataQueryTypes', token, auth)
    return (r.json())


@app.get("/overTimeDataClients", tags=['Pi-Hole OT'])
def over_time_data_clients(token):
    r = build_req(url, '?overTimeDataClients', token, auth)
    return (r.json())


@app.get("/getForwardDestinations", tags=['Pi-Hole Fwd Dst'])
def get_forward_dest(token):
    r = build_req(url, '?getForwardDestinations', token, auth)
    return (r.json())


@app.get("/getForwardDestinationNames", tags=['Pi-Hole Fwd Dst'])
def get_fw_dest_names(token):
    r = build_req(url, '?getForwardDestinationNames', token, auth)
    return (r.json())


@app.get("/getQueryTypes", tags=['Pi-Hole'])
def get_query_types(token):
    r = build_req(url, '?getQueryTypes', token, auth)
    return (r.json())


@app.get("/getCacheInfo", tags=['Pi-Hole'])
def get_cache_info(token):
    r = build_req(url, '?getCacheInfo', token, auth)
    return (r.json())


@app.get("/getAllQueries", tags=['Pi-Hole'])
def get_all_queries(token):
    r = build_req(url, '?getAllQueries', token, auth)
    return (r.json())
