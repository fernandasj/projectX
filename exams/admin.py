from django.contrib import admin
from .models import Test, Question, CodeAnswer, Choice, Answer, Discipline, TestStudent

# =====================
# TestAdmin
# =====================
class TestAdmin(admin.ModelAdmin):
    list_display = ('idTest', 'aplicationDate', 'name', 'get_questions')

admin.site.register(Test, TestAdmin)


# ======================
# QuestionAdmin
# ======================
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('idQuestion', 'headQuestion', 'typeQuestion')

admin.site.register(Question, QuestionAdmin)


# ======================
# CodeAnswerAdmin
# ======================
class CodeAnswerAdmin(admin.ModelAdmin):
    list_display = ('idCodeAnswer', 'question', 'inputCode', 'outputCode')

admin.site.register(CodeAnswer, CodeAnswerAdmin)


# ======================
# ChoiceAdmin
# ======================
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('idChoice', 'question', 'textChoice')

admin.site.register(Choice, ChoiceAdmin)


# ======================
# AnswerAdmin
# ======================
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('idAnswer', 'correct','test', 'question')

admin.site.register(Answer, AnswerAdmin)


# ======================
# Discipline
# ======================
class DisciplineAdmin(admin.ModelAdmin):
    list_display = ('idDiscipline', 'name', 'teacher', 'get_students')

admin.site.register(Discipline, DisciplineAdmin)


# ===============================
# TestStudentAdmin
# ===============================
class TestStudentAdmin(admin.ModelAdmin):
    list_display = ('idTestStudent', 'test', 'student', 'scores', 'timeStart',
        'timeFinish')

admin.site.register(TestStudent, TestStudentAdmin)
