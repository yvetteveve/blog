def test_no_access_password(self):
            with self.assertRaises(AttributeError):
                self.new_user.password

        def test_password_verification(self):
            self.assertTrue(self.new_user.verify_password('123'))
