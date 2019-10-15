docker build -t projectx/dockerpy .
docker run -it --name dockerpy projectx/dockerpy -e ARQUIVO=main_text.py -e ENTRADA=entrada.txt -e SAIDA=saida.txt
