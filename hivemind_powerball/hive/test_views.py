from django.test import TestCase, RequestFactory

from .models import Drone
from .views import DroneDetail, DroneList
from .views import DroneCreate, DroneDelete, DroneUpdate


class DroneViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.drone = Drone.objects.create(first_name='tim', last_name='jones')

    def test_drone_create_responds_with_200(self):
        request = self.factory.get('/hive/drone/add/')
        response = DroneCreate.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_drone_create_responds_with_correct_title(self):
        request = self.factory.get('/hive/drone/add/')
        response = DroneCreate.as_view()(request)
        self.assertContains(response, "Drone Identifier")

    def test_drone_detail_responds_with_200(self):
        request = self.factory.get('/hive/drone/{}/'.format(self.drone.id))
        response = DroneDetail.as_view()(request, pk=self.drone.id)
        self.assertEqual(response.status_code, 200)

    def test_drone_detail_responds_with_correct_data(self):
        request = self.factory.get('/hive/drone/{}/'.format(self.drone.id))
        response = DroneDetail.as_view()(request, pk=self.drone.id)
        self.assertContains(response, 'id: {}'.format(self.drone.id))
        self.assertContains(response, 'Tim Jones')

    def test_drone_list_responds_with_200(self):
        request = self.factory.get('/hive/drones/')
        response = DroneList.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_drone_list_responds_with_correct_data(self):
        newdrone = Drone.objects.create(first_name='tom', last_name='smith')
        request = self.factory.get('/hive/drones/')
        response = DroneList.as_view()(request)
        self.assertContains(response, 'Tim Jones')
        self.assertContains(response, 'Tom Smith')

    def test_drone_delete_responds_with_200(self):
        request = self.factory.get('/hive/drone/{}/delete'.format(self.drone.id))
        response = DroneDelete.as_view()(request, pk=self.drone.id)
        self.assertEqual(response.status_code, 200)

    def test_drone_delete_responds_with_correct_data(self):
        request = self.factory.get('/hive/drone/{}/delete'.format(self.drone.id))
        response = DroneDelete.as_view()(request, pk=self.drone.id)
        self.assertContains(response, 'Execute Drone')

    def test_drone_update_responds_with_200(self):
        request = self.factory.get('/hive/drone/{}/edit/'.format(self.drone.id))
        response = DroneUpdate.as_view()(request, pk=self.drone.id)
        self.assertEqual(response.status_code, 200)

    def test_drone_update_responds_with_correct_data(self):
        request = self.factory.get('/hive/drone/{}/edit/'.format(self.drone.id))
        response = DroneUpdate.as_view()(request, pk=self.drone.id)
        self.assertContains(response, "Drone Identifier")

