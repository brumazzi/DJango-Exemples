from django.db import models

# Create your models here.
def list_polls():
    polls = [
        {
            'id': 0,
            'name': 'poll_name',
            'url': 'Url'
        },
        {
            'id': 1,
            'name': 'poll_name',
            'url': 'Url'
        }
    ]
    return polls
