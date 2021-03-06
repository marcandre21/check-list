#********************************************************************************
#--------------------------------------------------------------------------------
#
#	Significance Labs
#	Brooklyn, NYC
#
# 	Author: Alexandra Berke (aberke)
# 	Written: Summer 2014
#
#
#
#	/lib/error_codes.py
#	error codes with messages returned by util.respond500
#	
#	Error codes with protocol makes error message translation easier
#		- Only return certain set of strings 
#			that are in spreadsheet to be translated
#
# 	See util.respond500
# 	Philosophy:
# 	Return a small set of error strings 
# 		- These strings are keywords in the translations spreadsheet that have translations
# 	Use:
# 	When endpoints are hit with bad data or cause accidental exceptions to occur
# 	It catches accidentally raised Exceptions 
# 		- In this case, expects code==0
# 		- Returns nicely formatted response to user rather than cryptic mongo/python error 
# 	It it called directly when endpoint receives invalid data 
# 		- Expects code in error_codes map	
#
#--------------------------------------------------------------------------------
#*********************************************************************************

map = {
	0: 'UNEXPECTED SERVER ERROR',
	1: 'PHONENUMBER REQUIRED ERROR',
	2: 'USER PHONENUMBER NOT FOUND ERROR',
	3: 'INVALID RESET CODE ERROR',
	4: 'INVALID PASSWORD ERROR',
	5: 'USER PHONENUMBER ALREADY EXISTS ERROR',
	6: 'NAME REQUIRED ERROR',
	7: 'INVALID PHONENUMBER',
}













