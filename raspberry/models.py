from django.db import models

# Create your models here.
class detail(models.Model):

	# 时间
	time = models.DateTimeField()

	# 湿度值
	humidity = models.FloatField()

	# 温度值
	temperature = models.FloatField()
	
	# 风扇是否在转
	is_pan_turn =  models.BooleanField()


	def __str__(self):
		return "Raspberry's detail"
