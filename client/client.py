import requests
import logging
import time
logging.basicConfig(level=logging.INFO)
log = logging.getLogger('urllib3')
log.setLevel(logging.DEBUG)
i = 0
time.sleep(5)
while True:
    r = requests.get("http://haproxy/message/{}/{}".format(i*60, 32*1024*1024))
    logging.info('%s %d', r, len(r.text))
    r.raise_for_status()
    i = i + 1
