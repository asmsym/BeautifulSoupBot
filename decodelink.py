import base64
import re
def decodelink(url):

    text = str(url)
    message = re.search("i=.*==$",text)
    print(message.group().replace("i=",""))
    message = message.group().replace("i=","")
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64decode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    print(base64_message)
