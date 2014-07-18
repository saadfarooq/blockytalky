from  multiprocessing import Process
from btsub import BTSub
from hardware_module import HardwareModule

if __name__ == "__main__":
  queue = BTSub('saad')
  hd = HardwareModule(queue)
  # Now we can connect a client to all these servers
  Process(target=hd, args=()).start()