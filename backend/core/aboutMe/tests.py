from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import AboutMe, Part
from datetime import datetime


class CheckAboutMeAPI(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.about_data = {
            'beginning': 'beginning text beginning text',
            'parts': [
                {
                    'part_number': 1,
                    'text': 'text text text text',
                    'picture': 'Image/1/2/3/4/5/6.png'
                },
                {
                    'part_number': 2,
                    'text': 'text text text text',
                    'picture': 'Image/1/2/3/4/5/6.png'
                }
            ]
        }

        AboutMe.objects.create(
            beginning=self.about_data['beginning']
            )

        Part.objects.create(
            about=AboutMe.objects.get(id=1),
            part_number=self.about_data['parts'][0]['part_number'],
            text=self.about_data['parts'][0]['text'],
            picture=self.about_data['parts'][0]['picture']
        )

        Part.objects.create(
            about=AboutMe.objects.get(id=1),
            part_number=self.about_data['parts'][1]['part_number'],
            text=self.about_data['parts'][1]['text'],
            picture=self.about_data['parts'][1]['picture']
        )
        
    def test__aboutMe_status_with_data(self):
        url = '/api/about/1/'
        response = self.client.get(url, follow=True, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_check_data_from_aboutMe_object(self):
        url = '/api/about/1/'
        response = self.client.get(url, follow=True, format='json')
        details = response.data
        self.assertEqual(details['id'], 1)
        self.assertEqual(details['beginning'], self.about_data['beginning'])

    def test_check_aboutMe_requests_method(self):
        url = '/api/about/'
        response = self.client.get(url, follow=True)
        self.assertEqual(response.request['PATH_INFO'], url)
        self.assertEqual(response.request['REQUEST_METHOD'], 'GET')
        self.assertNotEqual(response.request['REQUEST_METHOD'], 'POST')
        self.assertNotEqual(response.request['REQUEST_METHOD'], 'PUT')

    def test_part_model(self):
        url = '/api/about/1/'
        response = self.client.get(url, follow=True, format='json')
        details = response.data

        for x in range(2):
            self.assertEqual(details['parts'][x]['part_number'], self.about_data['parts'][x]['part_number'])
            self.assertEqual(details['parts'][x]['text'], self.about_data['parts'][x]['text'])
            self.assertEqual(details['parts'][x]['picture'], 'http://testserver/media/' + self.about_data['parts'][x]['picture'])

