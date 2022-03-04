import pykiwoom


if __name__ == "__main__":
    km = pykiwoom.KiwoomManager()

    tr_cmd = {
        'rqname': "opt10081",
        'trcode': 'opt10081',
        'next': '0',
        'screen': '1000',
        'input': {
            "종목코드": "005930",
            "기준일자": "20200424",
            "수정주가구분": "",
        },
        'output': ["일자", "시가", "고가", "저가", "현재가"]
    }

    for i in range(2):
        if i != 0:
            tr_cmd['next'] = '2'
        
        km.put_tr(tr_cmd)
        data = km.get_tr()
        print(data)
