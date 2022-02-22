from django.test import TestCase
# from my_lib.goods import views


class TestViews(TestCase):

    def test_get_products(self):
        response = self.client.get('/goods/get_products/', {})
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/goods/get_products/', {})
        self.assertEqual(response.status_code, 200)

