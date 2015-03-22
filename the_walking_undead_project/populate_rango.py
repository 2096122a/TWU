import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'the_walking_undead_project.settings')

import django
django.setup()

from twu.models import Score
from django.contrib.auth.models import User


def populate():
    Ross_user = add_user(username='Ross',
                         password='Ross',
                         email='Ross@gmail.com')

    Kenneth_user = add_user(username='Kenneth',
                         password='Kenneth',
                         email='Kenneth@gmail.com')

    Ivo_user = add_user(username='Ivo',
                         password='Ivo',
                         email='Ivo@gmail.com')

    Sophie_user = add_user(username='Sophie',
                         password='Sophie',
                         email='Sophie@gmail.com')

    test_user = add_user(username='test',
                         password='test',
                         email='test@gmail.com')

    Boss_user = add_user(username='Boss',
                         password='Boss',
                         email='Boss@gmail.com')

    add_score(player=test_user,
              timestamp='2015-03-14 05:24:42', score=100)



def add_score(player, score ,timestamp):
    s = Score.objects.get_or_create(player=player, timestamp=timestamp,score=score)[0]
    return s

def add_user(username, password , email):
    user, created = User.objects.get_or_create(username=username,email=email)
    user.set_password(password)

    user.save()
    return user

# Start execution here!
if __name__ == '__main__':
    print "Starting TWU population script..."
    populate()