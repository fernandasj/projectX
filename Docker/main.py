import docker
from io import BytesIO
from huey.contrib.djhuey import task
from docker import APIClient

from exams import models as exams

@task()
def build_image(codeFile, inputValues, outputQuestion, answer):
    client = docker.from_env()
    print(client.images.build(path="/home/fernanda/IdeaProjects/projectX/Docker/", rm=True, tag='projectx/image', buildargs={"ARQUIVO":codeFile, "ENTRADA":inputValues}))
    client.containers.run('projectx/image', name="projectx")

    container = client.containers.get('projectx')

    for line in container.logs(stream=True):
    	logContainer = line.strip().decode("utf-8")
    	result = (logContainer == outputQuestion)
    	exams.Answer.objects.filter(pk=answer).update(correct=result)
    	
    container.remove()

def main():

	build_image()	

if __name__ == "__main__":
	main()