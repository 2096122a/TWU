from django.test import TestCase

from twu.models import Score

from django.core.urlresolvers import reverse

from datetime import datetime, date

from django.db import models

from django.contrib.auth.models import User

"""
NOTE: We literally only have one model, Score, so we have 3 tests on Score,
      and 5 for views.
"""

class ScoreModelTest(TestCase):

    def test_ensure_score_is_positive(self):

        """
                ensure_score_is_positive should assert True
                for positive scores
        """
        user = User(username="test")
        user.save()
        score = Score(player=user, score=-1, timestamp="2015-01-01")
        score.save()
        print 'Testing for positive score...'

        self.assertEqual((score.score >= 0), True)

    def test_ensure_default_score_is_zero(self):

        """
                ensure_default_score_is_zero should assert True
                for newly instantiated scores
        """
        user = User(username="test")
        user.save()
        score = Score(player=user, timestamp="2015-01-01")
        score.save()
        print 'Testing for a new score...'

        self.assertEqual(score.score, 0)

    def test_ensure_date_is_stored_correctly(self):

        """
                ensure_date_is_stored_correctly should assert True
                for scores with date
        """
        user = User(username="test")
        user.save()
        score = Score(player=user, score=10, timestamp="2015-01-01")
        score.save()
        print 'Testing for date...'

        self.assertEqual(score.timestamp, "2015-01-01")


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
        print "Testing for correct options on index view..."


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
        print "Testing for correct info on the first how to play page..."


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
        print "Testing for correct info on the second how to play page..."


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
        print "Testing for correct info on the third how to play page..."


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
        print "Testing for correct info on the fourth how to play page..."
