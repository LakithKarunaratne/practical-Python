import re

complete = False
# dirty_string = '' # this is the parsed data

htmlTag_regex = '<(.|\n)*?>'

def check_found(string,regex):
	# do a string matching to verify if the data is clean
	return

def recursive_clean(dirty_string,regex_string):
	complete_status = False
	while complete_status == False:
		if check_found(dirty_string,regex_string):
			# if found/True run the clean up function
			pass
		else:
			# if found/False set complete to True
			complete_status = True

# <(.|\n)*?> selects the first encountered tag
# found = str(re.search('<(.|\n)*?>',textstr).group(0))
