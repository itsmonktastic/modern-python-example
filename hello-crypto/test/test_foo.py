import unittest

import foo


class FooTest(unittest.TestCase):
    def test_foo(self):
        self.assertEqual("foo", foo.foo())
