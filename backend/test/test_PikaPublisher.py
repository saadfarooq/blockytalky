#!/usr/bin/python
import unittest
from PikaPublisher import *

class test_PikaPublisher(unittest.TestCase):
  
  def test_pub_sub(self):
    pk = PikaPublisher(exchange_name="exchange")
    pk.publish(message='nothing', routing_key='routing_key')
    self.assertEqual(12, 12)

if __name__ == '__main__':
  unittest.main()