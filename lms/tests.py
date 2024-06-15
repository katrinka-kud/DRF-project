from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from lms.models import Course, Lesson, Subscription
from users.models import User


class CourseTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test123@test.com", password="test")
        self.course = Course.objects.create(title="Тестовое название курса", description="Тестовое описание курса",
                                            owner=self.user)
        self.lesson = Lesson.objects.create(title="Тестовое название урока", description="Тестовое описание урока",
                                            course=self.course, owner=self.user)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_retrieve_course(self):
        url = reverse("lms:course-detail", args=(self.course.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK,
        )
        self.assertEqual(
            data.get("title"), self.course.title,
        )

    def test_create_course(self):
        url = reverse("lms:course-list")
        data = {"title": "Test", "description": "Test"}
        response = self.client.post(url, data)
        # print(response.json())
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED,
        )
        self.assertEqual(
            Course.objects.all().count(), 2
        )

    def test_update_course(self):
        url = reverse("lms:course-detail", args=(self.course.pk,))
        data = {"title": "Test", "description": "Test"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK,
        )
        self.assertEqual(
            data.get("title"), "Test"
        )

    def test_delete_course(self):
        url = reverse("lms:course-detail", args=(self.course.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT,
        )
        self.assertEqual(
            Course.objects.all().count(), 0
        )

    def test_list_course(self):
        url = reverse("lms:course-list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [{
                "id": self.course.pk,
                "title": self.course.title,
                "description": self.course.description,
                "picture": None,
                "owner": self.user.pk
            }]}
        self.assertEqual(
            response.status_code, status.HTTP_200_OK,
        )
        self.assertEqual(
            data, result
        )


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test123@test.com", password="test")
        self.course = Course.objects.create(title="Тестовое название курса", description="Тестовое описание курса",
                                            owner=self.user)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_subscription_activate(self):
        url = reverse("lms:subscription-create")
        data = {"user": self.user.pk, "course": self.course.pk}
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"message": "подписка добавлена"})

    def test_subscription_deactivate(self):
        url = reverse("lms:subscription-create")
        Subscription.objects.create(user=self.user, course=self.course)
        data = {"user": self.user.id, "course": self.course.id}

        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"message": "подписка удалена"})
