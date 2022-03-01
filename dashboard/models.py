from django.db import models
import os
from twilio.rest import Client

# Create your models here.
class Message(models.Model):
    name= models.CharField(max_length=100)
    score = models.IntegerField(default=0)

def __str__(self):
    return self.name


def save(self,  *args, **kwargs):
    if self.score >= 70:
        account_sid = os.environ['ACa01b8670650553ebda5923a266648e67']
        auth_token = os.environ['fe69a3cbd14e7778160d75d9ae53da2c']
        client = Client(account_sid, auth_token)

        message = client.messages \
                .create(
                     body="Congratulations {self.name}, your score has been received.",
                     from_='+18623621418',
                     to='+254743880558'
                 )
        


    print(message.sid)
    # return super ().save(args, kwargs)
            
