FROM python:3.8
WORKDIR /bot
COPY ./ .
RUN pip install -r requirements.txt
CMD python3 src/main_bot.py