#FROM haproxy:2.3
FROM haproxy:1.8.26
RUN apt update && apt install -yqq net-tools tcpdump
COPY haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg

