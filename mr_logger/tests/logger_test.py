# -*- coding: utf-8 -*-
#!/usr/bin/python

import sys
import os
import unittest

parent = os.path.dirname(os.getcwd())
sys.path.append(parent)


from logger import Logger


class LoggerTest(unittest.TestCase):
    logger = Logger()

    def test_get_prefix(self):
        prefix = self.logger._get_prefix(msg_type=self.logger.type_info)
        self.assertEqual('[INFO]: ', prefix)
        prefix = self.logger._get_prefix(msg_type=self.logger.type_warn)
        self.assertEqual('[WARN]: ', prefix)
        prefix = self.logger._get_prefix(msg_type=self.logger.type_ok)
        self.assertEqual('[✔]: ', prefix)
        prefix = self.logger._get_prefix(msg_type=self.logger.type_err)
        self.assertEqual('[❌]: ', prefix)
        print(("test get prefix ... [ok]"))

    def test_get_color(self):
        """ change colors here when colors are changed in service """
        color = self.logger._get_color(msg_type=self.logger.type_info)
        self.assertEqual('cyan', color)
        color = self.logger._get_color(msg_type=self.logger.type_warn)
        self.assertEqual('yellow', color)
        color = self.logger._get_color(msg_type=self.logger.type_ok)
        self.assertEqual('green', color)
        color = self.logger._get_color(msg_type=self.logger.type_err)
        self.assertEqual('red', color)
        print(("test get color ... [ok]"))

    def test_logs(self):
        self.logger.info(text='test text cyan')
        self.logger.warn(text='test text yellow')
        self.logger.err(text='test text red')
        self.logger.ok(text='test text green')
        self.logger.log(text='test text white')


if __name__ == '__main__':
    unittest.main()
