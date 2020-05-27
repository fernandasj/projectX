class QuestionAnswer(object):
    def __init__(self, headQuestion, typeQuestion, correctAnswer):
        self.headQuestion = headQuestion
        self.typeQuestion = typeQuestion
        self.correctAnswer = correctAnswer
    
    def __str__(self):
        # basta isso :D
        return self.headQuestion + " " + self.correctAnswer


class TestResult(object):
    def __init__(self, idTest, name, discipline, questions, scores, student):
        self.idTest = idTest
        self.name = name
        self.discipline = discipline
        self.questions = questions
        self.scores = scores
        self.student = student