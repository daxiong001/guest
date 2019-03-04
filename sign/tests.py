from django.test import TestCase
from sign.models import Event,Guest

# Create your tests here.

class ModelTest(TestCase):

    def setUp(self):
        Event.objects.create(id=1, name="oneplus 3 event", status=True, limit=2000, address='shenzhen', start_time='2016-08-12 02:18:00')

    def test_event_model(self):
        result = Event.objects.get(name='oneplus 3 event')
        self.assertEqual(result.address, "beijing")
        self.assertTrue(result.status)


class IndexPageTest(TestCase):
    '''测试index登陆首页'''

    def test_index_page_renders_index_templates(self):
        response = self.client.get('/index/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')