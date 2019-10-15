import docker
from io import BytesIO
from docker import APIClient

def build_image():

    client = docker.from_env()
    print(client.images.build(path="../Docker", rm=True, tag='projectx/image'))
    print(client.containers.run('projectx/image', environment=["ARQUIVO=main_test.py", "ENTRADA=entrada.txt", "SAIDA=saida.txt"]))

def main():

	build_image()	

if __name__ == "__main__":
	main()
