import pykiwoom


if __name__ == "__main__":
    km = pykiwoom.KiwoomManager()

    tr_cmd = {
        'rqname': "opt10001",
        'trcode': 'opt10001',
        'next': '0',
        'screen': '1000',
        'input': {
            "종목코드": "005930"
        },
        'output': ['종목코드', '종목명', 'PER', 'PBR']
    }

    km.put_tr(tr_cmd)
    data = km.get_tr()
    print(data)


