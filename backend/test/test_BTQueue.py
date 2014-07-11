#!/usr/bin/python
import unittest
from mock import Mock

from BTQueue import BTQueue

class test_BTQueue(unittest.TestCase):

  def test_pub_sub(self):
    bt = BTQueue()
    bt.publish(message='someone', routing_key='key')
    f = Mock()
    bt.subscribe(f)
    print 'test pub sub'
    # self.assertIsNotNone(bt)
    f.assert_called_with('someone')


if __name__ == '__main__':
    unittest.main()
