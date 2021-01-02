#!/bin/bash
docker exec -u root -it haproxy-test_haproxy_1 tcpdump -vv -i eth0 -nn -X tcp
