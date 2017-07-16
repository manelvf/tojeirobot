# -*- coding: UTF-8 -*-
import unittest
import tempfile
import random
import string

from bot import (
    load_phrases_file,
    choose_random_phrase
) 


class TestTojeiro(unittest.TestCase):

    def test_phrases_file_is_loaded(self):
        f = tempfile.NamedTemporaryFile()
        for x in range(3):
            phrase = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
            f.write(phrase + "\n")

        f.seek(0)

        phrases = load_phrases_file(f.name)
        self.assertGreater(len(phrases), 2)

    def test_phrase_is_chosen_randomly(self):
        phrases = []

        for x in range(10):
            phrases.append(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(80)))

        for x in range(10):
            random_phrases = [
                choose_random_phrase(phrases) for f in range(10)]
            
            self.assertTrue(len(set(random_phrases)) > 1)
