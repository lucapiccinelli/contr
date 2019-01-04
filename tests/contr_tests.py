from nose.tools import *
from contr import contr


class contr_tests():
    def test_contr_mustInstallItself_AsAProxy(self):
        response = contr.main(["--test, https://www.google.com"])
        assert_equal("ok", response)