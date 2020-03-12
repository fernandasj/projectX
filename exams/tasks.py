import base64

from huey import crontab
from huey.contrib.djhuey import task

from . import models as exams

from Docker.main import build_image

@task()
def correctionCode(pk):
	# head = str.encode("aW1wb3J0IHN5cwpmcm9tIHVuaXR0ZXN0Lm1vY2sgaW1wb3J0IE1hZ2ljTW9jawoKbHN0ID0gc3lzLmFyZ3ZbMTpdCmlucHV0ID0gTWFnaWNNb2NrKHNpZGVfZWZmZWN0PWxzdCk=")
	answer = exams.Answer.objects.get(pk=pk)
	tests_case = exams.CodeAnswer.objects.filter(question_id=answer.question_id)

	decode = base64.b64decode(answer.textAnswer)
	# headFile = base64.b64decode(str(head))

	code = open('Docker/' + str(answer.pk) + '.py', 'a')
	# code.write(decode.headFile('utf-8'))
	code.write(decode.decode('utf-8'))
	code.close()
	
	for testcase in tests_case:
		build_image(str(answer.pk) + '.py' , testcase.inputCode, testcase.outputCode, answer.pk)

@task()
def correctionChoice(pk):

	answer = exams.Answer.objects.get(pk=pk)

