#!/usr/bin/python3
'''
 script that takes in a URL, sends a request to the URL and 
 displays the value of the X-Request-Id
'''


if __name__ == "__main__":

    import sys
    import urllib.request

    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        X_Request_Id = response.getheader('X-Request-Id')
        print(X_Request_Id)
