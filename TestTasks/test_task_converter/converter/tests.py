from django.test import TestCase, Client

class TestView(TestCase):
    c = Client()
    def test_get_view(self):
        response = self.c.get('')
        assert response.status_code == 200

    def test_post_view(self):
        response = self.c.post('', {'USD': 100})
        assert response.status_code == 200
