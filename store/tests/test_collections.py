from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
import pytest
from model_bakery import baker
from store.models import Collection
# from django.test import TestCase

@pytest.mark.django_db
class TestCreateCollections:
    def test_if_user_not_authenticated_return_401(self):
        #Arrange
        #Act
        client = APIClient()
        response = client.post('/store/collections/', {'title':'Bikinis'})
        #Assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_not_admin_return_403(self):
        #Arrange
        #Act
        client = APIClient()
        client.force_authenticate(user={})
        response = client.post('/store/collections/', {'title':'Bikinis'})
        #Assert
        assert response.status_code == status.HTTP_403_FORBIDDEN
        
    def test_if_user_admin_and_data_invalid_return_403(self):
        #Arrange
        #Act
        client = APIClient()
        client.force_authenticate(User(is_staff=True))
        response = client.post('/store/collections/', {'title':''})
        #Assert
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None

    def test_if_user_admin_and_data_isvalid_return_201(self):
        #Arrange
        #Act
        client = APIClient()
        client.force_authenticate(User(is_staff=True))
        response = client.post('/store/collections/', {'title':'Carpets'})
        #Assert
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0


@pytest.mark.django_db
class TestRetrieveCollection:
    def test_if_collections_exist_returns_200(self):
        #Arrange-Create a collection
            # Collection.objects.create(title='abc')
        collection = baker.make(Collection)

        #Act - Make a get request to collection
        client = APIClient()
        # client.force_authenticate(user={})
        response = client.get(f'/store/collections/{collection.id}/')

        #Assert
        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] == collection.id
        assert response.data['title'] == collection.title
        assert response.data['products_count'] == 0
