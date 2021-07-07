FROM python:3.9.2
RUN pip3 install --upgrade Extre
RUN chmod +x /usr/local/bin/*
RUN wget https://raw.githubusercontent.com/amanpandey7647/ExtremeProUserbot/master/Resources/deploy.sh
RUN sh deploy.sh
WORKDIR /root/amanpandey7647/
CMD ["bash", "Resources/startup.sh"]
