from django.test import SimpleTestCase, TestCase
from my_auth.models import MyUser


class TestMyUser(TestCase):
    def test_create_user(self):

        data = [
            {"login": "login", "password": "password", "email": "email"},
            {"login": "user", "password": "user", "email": "user@email.ru"},
            {"login": "user123", "password": "password123", "email": "123@mail.ru"},
        ]

        for user in data:
            MyUser()
            new_user = MyUser(**user)
            new_user.save()

            new_user_id = new_user.pk
            del new_user

            db_user = MyUser.objects.get(pk=new_user_id)

            self.assertTrue(db_user)
            print(f"Test assert TRUE:", True if db_user else False)

            if db_user:
                user_data = {"login": db_user.login, "password": db_user.password, "email": db_user.email}
                self.assertEqual(user_data, user)