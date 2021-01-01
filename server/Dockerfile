FROM python
RUN pip install requests flask uwsgi
WORKDIR /usr/app
COPY server.py .
#CMD python server.py
CMD /usr/local/bin/uwsgi --uid nobody --need-app --file /usr/app/server.py --http 0.0.0.0:8081 --callable app --processes 2 -M --http-timeout 600