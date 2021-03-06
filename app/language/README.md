LANGUAGE MODULE README
===

This tool allows for all text (Text messages, error messages, HTML) in the application to be translated.


Components
---

- AngularJS translate module
	- files stored in /static
	- This module is used as a resource by the main angularJS app
		- ```/static/module.js```
	- Filter allows any term in the HTML to be translated
		- ```/static/filters.js```
		- Use in an HTML file: ```{{ 'KEY_NAME' | translate: 'uppercase' }}```
		- Calls upon the service to handle the actual translation
	- Service sets the language and handles the actual work of translating terms
		- ```/static/services.js```
		- Intelligently determines the default language
			- If ***language-setting*** is stored in server session, uses that language, otherwise:
			- Defaults to Spanish if phone set in Spanish, otherwise English
		- Stores the current language + handles switching languages
			- Updates server ***language-setting*** when language switched
		- Stores the language ***map*** that is retreived from server
		- Handles translations 
			- Used by filter and controllers

- translate endpoints
	- ```__init__.py```
	- translate is a blueprint registered with the larger Flask application
	- ```/translate/map``` is the endpoint that returns formatted ***map*** in JSON
	- ```/language/setting``` endpoints handle saving the user's ***language-setting*** in session
		- POST ```/language/setting``` sets the ***language-setting*** in session
		- GET ```/language/setting``` retrieves ***language-setting*** in session

- ***map***
	- ```map.py``` does the work of building + returning map
	- ***map*** structure:
	```
		{
		keyname: {
			en: "english translation",
			es: "spanish translation",
			... for column/language in spreadsheet
		},
		... for row/keyname in spreadsheet
	}
	```
	- all translation data comes from google doc spreadsheet

- Spreadsheet
	- publicly hosted: <https://docs.google.com/a/significancelabs.org/spreadsheets/d/1O2VvGGMeIEeugPa-TBBk7sKt4Kstdw31bphQ5jDp71c/edit#gid=0>
		- Anyone can view (AKA my application), but only specified translators can edit
	- Contains all translation keys and terms
	- See spreadsheet notes for ***rules***


Spreadsheet Rules
---
- The following items will prevent the item from being parsed into the translations map
	- commas ```,```
	- colons ```:```


Test Coverage
---

Unit tests are in test_language.py

Still would like e2e tests for angular module

