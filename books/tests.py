from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient

from .models import Author
from .serializers import AuthorSerializer


class AuthorTestCase(TestCase):
    def setUp(self):
        Author.objects.create(last_name="Николаев", first_name="Олег", patronymic="Сергеевич")
        Author.objects.create(last_name="Иванова", first_name="Евгения", patronymic="Михайловна")

    def test_author_created(self):
        self.assertEqual(Author.objects.get(pk=1).last_name, "Николаев")


class GetAllAuthors(TestCase):
    def setUp(self):
        Author.objects.create(last_name="Петров", first_name="Олег", patronymic="Сергеевич")
        Author.objects.create(last_name="Иванова", first_name="Евгения", patronymic="Михайловна")
        self.user = User.objects.create(username="admin", password="admin")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_get_all_authors(self):
        response = self.client.get(reverse('author-list'))
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
