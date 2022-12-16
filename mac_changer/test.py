import argparse
parser = argparse.ArgumentParser()


parser.add_argument('a', type=int, help='first')
parser.add_argument('b', help='second')
parser.add_argument('-a', '--action',)
args = parser.parse_args()
print(args.a)



