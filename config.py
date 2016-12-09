import sys
import os
import datetime
import subprocess

from keyhac import *

def configure(keymap):	
	# かなキーのキーコード
	modifier_key = "(104)" 
	# 漢字直接入力で使う40文字のキーコード
	to_be_modified_keys = [
		18,19,20,21,23,22,26,28,25,29,
		12,13,14,15,17,16,32,34,31,35,
		0,1,2,3,5,4,38,40,37,41,
		6,7,8,9,11,45,46,43,47,44
	]
	# "#"キー
	prefix_key = "Shift-3"
	
	keymap_global = keymap.defineWindowKeymap()
	keymap.defineModifier(modifier_key, "User0")
	# ワンショットモディファイヤ
	keymap_global["O-"+modifier_key]=modifier_key
	
	# prefix_keyの後に元のキーが押されたものとみなす
	for key in to_be_modified_keys:
		keymap_global["User0-("+str(key)+")"] = (lambda key : (lambda : keymap.InputKeyCommand(prefix_key, "("+str(key)+")")()))(key)
