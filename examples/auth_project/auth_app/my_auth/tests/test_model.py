from django.test import SimpleTestCase
from my_auth.models import MyUser


class TestMyUser(SimpleTestCase):
    def test_create_user(self):
        data = {"login": "login", "password": "password", "email": "email"}

        new_user = MyUser(**data)
        new_user.save()
        new_user_id = new_user.id
        print(new_user_id)
        del new_user

        res = MyUser.objects.filter(id=new_user_id).first()

        self.assertTrue(res)
        print("TEST ASSERT TRUE", True if res else False)

        if res:
            res_d = {"login": res.login,
                     "password": res.password,
                     "email": res.email}

            self.assertEqual(res_d, data)




