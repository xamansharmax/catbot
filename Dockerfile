FROM sandy1709/catuserbot:slim-buster

#clonning repo 
RUN git clone https://github.com/beastzx18/catuserbot.git /root/userbot

#working directory 
WORKDIR /root/userbot

# Install requirements
RUN pip3 install -r requirements.txt

ENV PATH="/home/userbot/bin:$PATH"

# running command
CMD ["python3","-m","userbot"]
