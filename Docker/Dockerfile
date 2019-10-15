FROM python:3-alpine
ENV ARQUIVO main_test.py
ENV ENTRADA entrada.txt
ENV SAIDA saida.txt

COPY ${ARQUIVO} main.py
COPY ${ENTRADA} entrada.txt
COPY ${SAIDA} saida.txt

# sh run.sh
# *executar comando 1x*
# RUN ["python", "main.py", "entrada.txt", "saida.txt"]

# python main.py
# *executar comando dinamicamente, ou seja, pode ser modificada 
# em tempo de execução*
CMD ["python", "main.py", "entrada.txt", "saida.txt"]
