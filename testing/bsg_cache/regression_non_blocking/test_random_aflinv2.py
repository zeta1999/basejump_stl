import sys
import random
from test_base import *


class TestRandomAFLINV2(TestBase):

  def generate(self):
    # scrub tag and data
    self.clear_tag()
    for i in range(self.MAX_ADDR/4):
      self.send(SW, 4*i)

    # random SW/LW
    for iteration in range(10000):
      tag = random.randint(0,9)
      index = random.randint(0,1)
      store_not_load = random.randint(0,1)
      for b in range(self.block_size_in_words_p):
        taddr = self.get_addr(tag, index, b)
        if store_not_load:
          self.send(SW, taddr)
        else:
          self.send(LW, taddr)

      self.wait(random.randint(0,255))
          
      index = random.randint(0,1)
      store_not_load = random.randint(0,1)
      taddr = self.get_addr(tag, index)
      self.send(AFLINV, taddr)

    self.tg.done()
          
#   main()
if __name__ == "__main__":
  t = TestRandomAFLINV2()
  t.generate()
