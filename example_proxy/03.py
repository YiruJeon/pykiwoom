from pykiwoom.kiwoom import *

if __name__ == "__main__":
    proxy = KiwoomProxy()
    
    data = proxy.fetch(func="GetMasterCodeName", params=["005930"])
    print(data)

