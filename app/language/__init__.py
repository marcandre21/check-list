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
#	Base file of language module
# 	/language/__init__.py
#
#
#--------------------------------------------------------------------------------
#*********************************************************************************

from flask import Blueprint, request, session

from app.lib.util import dumpJSON, respond500, respond200, jsonp, APIexception, JSONencoder
from map import get_map


SUPPORTED_LANGUAGES = ['en', 'es']



bp = Blueprint('language', __name__, static_folder='static')



@bp.route('/')
def view():
	return 'language'


#- Language Setting --------------------------------------------------
@bp.route('/setting', methods=['POST'])
def POST_setting():
    try:
        data = JSONencoder.load(request.data)
        if not 'language-setting' in data and data['language-setting'] in SUPPORTED_LANGUAGES:
            raise APIexception("POST /language/setting expects 'language-setting' in payload as 'en' or 'es'")
        
        session['language-setting'] = data['language-setting']
        return respond200()
    except Exception as e:
        return respond500(e)


@bp.route('/setting')
@jsonp
def GET_language_setting():
    try:
        data = {'language-setting': session.get('language-setting', None)}
        return dumpJSON(data)
    except Exception as e:
        return respond500(e)


@bp.route('/setting/clear', methods=['DELETE', 'POST', 'GET', 'PUT'])
def clear_setting():
    """
    Clear the language setting from the session - not actually used by module
    """
    try:
        session['language-setting'] = None
        return respond200()
    except Exception as e:
        return respond500(e)

#-------------------------------------------------- Language Setting -


@bp.route('/map')
@jsonp
def GET_map():
	try:
		data = get_map()
		return dumpJSON(data)
	except Exception as e:
		return respond500(e)


























