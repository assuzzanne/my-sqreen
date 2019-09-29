import unittest
from app.lib.check_signature import check_signature


class TestCheckSignature(unittest.TestCase):
    def test_check_signature_succeeding(self):
        result = check_signature(b'1234', '9d101d2bf630748679226b767d2031634c520390ff0e926afc09bc65a05bfdb2', b'4567')
        self.assertTrue(result)

    def test_check_signature_failing(self):
        result = check_signature(b'1234', 'invalid_request_signature', b'4567')
        self.assertFalse(result)

if __name__ == '__main__':
  unittest.main()
