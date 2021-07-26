import urllib3


if __name__ == '__main__':
    http = urllib3.PoolManager()

    # first send 10 post request

    resp = http.request('POST', "http://127.0.0.1:5000/persons?name=tal&features=[6,9,6]")
    print(resp.data.decode('utf-8'))

    resp = http.request('POST', "http://127.0.0.1:5000/persons?name=lior&features=[1,3,4]")
    print(resp.data.decode('utf-8'))

    resp = http.request('POST', "http://127.0.0.1:5000/persons?name=noa&features=[1,2,3]")
    print(resp.data.decode('utf-8'))

    resp = http.request('POST', "http://127.0.0.1:5000/persons?name=efi&features=[1,7,7]")
    print(resp.data.decode('utf-8'))

    resp = http.request('POST', "http://127.0.0.1:5000/persons?name=david&features=[9,9,9]")
    print(resp.data.decode('utf-8'))

    resp = http.request('POST', "http://127.0.0.1:5000/persons?name=dor&features=[8,1,4]")
    print(resp.data.decode('utf-8'))

    resp = http.request('POST', "http://127.0.0.1:5000/persons?name=linoy&features=[8,7,6]")
    print(resp.data.decode('utf-8'))

    resp = http.request('POST', "http://127.0.0.1:5000/persons?name=ido&features=[3,5,1]")
    print(resp.data.decode('utf-8'))

    resp = http.request('POST', "http://127.0.0.1:5000/persons?name=noga&features=[2,2,2]")
    print(resp.data.decode('utf-8'))

    resp = http.request('POST', "http://127.0.0.1:5000/persons?name=erez&features=[6,8,3]")
    print(resp.data.decode('utf-8'))