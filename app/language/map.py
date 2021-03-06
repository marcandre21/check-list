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
# 	/language/map.py
#
# Contains the actual translation data
# Translate data comes from a publicly published Google Spreadsheet
# Initially contains empty map
#
# {
# 	keyname: {
# 		en: "english translation",
# 		es: "spanish translation",
# 		... for column/language in spreadsheet
# 	},
# 	... for row/keyname in spreadsheet
# }
#
#	Google documentation for accessing spreadsheet data:
#		https://developers.google.com/gdata/samples/spreadsheet_sample
#
#
#--------------------------------------------------------------------------------
#*********************************************************************************

import requests
import re # splitting content returned from google with a regex

from app.lib.util import APIexception, yellERROR, jsonp
import config


# Google documentation for accessing spreadsheet data:
# https://developers.google.com/gdata/samples/spreadsheet_sample
KEY = config.GOOGLE_API_TRANSLATE_SPREADSHEET_KEY 
FORMAT = 'json'
GOOGLE_API_REQUEST_URL = 'http://spreadsheets.google.com/feeds/list/{0}/od6/public/basic?alt={1}'.format(KEY, FORMAT)



# map of translations kept in "cache"
map = {}

def get_map():
	if map:
		return map
	return build_map()

def build_map():
	# re-initialize map
	map = {}

	# get translate data from spreadsheet as json
	r = requests.get(GOOGLE_API_REQUEST_URL)
	if not (r.status_code == 200 or r.status_code == '200'):
		raise APIexception(message='Error retrieving translate google spreadsheet')

	# parse translate data json into map form

	data = r.json()

	entry_list = data['feed']['entry']
	entry = None
	keyname = None
	content = None
	translation_array = None
	translation_partition = None

	for i in range(len(entry_list)):
		# will add { keyname: translations } to map after building translations dictionary
		translations = {} # of form {'en': translation, 'es':translation,..}

		try:
			entry = entry_list[i]
			keyname = entry['title']['$t']

			# content of form "en: phone, es: phonenumber abbr. in spanish"
			content = entry['content']['$t']
			translation_array = re.split(r', *', content)

			for a in range(len(translation_array)):
				translation_partition = re.split(r': *', translation_array[a])
				language = translation_partition[0]
				translation = translation_partition[1]
				translations[language] = translation
		
		except Exception as e:
			yellERROR('Error parsing translation map item: \n' + e.message + '\n' + str(entry))
			continue

		map[keyname] = translations

	return map



map = build_map()