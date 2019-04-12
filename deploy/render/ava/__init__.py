# -*- coding: utf-8 -*-
from render.ava.default import Render as default
from render.ava.user import Render as user
from server.render.html.utils import jinjaGlobalFunction,jinjaGlobalFilter
from server import utils,exposed,errors,request
import logging

@exposed
def index( *args, **kwargs ):
	if not utils.getCurrentUser():
		raise errors.Redirect("/ava/user/auth_userpassword/login")
	elif not canAccess():
		raise errors.Forbidden()
	else:
		r = default()
		return( r.view( None, tpl="index") )

def canAccess( *args, **kwargs ):
	user = utils.getCurrentUser()

	if user:
		if ("root" in user["access"]):
			return( True )
		else:
			return( False )

	pathList = request.current.get().pathlist

	if len( pathList )>=2 and pathList[1] == "skey":
		# Give the user the chance to login :)
		return( True )
	if len( pathList )>=3 and pathList[1] == "user" and \
		(pathList[2] == "auth_userpassword" or
		 pathList[2] == "auth_googleaccount" or
		 pathList[2] == "auth_timebasedotp"):
		# Give the user the chance to login :)
		return( True )
	if len( pathList ) == 1:
		raise errors.Redirect("/ava/user/auth_userpassword/login")
	return( False )

def _postProcessAppObj( obj ):
	obj.index = index
	obj.canAccess = canAccess
	return obj



@jinjaGlobalFilter
def isList(render, val):
	return isinstance(val, list)

@jinjaGlobalFilter
def isDict(render, val):
	return isinstance(val, dict)

@jinjaGlobalFunction
def getAdminConf(render):
	from server import conf
	import json
	adminTree = conf["viur.mainApp"]

	adminConfig = {}
	for key in dir( adminTree ):
		app = getattr( adminTree, key )
		if "adminInfo" in dir( app ) and app.adminInfo:
			if callable( app.adminInfo ):
				info = app.adminInfo()
				if info is not None:
					adminConfig[ key ] = info
			else:
				adminConfig[ key ] = app.adminInfo.copy()
				adminConfig[ key ]["name"] = _(adminConfig[ key ]["name"])
				adminConfig[ key ]["views"] = []
				if "views" in app.adminInfo:
					for v in app.adminInfo["views"]:
						tmp = v.copy()
						tmp["name"] = _(tmp["name"])
						adminConfig[ key ]["views"].append( tmp )
	res = {	"capabilities": conf["viur.capabilities"],
		"modules": adminConfig,
		"configuration": {}
		}
	for k, v in conf.items():
		if k.lower().startswith("admin."):
			res["configuration"][ k[ 6: ] ] = v
	return json.dumps( res )
