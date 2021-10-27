from torrequest import TorRequest

with TorRequest() as tr:
    response = tr.get('http://ipecho.net/plain')
    print(response.text)  # not your IP address

    tr.reset_identity()

    response = tr.get('http://ipecho.net/plain')
    print(response.text)  # another IP address, not yours
