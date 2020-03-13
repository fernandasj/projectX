import base64

from huey import crontab
from huey.contrib.djhuey import task

from . import models as exams

from Docker.main import build_image

@task()
def correctionCode(pk):
	head = ''' 
import sys
from unittest.mock import MagicMock

lst = sys.argv[1:]
input = MagicMock(side_effect=lst)
'''

	answer = exams.Answer.objects.get(pk=pk)
	tests_case = exams.CodeAnswer.objects.filter(question_id=answer.question_id)

	decode = base64.b64decode(answer.textAnswer)

	code = open('Docker/' + str(answer.pk) + '.py', 'a')
	code.write(head)
	code.write(decode.decode('utf-8'))
	code.close()
	
	for testcase in tests_case:
		build_image(str(answer.pk) + '.py' , testcase.inputCode, testcase.outputCode, answer.pk)

@task()
def correctionChoice(pk):

	answer = exams.Answer.objects.get(pk=pk)

