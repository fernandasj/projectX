docker build -t projectx/dockerpy .
docker run -it --name dockerpy projectx/dockerpy -e arquivo=main_text.py -e entrada=entrada.txt -e saida=saida.txt
