#-*- coding: utf-8 -*-
from server.skeleton import Skeleton, RelSkel
from server.bones import *

class xntestRelSkel(RelSkel):
	name = stringBone(descr="Str")

class xntestSkel(Skeleton):
	# Defaults
	strbone = stringBone(descr="StringBone")
	strbone_hidden = stringBone(descr="StringBone Hidden",visible=False)
	strbone_readonly = stringBone(descr="StringBone Readonly",readOnly=True)
	strbone_multiple = stringBone(descr="StringBone Mulitple",multiple=True)
	strbone_lang= stringBone(descr="StringBone Lang", multiple=False,languages=["de", "en"])
	strbone_multiple_lang = stringBone(descr="StringBone Multiple Lang", multiple=True, languages=["de", "en"])

	numbone = numericBone(descr="NumericBone")

	basbone = baseBone(descr="baseBone")
	boolbone = booleanBone(descr="booleanBone")
	capbone =captchaBone(descr="captchaBOne")
	colorbone = colorBone(descr="ColorBone")
	credbone = credentialBone(descr="CredentialBone")
	databone = dateBone(descr="Datebone")
	mailbone = emailBone(descr="EmailBone")
	filebone = fileBone(descr="FileBone")
	filebone_multiple = fileBone(descr="FileBone",multiple=True)
	hierbone = hierarchyBone(descr="HierarchyBone",kind="example")
	keybone = keyBone(descr="KeyBOne")
	pwdbone = passwordBone(descr="passwordBone")
	rndslicebone = randomSliceBone(descr="randomSliceBone")
	relbone = relationalBone(descr="relbone",kind="example")
	relbone_multiple = relationalBone(descr="relbone multi", kind="example")
	relbone_using = relationalBone(descr="relbone using", kind="example", using=xntestRelSkel)
	relbone_multiple_using = relationalBone(descr="relbone multi using", kind="example", using=xntestRelSkel, multiple=True)
	selectbone = selectBone(descr="selectBone",values={"0":"0","1":"1"})
	selectbone_multiple = selectBone(descr="selectBone multi",multiple =True, values={"0": "0", "1": "1"})
	selectcountrybone = selectCountryBone(descr="SelectCountybone")
	statialbone = spatialBone(descr="SpatialBone",boundsLat=(23,23),boundsLng=(24,24),gridDimensions=(10,30))
	textbone = textBone(descr="text")
	textbone_lang = textBone(descr="text lang", languages=["de","en"])
	treedirbone =treeDirBone(descr="treedirbone",kind="file")
	treeitembone = treeItemBone(descr="treeitembone", kind="file")
	usrbone = userBone(descr="userBone")






