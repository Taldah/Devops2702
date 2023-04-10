#import requests
import socket
import ssl
import datetime
#response = requests.post("http://127.0.0.1:5001/whatismyname")
#response1 = requests.get('https://https://www.nechama.org.il:443/')

#print(response1)
#actual = "saved new car"
#print(response.text)
domains_url = [
"www.nechama.org.il"
]

def ssl_expiry_datetime(hostname):
    ssl_dateformat = r'%b %d %H:%M:%S %Y %Z'

    context = ssl.create_default_context()
    context.check_hostname = False

    conn = context.wrap_socket(
        socket.socket(socket.AF_INET),
        server_hostname=hostname,
    )
    # 5 second timeout
    conn.settimeout(5.0)

    conn.connect((hostname, 443))
    ssl_info = conn.getpeercert()
    # Python datetime object
    return datetime.datetime.strptime(ssl_info['notAfter'], ssl_dateformat)

if __name__ == "__main__":
    for value in domains_url:
        now = datetime.datetime.now()
        try:
            expire = ssl_expiry_datetime(value)
            diff = expire - now
            print ("Domain name: {} Expiry Date: {} Expiry Day: {}".format(value,expire.strftime("%Y-%m-%d"),diff.days))
        except Exception as e:
            print (e)