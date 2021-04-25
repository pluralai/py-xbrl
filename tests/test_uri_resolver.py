import sys
import unittest
import os
import time
from xbrl_parser.cache import HttpCache
import logging
from xbrl_parser.helper.uri_resolver import resolve_uri


class UriResolverTest(unittest.TestCase):

    def test_resolve_uri(self):
        """
        :return:
        """

        test_arr = [
            # test paths
            (('E:\\Programming\\python\\xbrl_parser\\tests\\data\\example.xsd', '/example-lab.xml'),
             os.sep.join(['E:', 'Programming', 'python', 'xbrl_parser', 'tests', 'data', 'example-lab.xml'])),
            ((r'E:\Programming\python\xbrl_parser\tests\data\example.xsd', '/example-lab.xml'),
             os.sep.join(['E:', 'Programming', 'python', 'xbrl_parser', 'tests', 'data', 'example-lab.xml'])),
            (('E:/Programming/python/xbrl_parser/tests/data/example.xsd', '/example-lab.xml'),
             os.sep.join(['E:', 'Programming', 'python', 'xbrl_parser', 'tests', 'data', 'example-lab.xml'])),
            # test directory traversal
            (('E:/Programming/python/xbrl_parser/tests/data/example.xsd', '/../example-lab.xml'),
             os.sep.join(['E:', 'Programming', 'python', 'xbrl_parser', 'tests', 'example-lab.xml'])),
            (('E:/Programming/python/xbrl_parser/tests/data/example.xsd', './../example-lab.xml'),
             os.sep.join(['E:', 'Programming', 'python', 'xbrl_parser', 'tests', 'example-lab.xml'])),
            (('E:/Programming/python/xbrl_parser/tests/data/example.xsd', '../../example-lab.xml'),
             os.sep.join(['E:', 'Programming', 'python', 'xbrl_parser', 'example-lab.xml'])),

            # test urls
            (('http://example.com/a/b/c/d/e/f/g', 'file.xml'), 'http://example.com/a/b/c/d/e/f/g/file.xml'),
            (('http://example.com/a/b/c/d/e/f/g', '/file.xml'), 'http://example.com/a/b/c/d/e/f/g/file.xml'),
            (('http://example.com/a/b/c/d/e/f/g', './file.xml'), 'http://example.com/a/b/c/d/e/f/g/file.xml'),
            (('http://example.com/a/b/c/d/e/f/g', '../file.xml'), 'http://example.com/a/b/c/d/e/f/file.xml'),
            (('http://example.com/a/b/c/d/e/f/g', '/../file.xml'), 'http://example.com/a/b/c/d/e/f/file.xml'),
            (('http://example.com/a/b/c/d/e/f/g', './../file.xml'), 'http://example.com/a/b/c/d/e/f/file.xml'),
            (('http://example.com/a/b/c/d/e/f/g', '../../file.xml'), 'http://example.com/a/b/c/d/e/file.xml'),
            (('http://example.com/a/b/c/d/e/f/g', '/../../file.xml'), 'http://example.com/a/b/c/d/e/file.xml'),
            (('http://example.com/a/b/c/d/e/f/g', './../../file.xml'), 'http://example.com/a/b/c/d/e/file.xml'),
            (('http://example.com/a/b/c/d/e/f/g', '../../../file.xml'), 'http://example.com/a/b/c/d/file.xml')

        ]
        for i, elem in enumerate(test_arr):
            self.assertEqual(elem[1], resolve_uri(elem[0][0], elem[0][1]), msg=f'Failed at test elem {i}')


if __name__ == '__main__':
    unittest.main()