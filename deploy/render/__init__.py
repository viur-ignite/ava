from server.render import admin, html, json, vi, xml



@html.utils.jinjaGlobalFilter
def isList(render, val):
	return isinstance(val, list)

@html.utils.jinjaGlobalFilter
def isDict(render, val):
	return isinstance(val, dict)

@html.utils.jinjaGlobalFunction
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
