from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Competence, Resume
from datetime import datetime


class CheckResumeAPI(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.resume_data = {
            'main_photo': 'Image/1/2/3/4/5/6.png',
            'name_surname': 'Jan Kowalski',
            'email_info': 'jan.kowalski@mail.com',
            'competences': [
                {
                    'resume': 1,
                    'competence_number': 1,
                    'choice': 1,
                    'title': 'Praca 1',
                    'start_date': '2022-05-23',
                    'end_date': '2022-05-24',
                    'company': 'praca 1 company',
                    'type': 'IT',
                    'details': 'details text'
                },
                {
                    'resume': 1,
                    'competence_number': 2,
                    'choice': 2,
                    'title': 'Choice 2 title',
                    'start_date': '2022-05-21',
                    'end_date': '2022-05-24',
                    'company': 'Choice 2 company',
                    'type': 'IT',
                    'details': 'Choice 2 details text'
                }
            ]
        }

        Resume.objects.create(
            main_photo=self.resume_data['main_photo'],
            name_surname=self.resume_data['name_surname'],
            email_info=self.resume_data['email_info'],
            )

        Competence.objects.create(
            resume=Resume.objects.get(id=1),
            competence_number=self.resume_data['competences'][0]['competence_number'],
            choice=self.resume_data['competences'][0]['choice'],
            title=self.resume_data['competences'][0]['title'],
            start_date=self.resume_data['competences'][0]['start_date'],
            end_date=self.resume_data['competences'][0]['end_date'],
            company=self.resume_data['competences'][0]['company'],
            type=self.resume_data['competences'][0]['type'],
            details=self.resume_data['competences'][0]['details'],
        )

        Competence.objects.create(
            resume=Resume.objects.get(id=1),
            competence_number=self.resume_data['competences'][1]['competence_number'],
            choice=self.resume_data['competences'][1]['choice'],
            title=self.resume_data['competences'][1]['title'],
            start_date=self.resume_data['competences'][1]['start_date'],
            end_date=self.resume_data['competences'][1]['end_date'],
            company=self.resume_data['competences'][1]['company'],
            type=self.resume_data['competences'][1]['type'],
            details=self.resume_data['competences'][1]['details'],
        )

    def test__first_resume_status_with_data(self):
        url = '/api/resume/1/'
        response = self.client.get(url, follow=True, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_check_data_for_resume_model(self):
        url = '/api/resume/1/'
        response = self.client.get(url, follow=True, format='json')
        details = response.data
        self.assertEqual(details['id'], 1)
        self.assertEqual(details['email_info'], self.resume_data['email_info'])
        self.assertEqual(details['name_surname'], self.resume_data['name_surname'])
        self.assertEqual(details['main_photo'], 'http://testserver/media/' + self.resume_data['main_photo'])

    def test_check_resume_requests_method(self):
        url = '/api/resume/'
        response = self.client.get(url, follow=True)
        self.assertEqual(response.request['PATH_INFO'], url)
        self.assertEqual(response.request['REQUEST_METHOD'], 'GET')
        self.assertNotEqual(response.request['REQUEST_METHOD'], 'POST')
        self.assertNotEqual(response.request['REQUEST_METHOD'], 'PUT')

    def test_competence_model(self):
        url = '/api/resume/1/'
        response = self.client.get(url, follow=True, format='json')
        details = response.data

        for x in range(2):
            self.assertEqual(details['competences'][x]['competence_number'], self.resume_data['competences'][x]['competence_number'])
            self.assertEqual(details['competences'][x]['choice'], self.resume_data['competences'][x]['choice'])
            self.assertEqual(details['competences'][x]['start_date'], self.resume_data['competences'][x]['start_date'])
            self.assertEqual(details['competences'][x]['end_date'], self.resume_data['competences'][x]['end_date'])
            self.assertEqual(details['competences'][x]['company'], self.resume_data['competences'][x]['company'])
            self.assertEqual(details['competences'][x]['type'], self.resume_data['competences'][x]['type'])
            self.assertEqual(details['competences'][x]['details'], self.resume_data['competences'][x]['details'])

    def test_compare_dates_true(self):
        url = '/api/resume/1/'
        response = self.client.get(url, follow=True, format='json')
        details = response.data

        for x in range(2):
            start_date = datetime.strptime(details['competences'][x]['start_date'], '%Y-%m-%d')
            end_date = datetime.strptime(details['competences'][x]['end_date'], '%Y-%m-%d')
            self.assertFalse(start_date > end_date)

    def test_compare_dates_false(self):
        url = '/api/resume/1/'
        response = self.client.get(url, follow=True, format='json')
        details = response.data
        
        for x in range(2):
            start_date = datetime.strptime(details['competences'][x]['start_date'], '%Y-%m-%d')
            end_date = datetime.strptime(details['competences'][x]['end_date'], '%Y-%m-%d')
            self.assertFalse(start_date > end_date)
         

