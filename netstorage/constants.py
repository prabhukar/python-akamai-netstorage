
## Proxies
fiddlerproxy = { # for capturing data going via Fiddler
                "http": "http://localhost:8888",
                "https": "http://localhost:8888",
            }
proxy = { # Internet Facing proxies
                "http": "https://<proxyname>:<port>",
                "https": "https://<proxyname>:<port>",
            }
proxydirect = { # direct proxy for connecting directly
                "http": "",
                "https": "",
            }
            
            
AKAMAI_HOST_POSTFIX = '-nsu.akamaihd.net'
AKAMAI_AUTH_VERSION = 5
AKAMAI_PROTOCOL_VERSION = 1
