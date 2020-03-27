import re


def validate_username(username):
	if re.match(r'^[a-zA-Z\d_]{5,30}$', username):
		return True
	return False
