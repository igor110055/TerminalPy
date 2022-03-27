FROM ubuntu

RUN apt update && apt upgrade -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y

COPY . /home/TerminalPy

# WORKDIR /home/TerminalPy/ta-lib
# RUN ./configure --prefix=/usr
# RUN make
# RUN make install

WORKDIR /home/TerminalPy



RUN pip install -r requirements.txt

# WORKDIR /var/log/supervisor/
# RUN touch Terminalpy.out.log 
# RUN touch Terminalpy.err.log

# RUN supervisorctl start all

CMD ["python3", "App.py"]


# sudo docker run -t penis/ll
# sudo docker build . -t penis/ll
# sudo docker images

# delete image
# sudo docker rmi <imageid>

# remove all containers
# sudo docker system prune
