from django.test import TestCase

from twu.models import Score

from django.core.urlresolvers import reverse

from datetime import datetime, date

from django.db import models

from django.contrib.auth.models import User

"""
NOTE: We literally only have one model, Score, so instead of
      3 redundant tests for models, we've done 1 test for Score
      and 5 for views.
"""


def add_cat(player, score, timestamp):
    user = User.objects.get(id=player)
    c.score = score
    c.timestamp = timestamp
    c.save()
    return c

class ScoreModelTest(TestCase):

    def test_ensure_score_is_positive(self):

        """
                ensure_score_is_positive should assert True
                for positive scores
        """
        user = User.objects.get(id=player)
        cat = Score(player=user, score=-1, timestamp="2015-01-01")
        cat.save()
        print 'views', cat.score

        self.assertEqual((cat.score >= 0), True)


class IndexViewTests(TestCase):

    def test_index_shows_menu_options(self):
        """
        Checks that the index page has the correct options displayed.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "How To Play")
        self.assertContains(response, "Scoreboard")
        self.assertContains(response, "Log In To Play")


class Howto1ViewTests(TestCase):

    def test_content_of_howto1(self):
        """
        Checks that the Howto1 page is outputting the correct content.
        """
        response = self.client.get(reverse('howto1'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "These are your Life Points")
        self.assertContains(response, "Bullets are needed to use your gun.")
        self.assertContains(response, "Roll 2+ to hit")


class Howto2ViewTests(TestCase):

    def test_content_of_howto2(self):
        """
        Checks that the Howto2 page is outputting the correct content.
        """
        response = self.client.get(reverse('howto2'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This is the map.")
        self.assertContains(response, "the map tile has not yet been explored")
        self.assertContains(response, "Here you can see your current score.")


class Howto3ViewTests(TestCase):

    def test_content_of_howto3(self):
        """
        Checks that the Howto3 page is outputting the correct content.
        """
        response = self.client.get(reverse('howto3'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "These are your Life Points")
        self.assertContains(response, "Bullets are needed to use your gun.")
        self.assertContains(response, "Roll 2+ to hit")


class Howto4ViewTests(TestCase):

    def test_content_of_howto4(self):
        """
        Checks that the Howto4 page is outputting the correct content.
        """
        response = self.client.get(reverse('howto4'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This is the map.")
        self.assertContains(response, "the map tile has not yet been explored")
        self.assertContains(response, "Here you can see your current score.")

