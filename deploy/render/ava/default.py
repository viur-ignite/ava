# -*- coding: utf-8 -*-
import os,logging
from server.render.html.default import Render as htmldefault
from server import request, errors

class Render(htmldefault):
	htmlpath = "ava"

	def getTemplateFileName( self, template, ignoreStyle=False ):
		validChars = "abcdefghijklmnopqrstuvwxyz1234567890-"
		if "htmlpath" in dir( self ):
			htmlpath = self.htmlpath
		else:
			htmlpath = "html"
		if not ignoreStyle\
			and "style" in request.current.get().kwargs\
			and all( [ x in validChars for x in request.current.get().kwargs["style"].lower() ] ):
				stylePostfix = "_"+request.current.get().kwargs["style"]
		else:
			stylePostfix = ""
		lang = request.current.get().language #session.current.getLanguage()
		fnames = [ template+stylePostfix+".html", template+".html" ]
		if lang:
			fnames = [ 	os.path.join(  lang, template+stylePostfix+".html"),
						template+stylePostfix+".html",
						os.path.join(  lang, template+".html"),
						template+".html" ]
		logging.error(fnames)
		for fn in fnames: #check subfolders
			prefix = template.split("_")[0]
			if os.path.isfile(os.path.join(os.getcwd(), htmlpath, prefix, fn)):
				return ( "%s/%s" % (prefix, fn ) )
		for fn in fnames: #Check the templatefolder of the application
			logging.error(os.path.join( os.getcwd(), htmlpath, fn ))
			logging.error(os.path.isfile( os.path.join( os.getcwd(), htmlpath, fn ) ))
			if os.path.isfile( os.path.join( os.getcwd(), htmlpath, fn ) ):
				self.checkForOldLinePrefix( os.path.join( os.getcwd(), htmlpath, fn ) )
				return (fn)
		for fn in fnames: #Check the fallback
			if os.path.isfile( os.path.join( os.getcwd(), "server", "template", fn ) ):
				self.checkForOldLinePrefix( os.path.join( os.getcwd(), "server", "template", fn ) )
				return( fn )
		raise errors.NotFound( "Template %s not found." % template )

