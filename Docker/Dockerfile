FROM python:3-alpine
ENV ARQUIVO main_test.py
ENV ENTRADA entrada.txt
ENV SAIDA saida.txt

COPY ${ARQUIVO} main.py
COPY ${ENTRADA} entrada.txt
COPY ${SAIDA} saida.txt

CMD ["python", "main.py", "entrada.txt", "saida.txt"]
