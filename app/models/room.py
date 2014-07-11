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
# Room Model
# 	_id		{ObjectId}
# 	_list 	{ObjectId}	<- list._id of owner list
# 	name
# 	type 				<- icon etc
# 	tasks 	{array}
#
#--------------------------------------------------------------------------------
#*********************************************************************************


from bson import ObjectId

from app.database import db
from . import stamp_last_modified



def find(id=None, _list=None):
	query = {}
	if id:
		query['_id'] = ObjectId(id)
	elif _list:
		query['_list'] = ObjectId(_list)
	return [r for r in db.rooms.find(query)]

def insert_new(list_id, data=None):
	"""
	@param {ObjectId} list_id
	Returns _id of newly inserted room 
	"""
	data = data if data else {}
	data["_list"] = list_id
	data["tasks"] = []
	data = stamp_last_modified(data)
	return db.rooms.insert(data)

def update(id, data):
	# TODO - RAISE ERROR for unsatisfactory write result ?
	data = stamp_last_modified(data)
	ret = db.rooms.update({ "_id": ObjectId(id) }, { "$set": data})
	return ret

def add_task(id, task_data):
	ret = db.rooms.update({ "_id": ObjectId(id) }, { "$push": {"tasks": task_data }})
	return ret

def delete(id):
	"""
	1) delete _list's reference to room
	2) delete room document itself
	"""
	# 0) get room document to have reference it its _list
	r = db.rooms.find({ "_id": id })
	if not r:
		raise Exception("Cannot delete room with _id {0} - no such document".format(id))
	# 1) delete _list's reference to it
	db.lists.update({ "_id": r["_list"] }, { "$pull": { "rooms": id }})
	
	# 2) delete room document
	db.rooms.remove({ "_id": ObjectId(id) })
	

