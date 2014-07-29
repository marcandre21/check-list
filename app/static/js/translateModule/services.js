/***************************************************
	Significance Labs
	Brooklyn, NYC

 	Author: Alexandra Berke (aberke)
 	Written: June 2014


 	AngularJS translateModule: service

****************************************************/

var TranslateService = function() {

	/*
	- Manager of current language {String} currentLanguage
	- Called by TranslateFilter to do the work of translation
	- Keeps translations in translateMap:
	{
		keyname: {
			en: "english translation",
			es: "spanish translation",
			... for column/language in spreadsheet
		},
		... for row/keyname in spreadsheet
	}
	translateMap is constructed in translateMap.js
	*/

	// initialize currentLanguage to english
	var currentLanguage = 'en';

	this.getCurrentLanguage = function() {
		return currentLanguage;
	}
	this.setCurrentLanguage = function(language) {
		currentLanguage = language;
		return language;
	}
	this.translateMap = translateMap;

	this.translate = function(keyname) {
		if (keyname in translateMap) {
			return translateMap[keyname][currentLanguage];
		}
		return null;
	}
}
