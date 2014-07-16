#!/usr/bin/python
import unittest
from mock import MagicMock

from btqueue import BTQueue

class test_BTQueue(unittest.TestCase):

  def test_pub_sub(self):
    bt = BTQueue('HwCmd')
    bt.publish(message='someone')
    f = MagicMock()
    bt.subscribe(f)
    f.assert_called_once()

if __name__ == '__main__':
    unittest.main()
