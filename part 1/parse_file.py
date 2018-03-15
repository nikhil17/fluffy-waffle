import datetime
import pytz
from collections import Counter, defaultdict

f = open("input.txt",'r')
timestamp_counter = defaultdict(Counter)

for line in f:
	line = line.strip('\n').split('|')
	timestamp, website = line
	#change timestamp to gmt
	gmt = pytz.timezone('GMT')
	date_object = datetime.datetime.fromtimestamp(int(timestamp), gmt)
	output_date = date_object.strftime("%d/%m/%y")
	timestamp_counter[output_date][website] += 1

keys = sorted(timestamp_counter.keys())
for key in keys:
	print key 
	websites_and_count = timestamp_counter[key].most_common()
	for website, count in websites_and_count:
		print website, count



	