import re
def findMonthAndDate(string):
		
	regex = r"([a-zA-Z]+) (\d+)"
	match = re.match(regex, string)
		
	if match == None:
		print ("Not a valid date")
		return
	
	print ("Given Data: %s" % (match.group()))
	print ("Month: %s" % (match.group(1)))
	print ("Day: %s" % (match.group(2)))
	
		
findMonthAndDate("Jun 24")
print("")
findMonthAndDate("I was born on June 4")
