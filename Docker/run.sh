docker build --build-arg ARQUIVO=answer.py --build-arg ENTRADA="1 2" -t projectx/dockerpy .
docker run -it --name dockerpy projectx/dockerpy 
