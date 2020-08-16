import os, argparse
import collections


defaults = {'color': 'red', 'user': 'guest'}

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = {k:v for k, v in vars(namespace).items() if v}

#print(command_line_args)

combined = collections.ChainMap(command_line_args, os.environ, defaults)
#print(combined)
print(combined['color'])
print(combined['user'])