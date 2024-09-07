from django.db import models

class Client(models.Model):
    class Meta:
        ...
    
    name = models.CharField(max_length = 50,
                            null = False,
                            blank = False,
                            )
    phone = models.CharField(max_length = 50,
                             null = False,
                             blank = False,
                             )
    agreement = models.BooleanField(default = False,
                                    )
    send = models.BooleanField(default = True)