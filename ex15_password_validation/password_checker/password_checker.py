import bcrypt


class PasswordChecker:
    # this obviously isn't the right way to implement a password vault!
    VAULT = {
        'me': bcrypt.hashpw(b'password', bcrypt.gensalt()),
        'you': bcrypt.hashpw(b'passord', bcrypt.gensalt())
    }

    def valid_pw_p(self, user, password):
        # `not in` checks for non-membership
        if user not in self.VAULT.keys():
            return False

        # bcrypt requires the object being encrypted to be a bytestream
        return bcrypt.checkpw(password.encode(), self.VAULT[user])
