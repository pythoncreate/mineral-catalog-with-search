from django.core.urlresolvers import reverse
from django.test import TestCase
import unittest

from .models import Mineral

class MineralViewsTests(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
            name="MineralExample",
            image_filename="mineral.jpg"
        )


    def test_mineral_list_view(self):
        resp = self.client.get(reverse('minerals:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral,resp.context['minerals'])

    def test_mineral_detail_view(self):
        resp = self.client.get(reverse('minerals:detail',
                                       kwargs={'pk': self.mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral,resp.context['mineral'])


if __name__ == '__main__':
    unittest.main()