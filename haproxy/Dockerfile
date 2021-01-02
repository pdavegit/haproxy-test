FROM haproxy:2.3
RUN apt update && apt install -yqq net-tools tcpdump
COPY haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg

