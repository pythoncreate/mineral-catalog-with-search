from django.core.urlresolvers import reverse
from django.test import TestCase
import unittest


from .models import Mineral

mineral_one = {
               "name": "Allanpringite",
               "category": "Phosphate",
               "formula": "<sub>498</sub>.<sub>07</sub> g",
               "strunz_classification": "08.DC.50",
               "unit_cell": "a = 9.777 Å, b = 7.358 Å, c = 17.83 Å, Z = 4; β = 92.19°",
               "color": "Pale brownish yellow",
               "crystal_symmetry": "Monoclinic – prismatic, H-M symbol (2/m), space group P21/n",
               "cleavage": "{hk0} perfect, {010} good",
               "luster": "Vitreous",
               "streak": "Pale yellowish white",
               "diaphaneity": "Translucent to transparent",
               "group":"Phosphates",
}

mineral_two = {"name": "Ancylite",
               "category": "Carbonate",
               "formula": "Sr(Ce,La)(CO<sub>3</sub>)<sub>2</sub>(OH)·H<sub>2</sub>O",
               "strunz_classification": "05.DC.05",
               "color": "Light yellow, orange-yellow, yellow-brown, grey",
               "cleavage": "None",
               "luster": "Dull",
               "streak": "White",
               "diaphaneity": "Translucent",
}


class MineralViewsTests(TestCase):
    def setUp(self):
        self.mineral_one = Mineral.objects.create(**mineral_one)
        self.mineral_two = Mineral.objects.create(**mineral_two)

    def test_mineral_list_view(self):
        resp = self.client.get(reverse('minerals:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral_one,resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')

    def test_mineral_detail_view(self):
        resp = self.client.get(reverse('minerals:detail',
                                       kwargs={'pk': self.mineral_one.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral_one,resp.context['mineral'])
        self.assertTemplateUsed(resp, 'minerals/mineral_detail.html')

    def test_mineral_letter_search(self):
        resp = self.client.get(
            reverse('minerals:letter', kwargs={'letter': 'a'})
        )
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral_one, resp.context['minerals'])
        self.assertIn(self.mineral_two, resp.context['minerals'])

    def test_mineral_category_search(self):
        resp = self.client.get(
            reverse(
                'minerals:groups',
                kwargs={'group': 'Phosphates'}
            )
        )
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral_one, resp.context['minerals'])
        self.assertNotIn(self.mineral_two, resp.context['minerals'])

    def test_mineral_search_box(self):
        resp = self.client.get(reverse('minerals:search'), {'q': 'ancy'})
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral_two, resp.context['minerals'])

class MineralModelTest(TestCase):
    def test_mineral_created(self):
        mineral = Mineral.objects.create(**mineral_one)
        self.assertEqual(mineral.name, 'Allanpringite')

if __name__ == '__main__':
    unittest.main()