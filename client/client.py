import requests
import logging
import time
logging.basicConfig(level=logging.INFO)
log = logging.getLogger('urllib3')
log.setLevel(logging.DEBUG)
m = 10
time.sleep(30)
while True:
    r = requests.get("http://haproxy/message/{}/{}".format(m*60, 32))
    logging.info('%s %d', r, len(r.text))
    r.raise_for_status()
    m = m + 10
