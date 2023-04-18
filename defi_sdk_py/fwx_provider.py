import web3

class FwxAsyncHTTPProvider(web3.AsyncHTTPProvider):
    pass

class FwxWebsocketProvider(web3.WebsocketProvider):
    pass

def getProvider(url,type):
    if type == 'http':
        return [FwxAsyncHTTPProvider(url), web3.AsyncHTTPProvider(url)]
    elif type == 'wss':
        return [FwxAsyncHTTPProvider(url), web3.WebsocketProvider(url)]
    return []
