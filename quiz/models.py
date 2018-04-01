from django.db import models

# Create your models here.	
class Level(models.Model):

	MAYBECHOICE = {
		(0, 1),
		(1, 2),
		(2, 3),
	}
	level_number = models.IntegerField(choices=MAYBECHOICE, unique=True, default=0)
	level_name = models.CharField(max_length=200)
	def __str__(self):
		return self.level_name
   


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    level = models.ForeignKey(Level, on_delete=models.CASCADE, to_field='level_number', default=1)

    def __str__(self):
    	return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
    	return self.answer_text


class User(models.Model):
	name = models.CharField(max_length=200)
	surname = models.CharField(max_length=200)
	role = models.CharField(max_length=200)


class Test(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateTimeField('date published')


class TestQuestion(models.Model):
	test_id = models.ForeignKey(Test, on_delete=models.CASCADE)
	question_id = models.ForeignKey(Question, on_delete=models.CASCADE)


class UserAnswer(models.Model):
	question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
	user_answer = models.ForeignKey(Answer)

