from django.contrib.auth.hashers import BasePasswordHasher

class PlainTextPassword(BasePasswordHasher):
    """Password hasher that stores passwords as plain text."""
    algorithm = "plain"
    prefix = algorithm + "$"

    def salt(self):
        return ''

    def encode(self, password, salt):
        assert salt == ''
        return self.prefix + password

    def verify(self, password, encoded):
        if encoded.startswith(self.prefix):
            ok = password == encoded[len(self.prefix):]
            #print(repr([password, encoded, ok]))
            return ok
        return False

    def safe_summary(self, encoded):
        return OrderedDict([
            (_('algorithm'), self.algorithm),
            (_('hash'), encoded),
        ])
