from django.test import TestCase
from .models import Order
# Create your tests here.

class TodoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Order.objects.create(robot='sw1', start='w', finish='z', status='completed')
        Order.objects.create(robot='vie', start='w', finish='y', status='incomplete')

    def test_start_content(self):
        todo = Order.objects.get(id=1)
        expected_object_name = f'{todo.start}'
        self.assertEquals(expected_object_name, 'w')

    def test_finish_content(self):
        todo = Order.objects.get(id=2)
        expected_object_name = f'{todo.finish}'
        self.assertEquals(expected_object_name, 'y')

    def test_status_content(self):
        todo = Order.objects.get(id=2)
        expected_object_name = f'{todo.status}'
        self.assertEquals(expected_object_name, 'incomplete')