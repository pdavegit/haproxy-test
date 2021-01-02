#!/bin/bash
# docker exec -u root -it haproxy-test_haproxy_1 tcpdump -K -vv -i eth0 -nn -X tcp
docker run --rm -it --net container:haproxy-test_haproxy_1 nicolaka/netshoot tcpdump -K -i eth0 -nn -vv -X tcp
