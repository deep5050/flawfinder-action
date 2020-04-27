FROM python:3
RUN sudo apt-get install flawfinder
ADD ./src/entrypoint.py /entrypoint.py
ENTRYPOINT ["python", "/entrypoint.py"]
