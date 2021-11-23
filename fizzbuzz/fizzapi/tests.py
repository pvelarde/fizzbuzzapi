from django.test import RequestFactory, TestCase
from .models import FizzBuzz
from .views import FizzBuzzView, FizzBuzzDetail

class TestFizzBuzzView(TestCase):
    """
    This test class covers the endpoint /fizzbuzz (GET and POST)
    """
    def create_test_data(self):
        """
        Creates test data for retrieval by GET
        """
        testData = FizzBuzz(
            fizzbuzz_id=1,
            useragent=(
                'Mozilla/5.0 (Macintosh; Intel Mac OS X XX.XX; rv:XX.0) '
                'Gecko/20100100 Firefox/XX.X'
            ),
            message='Test message'
        )
        testData.save()
        testDataTwo = FizzBuzz(
            fizzbuzz_id=2,
            useragent=(
                'Mozilla/5.0 (Macintosh; Intel Mac OS X XX.XX; rv:XX.0) '
                'Gecko/20100100 Firefox/XX.X 2'
            ),
            message='Test message 2'
        )
        testDataTwo.save()

    def test_fizzlist(self):
        """
        Tests the GET functionality of /fizzbuzz
        """
        self.create_test_data()
        request = RequestFactory().get('/fizzbuzz')
        response = FizzBuzzView.as_view()(request)
        firstEntry=response.data[0]
        secondEntry=response.data[1]
        # Test first entry data
        self.assertEqual(firstEntry['fizzbuzz_id'], 1)
        useragent = (
            'Mozilla/5.0 (Macintosh; Intel Mac OS X XX.XX; rv:XX.0) '
            'Gecko/20100100 Firefox/XX.X'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(firstEntry['useragent'], useragent)
        self.assertEqual(firstEntry['message'], 'Test message')
        # Test second entry data
        self.assertEqual(secondEntry['fizzbuzz_id'], 2)
        useragent = (
            'Mozilla/5.0 (Macintosh; Intel Mac OS X XX.XX; rv:XX.0) '
            'Gecko/20100100 Firefox/XX.X 2'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(secondEntry['useragent'], useragent)
        self.assertEqual(secondEntry['message'], 'Test message 2')

    def test_post(self):
        """
        Tests the POST functionality of /fizzbuzz
        """
        factory = RequestFactory()
        data = {'message': 'POST Test Message'}
        request = factory.post('/fizzbuzz', data, content_type='application/json', 
            HTTP_USER_AGENT='Mozilla/5.0')
        response = FizzBuzzView.as_view()(request)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['message'], 'POST Test Message')
        self.assertEqual(response.data['useragent'], 'Mozilla/5.0')

class TestFizzBuzzDetail(TestCase):
    """
    This test class covers the endpoint /fizzbuzz/<int> (GET)
    """
    def create_test_data(self):
        """
        Creates test data for retrieval by GET
        """
        testData = FizzBuzz(
            fizzbuzz_id=3,
            useragent=(
                'Mozilla/5.0 (Macintosh; Intel Mac OS X XX.XX; rv:XX.0) '
                'Gecko/20100100 Firefox/XX.X'
            ),
            message='Test detail message'
        )
        testData.save()
    
    def test_detail_data(self):
        """
        Tests the GET functionality of /fizzbuzz/<int>
        """
        self.create_test_data()
        request = RequestFactory().get('/fizzbuzz/3')
        response = FizzBuzzDetail.as_view()(request, 3)
        details=response.data
        # Test response data
        self.assertEqual(details['fizzbuzz_id'], 3)
        useragent = (
            'Mozilla/5.0 (Macintosh; Intel Mac OS X XX.XX; rv:XX.0) '
            'Gecko/20100100 Firefox/XX.X'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(details['useragent'], useragent)
        self.assertEqual(details['message'], 'Test detail message')

    def test_detail_error(self):
        """
        Tests the GET functionality of /fizzbuzz/<int> when <int>
        is not found
        """
        self.create_test_data()
        request = RequestFactory().get('/fizzbuzz/10')
        response = FizzBuzzDetail.as_view()(request, 10)
        self.assertEqual(response.status_code, 404)