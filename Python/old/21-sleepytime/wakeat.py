import argparse

parser = argparse.ArgumentParser(description='Gets times to go to bed with given wake time.')
parser.add_argument('hour', metavar='N', type=int, nargs='+', 
	help='an integer for the hour of the day')
parser.add_argument('minute', metavar='N', type=int, nargs='+', 
	help='an integer for the minute of the hour')

args = parser.parse_args()
hour, minute = args.hour[0], args.minute[0]
sh = hour - 5
sm = minute - 30

if (sm < 0):
	hour-=1
	sm = -sm
print("You should go to sleep at [{}:{}]".format(sh, sm))