from django.db import models

class DataItem(models.Model):

    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 30)

    def __str__(self):
        return str(self.file_name) + ' ' + str(self.file_name)
