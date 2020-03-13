import re


def validate_username(username):
	if re.match(r'^[\w\d]{5,30}$', username):
		return True
	return False
