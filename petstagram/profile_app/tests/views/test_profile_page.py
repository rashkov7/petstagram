from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from petstagram.main_app.models import Pet, PetPhoto
from petstagram.profile_app.models import Profile

UserModel = get_user_model()


class TestProfilePageView(TestCase):
    data_profile = {
        "first_name": 'gogo',
        "last_name": 'gogov',
        'picture': "https://www.business2community.com/wp-content/uploads/2017/08/blank-profile-picture-973460_640.png",
        "birth_date": '2000-02-08',
        'description': 'ggggg',
        'gender': "Male",
    }
    data_user = {
        'email': 'gogo@abv.bg',
        'password': '123',
    }
    data_pet = {
        'name': 'Puppy',
        'animal_type': 'Dog',
        'birth_date': '2020-02-08',
    }
    data_petphoto = {
        'photo': 'images/dog2_oH6BtFR.jpg',
        'description': 'description text',
        'published': '2022-03-18',
    }

    def create_actual_profile_user(self):
        self.data_user['has_profile'] = True
        user = UserModel.objects.create_user(**self.data_user)
        profile = Profile.objects.create(**self.data_profile, user=user)
        return profile, user

    def test__user_has_only_a_profile(self):
        profile, user = self.create_actual_profile_user()
        key = profile.pk
        response = self.client.get(reverse('profile page', kwargs={'pk': key}))
        self.assertTemplateUsed(response, template_name='profile_details.html')

    def test__user_has_no_profile_no_pets_no_photos_no_likes(self):
        user = UserModel.objects.create_user(**self.data_user)
        profile = Profile.objects.create(**self.data_profile, user=user)
        key = profile.pk
        response = self.client.get(reverse('profile edit', kwargs={'pk': key}))
        self.assertTemplateUsed(response, 'profile/profile_edit.html')

    def test__user_has_profile_and_two_pets_no_photos_no_likes(self):
        profile, user = self.create_actual_profile_user()

        Pet.objects.create(**self.data_pet, user_profile=profile)
        self.data_pet['name'] = 'Tosho'
        Pet.objects.create(**self.data_pet, user_profile=profile)

        response = self.client.get(reverse('profile page', kwargs={'pk': profile.pk}))
        self.assertTrue(response.context_data['pets'])
        self.assertEqual(len(response.context_data['pets']), 2)

    def test__user_has_profile_and_two_pets_with_one_photo_no_likes(self):
        profile, user = self.create_actual_profile_user()

        pet = Pet.objects.create(**self.data_pet, user_profile=profile)
        self.data_pet['name'] = 'Bosho'
        pet2 = Pet.objects.create(**self.data_pet, user_profile=profile)

        photo = PetPhoto.objects.create(**self.data_petphoto)
        photo.pets.add(pet)
        photo.pets.add(pet2)
        photo.save()

        response = self.client.get(reverse('profile page', kwargs={'pk': profile.pk}))
        self.assertEqual(2, len(response.context['pets']))

    def test__user_with_profile_and_two_pets_with_one_photo__added_unfamiliar_pet(self):
        user = UserModel.objects.create_user(**self.data_user)
        profile = Profile.objects.create(**self.data_profile, user=user)

        self.data_user['email'] = 'dd@abv.bg'
        user2 = UserModel.objects.create_user(**self.data_user)
        profile2 = Profile.objects.create(**self.data_profile, user=user2)
        pet_else = Pet.objects.create(**self.data_pet, user_profile=profile2)
        photo_else = PetPhoto.objects.create(**self.data_petphoto)
        photo_else.pets.add(pet_else)
        pet_else.save()

        pet = Pet.objects.create(**self.data_pet, user_profile=profile)
        self.data_pet['name'] = 'Kosho'
        pet2 = Pet.objects.create(**self.data_pet, user_profile=profile)

        photo = PetPhoto.objects.create(**self.data_petphoto)
        photo.pets.add(pet)
        photo.pets.add(pet2)
        photo.save()

        response = self.client.get(reverse('profile page', kwargs={'pk': profile.pk}))
        self.assertEqual(2, len(response.context['pets']))
