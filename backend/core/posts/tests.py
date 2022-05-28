from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Post



class CheckPostAPI(APITestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.post_data = {
            'title': 'First post',
            'beginning': 'beginning text section, beginning text section, beginning text section',
            'main_picture': 'Image/1/2/3/4/5/6.png',
            'main_text': 'main text section, main text section, main text section, main text section',
        }
        Post.objects.create(
            title=self.post_data['title'],
            beginning=self.post_data['beginning'],
            main_picture=self.post_data['main_picture'],
            main_text=self.post_data['main_text']
            )

    def test_list_status(self):
        url = '/api/posts/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_first_post_status_without_data(self):
        url = '/api/posts/2'
        response = self.client.get(url, follow=True, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual('Nie znaleziono.', str(response.data['detail']))

    def test__first_post_status_with_data(self):
        url = '/api/posts/1'
        response = self.client.get(url, follow=True, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_check_data_first_post(self):
        url = '/api/posts/1'
        response = self.client.get(url, follow=True, format='json')
        details = response.data
        self.assertEqual(details['id'], 1)
        self.assertEqual(details['title'], self.post_data['title'])
        self.assertEqual(details['beginning'], self.post_data['beginning'])
        self.assertEqual(details['main_picture'], 'http://testserver/media/' + self.post_data['main_picture'])
        self.assertEqual(details['main_text'], self.post_data['main_text'])

    def test_check_list_requests_method(self):
        url = '/api/posts/'
        response = self.client.get(url, follow=True)
        self.assertEqual(response.request['PATH_INFO'], url)
        self.assertEqual(response.request['REQUEST_METHOD'], 'GET')
        self.assertNotEqual(response.request['REQUEST_METHOD'], 'POST')
        self.assertNotEqual(response.request['REQUEST_METHOD'], 'PUT')

    def test_check__requests_method_for_post(self):
        url = '/api/posts/1/'
        response = self.client.get(url, follow=True)
        self.assertEqual(response.request['PATH_INFO'], url)
        self.assertEqual(response.request['REQUEST_METHOD'], 'GET')
        self.assertNotEqual(response.request['REQUEST_METHOD'], 'POST')
        self.assertNotEqual(response.request['REQUEST_METHOD'], 'PUT')

        
    
