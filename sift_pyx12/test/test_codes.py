import unittest

import sift_pyx12.codes
import sift_pyx12.error_handler
import sift_pyx12.map_if
import sift_pyx12.params


class TestExternal(unittest.TestCase):
    """
    Load Codes interface
    """
    def setUp(self):
        self.param = sift_pyx12.params.params()
        self.ext_codes = sift_pyx12.codes.ExternalCodes(None, self.param.get('exclude_external_codes'))

    def test_valid_state1(self):
        self.assertTrue(self.ext_codes.isValid('states', 'MI', '20031001'))

    def test_valid_state2(self):
        self.assertTrue(self.ext_codes.isValid('states', 'NV'))

    def test_invalid_state1(self):
        self.assertFalse(self.ext_codes.isValid('states', 'AN', '20031001'))

    def test_exclude_state_code(self):
        self.param.set('exclude_external_codes', 'states')
        ext_codes = sift_pyx12.codes.ExternalCodes(None, self.param.get('exclude_external_codes'))
        self.assertTrue(ext_codes.isValid('states', 'ZZ'))

    def test_noexclude_state_code(self):
        ext_codes = sift_pyx12.codes.ExternalCodes(None, self.param.get('exclude_external_codes'))
        self.assertFalse(ext_codes.isValid('states', 'ZZ'))


class TestExternalMapPath(unittest.TestCase):
    """
    Load Codes interface
    """
    def setUp(self):
        import os.path
        self.param = sift_pyx12.params.params()
        map_path = os.path.join(os.path.dirname(sift_pyx12.codes.__file__), 'map')
        self.ext_codes = sift_pyx12.codes.ExternalCodes(map_path, self.param.get('exclude_external_codes'))

    def test_valid_state1(self):
        self.assertTrue(self.ext_codes.isValid('states', 'MI', '20031001'))

    def test_valid_state2(self):
        self.assertTrue(self.ext_codes.isValid('states', 'NV'))

    def test_invalid_state1(self):
        self.assertFalse(self.ext_codes.isValid('states', 'AN', '20031001'))

    def test_exclude_state_code(self):
        self.param.set('exclude_external_codes', 'states')
        ext_codes = sift_pyx12.codes.ExternalCodes(None, self.param.get('exclude_external_codes'))
        self.assertTrue(ext_codes.isValid('states', 'ZZ'))

    def test_noexclude_state_code(self):
        ext_codes = sift_pyx12.codes.ExternalCodes(None, self.param.get('exclude_external_codes'))
        self.assertFalse(ext_codes.isValid('states', 'ZZ'))
