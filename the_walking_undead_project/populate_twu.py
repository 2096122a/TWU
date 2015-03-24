import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'the_walking_undead_project.settings')

import django
django.setup()

from twu.models import Score
from django.contrib.auth.models import User
from datetime import datetime , date

def populate():
    Bob = add_user(username='Bob',
                         password='Bob',
                         email='bob@gmail.com')

    Richard = add_user(username='Richard',
                         password='Richard',
                         email='richard@gmail.com')

    Michael = add_user(username='Michael',
                         password='Michael',
                         email='Michael@gmail.com')

    Rachel = add_user(username='Rachel',
                         password='Rachel',
                         email='Rachel@gmail.com')

    John = add_user(username='John',
                         password='John',
                         email='John@gmail.com')

    Dumbledore = add_user(username='Dumbledore',
                         password='Dumbledore',
                         email='Dumbledore@gmail.com')

    Hagrid = add_user(username='Hagrid',
                         password='Hagrid',
                         email='Hagrid@gmail.com')

    Tom = add_user(username='Tom',
                         password='Tom',
                         email='Tom@gmail.com')

    Ron = add_user(username='Ron',
                         password='Ron',
                         email='Ron@gmail.com')

    Sam = add_user(username='Sam',
                         password='Sam',
                         email='Sam@gmail.com')

    Tim = add_user(username='Tim',
                         password='Tim',
                         email='Tim@gmail.com')

    Gandalf = add_user(username='Gandalf',
                         password='Gandalf',
                         email='Gandalf@gmail.com')

    Frodo = add_user(username='Frodo',
                         password='Frodo',
                         email='Frodo@gmail.com')

    Aragorn = add_user(username='Aragorn',
                         password='Aragorn',
                         email='Aragorn@gmail.com')

    Legolas = add_user(username='Legolas',
                         password='Legolas',
                         email='Legolas@gmail.com')
    
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

    add_score(player=Boss_user,
              timestamp='2015-03-24', score=236)

    add_score(player=Sophie_user,
              timestamp='2015-03-24', score=98)

    add_score(player=Ivo_user,
              timestamp='2015-03-24', score=130)

    add_score(player=Kenneth_user,
              timestamp='2015-03-24', score=131)

    add_score(player=Ross_user,
              timestamp='2015-03-24', score=999999)

    add_score(player=Ross_user,
              timestamp='2015-03-14', score=999999)

    add_score(player=Legolas,
              timestamp='2015-03-19', score=45)

    add_score(player=Aragorn,
              timestamp='2015-03-19', score=63)

    add_score(player=Frodo,
              timestamp='2015-03-19', score=101)

    add_score(player=Gandalf,
              timestamp='2015-03-19', score=25)

    add_score(player=Tim,
              timestamp='2015-03-19', score=80)

    add_score(player=Ron,
              timestamp=datetime.now(), score=1023)

    add_score(player=Tom,
              timestamp=datetime.now(), score=98)

    add_score(player=Hagrid,
              timestamp=datetime.now(), score=74)

    add_score(player=Dumbledore,
              timestamp=datetime.now(), score=65)

    add_score(player=John,
              timestamp='2015-03-14', score=45)

    add_score(player=Rachel,
              timestamp='2015-03-14', score=102)

    add_score(player=Michael,
              timestamp='2015-03-14', score=74)

    add_score(player=Richard,
              timestamp='2015-03-14', score=32)

    add_score(player=Bob,
              timestamp='2015-03-14', score=541)
    
    add_score(player=Sam, timestamp=datetime.now() ,score=10)

    



def add_score(player, score,timestamp):
    s = Score.objects.get_or_create(player=player,score=score,timestamp=timestamp)[0]
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
