
"""
argparse library -> https://docs.python.jp/3/library/argparse.html
python-osc -> https://github.com/attwad/python-osc
"""
import argparse
import math

from pythonosc import dispatcher
from pythonosc import osc_server

def print_myo_handler(unused_addr,args,myo):
    print("[{0}] ~ {1}".format(args[0],myo))

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip",
      default="127.0.0.1", help="The ip to listen on")
  parser.add_argument("--port",
      type=int, default=8888, help="The port to listen on")
  args = parser.parse_args()

  dispatcher = dispatcher.Dispatcher()
  dispatcher.map("/myo", print_myo_handler,"myo")

  server = osc_server.ThreadingOSCUDPServer( (args.ip, args.port), dispatcher)
  print("Serving on {}".format(server.server_address))
  server.serve_forever()
