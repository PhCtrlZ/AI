import speech_recognition
import pyttsx3
from datetime import date
from datetime import datetime
import webbrowser
import subprocess,json,time
import requests
import os
import ctypes	
import winshell
from colorama import Fore, Back, Style
import socket
import sys
robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain=""
PDV=""

os.system("cls")
print(Fore.GREEN+"đang checking kết nối mạng")
try:
    requests.get('https://www.google.com/').status_code
    print(Fore.GREEN+"Connected to internet is successfully")
    pass
except:
	print(Fore.RED+"Connected to internet is not successfully please check your internet connection again ")
	print(Style.RESET_ALL)
	time.sleep(5)
	exit()

class ProgressBar(object):
    DEFAULT_BAR_LENGTH = 75
    DEFAULT_CHAR_ON  = '='
    DEFAULT_CHAR_OFF = ' '

    def __init__(self, end, start=0):
        self.end    = end
        self.start  = start
        self._barLength = self.__class__.DEFAULT_BAR_LENGTH

        self.setLevel(self.start)
        self._plotted = False

    def setLevel(self, level):
        self._level = level
        if level < self.start:  self._level = self.start
        if level > self.end:    self._level = self.end

        self._ratio = float(self._level - self.start) / float(self.end - self.start)
        self._levelChars = int(self._ratio * self._barLength)

    def plotProgress(self):
        sys.stdout.write("\r  %3i%% [%s%s]" %(
            int(self._ratio * 100.0),
            self.__class__.DEFAULT_CHAR_ON  * int(self._levelChars),
            self.__class__.DEFAULT_CHAR_OFF * int(self._barLength - self._levelChars),
        ))
        sys.stdout.flush()
        self._plotted = True

    def setAndPlot(self, level):
        oldChars = self._levelChars
        self.setLevel(level)
        if (not self._plotted) or (oldChars != self._levelChars):
            self.plotProgress()

    def __add__(self, other):
        assert type(other) in [float, int], "can only add a number"
        self.setAndPlot(self._level + other)
        return self
    def __sub__(self, other):
        return self.__add__(-other)
    def __iadd__(self, other):
        return self.__add__(other)
    def __isub__(self, other):
        return self.__add__(-other)
    def __del__(self):
        sys.stdout.write("\n")

if __name__ == "__main__":
    count = 150
    print ("Loadding tool...")
    pb = ProgressBar(count)
    for i in range(0, count):
        pb += 1
        time.sleep(0.01)
    del pb

    print ("done")

b ="sever"
r = requests.get('your api')
r = json.loads(r.text)
start = "\033[1m"
end = "\033[0;0m"

try:
	key = r[b]
	if key == True:
		mess=r['message']
		print(Fore.GREEN+start+mess+end)
		print(Fore.GREEN+start+"Connected to sever is successfully"+end)
		time.sleep(1)
		print("Sever sẽ đóng vào 12h->7h30 sáng để bảo trì")
		time.sleep(1)
		print(Fore.GREEN+start+"sever is open"+end)
		time.sleep(1)
		print(Fore.GREEN+start+"Loading...!"+end)
		time.sleep(1)
		print(Style.RESET_ALL)
		print(Style.RESET_ALL)
		print(Style.RESET_ALL)
		print(Style.RESET_ALL)
		print("""
_________    __           .__   __________
\_   ___ \ _/  |_ _______ |  |  \____    /
/    \  \/ \   __\\_  __ \|  |    /     / 
\     \____ |  |   |  | \/|  |__ /     /_ 
 \_______/ |__|   |__|   |____//_________\
                                       

""")
		print(Fore.CYAN+"""
                                                                 ÛÛ
                                                                ÛÛ  
                                                              ÛÛ 
                                                                            
                        ±Û          ÛÛÛÛÛÛÛÛÛ  ÛÛÛ   ÛÛÛ  ÛÛÛ   ÛÛÛ   ÛÛÛÛÛÛÛÛÛ         
                          Û         ÛÛÛ   ÛÛÛ  ÛÛÛ   ÛÛÛ  ÛÛÛ   ÛÛÛ   ÛÛ            
                           ²Û       ÛÛÛÛÛÛÛÛÛ  ÛÛÛÛÛÛÛÛÛ  ÛÛÛ   ÛÛÛ   ÛÛ             
                          Û         ÛÛÛ        ÛÛÛ   ÛÛÛ  ÛÛÛ   ÛÛÛ   ÛÛ           
                        ±Û   ²²²²²  ÛÛÛ        ÛÛÛ   ÛÛÛ  ÛÛÛÛÛÛÛÛÛ   ÛÛÛÛÛÛÛÛÛ   
                                          Tool change mode:on   

                                           """)
		print(Style.RESET_ALL)



		while True:
			with speech_recognition.Microphone() as mic:
				print("Trợ lí ảo : i'm listening")
				audio = robot_ear.record(mic,duration=6)
				print("Trợ lí ảo :...")
			try:
				you = robot_ear.recognize_google(audio)
			except:
				you =""
				print("You:" + you)
			if you =="":
				robot_brain=""
				PDV=""			
			elif you == "hello":
				robot_brain="Hello Phuc,I am smart robot"
				PDV="Xin chào tôi là robot thông minh"
			elif "you can help me" in you:
				robot_brain="how can i help you"
				PDV="Tôi có thể giúp bạn như thế nào" 
			elif "thank you" in you:
				robot_brain="No problem"
				PDV="Không có gì"
			elif "how are you" in you:
				robot_brain=" i'm fine, thanks"
				PDV="tôi khỏe ,cảm ơn"
			elif "what time is it now" in you:
				now= datetime.now()
				robot_brain = now.strftime("%H:%M:%S")
				print("Giờ hiện tại=", robot_brain)
			elif "what date is today" in you:
				today = date.today()
				robot_brain= today.strftime("%B %d, %Y")
				d1=date.today()
				PDV= today.strftime("%d/%m/%Y")
			if "opening youtube" in you.lower() :
				url = "https://www.youtube.com/"
				robot_brain="okay"
				runprf= webbrowser.open_new_tab(url)
				PDV="=))))"
			if "open my favorite music please" in you.lower() :
				url = "https://www.youtube.com/watch?v=xypzmu5mMPY"
				robot_brain = "okay"
				runprf=webbrowser.open_new_tab(url)
				PDV="Được thôi,Vui lòng chờ ..."
			elif "how is the weather today" in you.lower():
				url="https://www.google.com/search?q=weather&oq=weather&aqs=chrome..69i57j0i402j46i433j0i433j0j0i433j0j69i60.2662j0j7&sourceid=chrome&ie=UTF-8"
				robot_brain="please wait "
				runprf = webbrowser.open_new_tab(url)
				PDV="Chờ tôi chút"
			if "good night" in you.lower():
				robot_brain="Okay Good night"
				PDV="Ngủ ngon!!!"
			if "shut down computer" in you.lower():
				robot_brain="computer will shutdown now!!!"
				PDV="máy tính sẽ tắt ngay bây giờ"
				os.system('shutdown -s')
			if "opening facebook" in you.lower():
				url="https://www.facebook.com/"
				robot_brain="okay"
				runprf=webbrowser.open_new_tab(url)
				PDV="Được thôi"
			if "i love you" in you.lower():
				robot_brain="I love you too "
				PDV="Tôi cũng yêu bạn nè "
			if "i'm so sad" in you.lower():
				robot_brain="Do something comfortable like taking a bath or sleeping"
				PDV="Hãy làm việc gì đó làm thoải mái cơ thể ví dụ như là tắm hoặc là ngủ"
			if "search google" in you.lower():
				robot_brain="Please enter what you want to search for"
				PDV="Vui lòng nhập thứ mà bạn muốn tìm kiếm trên google"
				url="https://www.google.com.vn/"
				runprf = webbrowser.open_new_tab(url)
			if "opening goole translate" in you.lower():
				robot_brain="Please wait"
				url="https://translate.google.com/?hl=vi"
				PDV="Chờ chút"
				runprf = webbrowser.open_new_tab(url)
			if "computer speed up" in you.lower():
				robot_brain="work done"
				PDV="đã xong công việc"
				os.system("powercfg -h off>nul")
				os.system("del /f /s /q %temp%")
				os.system("del /f /s /q %windir%\prefetch\ ")
				os.system("ipconfig /all")
				os.system("ipconfig /flushdns")
				os.system("ipconfig /release")
				os.system("ipconfig /renew")
				os.system("Netsh int tcp show global")
				os.system("Netsh int tcp set global chimney=enabled")
				os.system("Netsh int tcp set global autotuninglevel=normal")
				os.system("Netsh int set global congestionprovider=ctcp ")
				os.system("netsh interface tcp set global autotuning=disable")
				os.system("netsh interface tcp set heuristics disabled")
				os.system("netsh int ip reset c:\resetlog.txt")
				os.system("EmptyStandbyList.exe workingsets")
				os.system("mptyStandbyList.exe modifiedpagelist")
				os.system("EmptyStandbyList.exe priority0standbylist")
				os.system("EmptyStandbyList.exe standbylist")
			if "delete windows old" in you.lower():
				robot_brain="Delete windows old is start now"
				PDV="Xóa windows cũ bắt đầu ngay bây giờ"
				os.system("del RD /S /Q %SystemDrive%\windows.old\ ")
			if "turn on windows defender" in you.lower():
				robot_brain="Okay"
				PDV="Được luôn"
				os.system("netsh advfirewall set allprofiles state on")
				os.system("netsh advfirewall set currentprofile state on")
				os.system("netsh advfirewall set domainprofile state on")
				os.system("netsh advfirewall set publicprofile state on")
				os.system("netsh advfirewall set privateprofile state on")
			if "turn off windows defender" in you.lower():
				robot_brain="Okay"
				PDV="được luôn"
				os.system("netsh advfirewall set allprofiles state off")
				os.system("netsh advfirewall set currentprofile state off")
				os.system("netsh advfirewall set domainprofile state off")
				os.system("netsh advfirewall set publicprofile state off")
				os.system("netsh advfirewall set privateprofile state off")
			if "lock my screen" in you:
				robot_brain="Your screen will lock now"
				PDV="màn hình của bạn sẽ khóa sau 5s"
				time.sleep(5)
				ctypes.windll.user32.LockWorkStation()
				print("Trợ lí ảo :"+robot_brain)
				print("You:"+you)
				print("Phiên Dịch viên :"+PDV)
				robot_mouth.say(robot_brain)
				robot_mouth.runAndWait()
				break
			if "clear my bin" in you:
				robot_brain="Your bin in computer will clear trash now"
				PDV="rác của trong máy tính của bạn sẽ bị dọn sạch ngay"
				winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
				print("đã dọn sạch rác")
			if "open Microsoft Access" in you:
				robot_brain="Okay"
				PDV="Được thôi" 
				s=os.startfile("C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\MSACCESS.EXE")
			if "open Microsoft Word" in you:
				robot_brain="Okay"
				PDV="Được thôi"
				f = os.startfile("C:\\Program Files (x86)\\Microsoft Office\\root\\Office16/WINWORD.EXE") 
			if "open Microsoft OneNote" in you:
				robot_brain="Okay"
				PDV="Được thôi"
				f = os.startfile("C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\ONENOTE.EXE") 
			if "open Microsoft Excel" in you:
				robot_brain="Okay"
				PDV="Được thôi"
				f = os.startfile("C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL.EXE") 
			if "open Microsoft Publisher" in you:
				robot_brain="Okay"
				PDV="Được thôi"
				f = os.startfile("C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\MSPUB.EXE") 
			if "open Microsoft Outlook" in you:
				robot_brain="Okay"
				PDV="Được thôi"
				f = os.startfile("C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE")
			if "open Microsoft Powerpoint" in you:
				robot_brain="Okay"
				PDV="Được thôi"
				f = os.startfile("C:/Program Files (x86)/Microsoft Office/root/Office16/POWERPNT.EXE")
			if "open Google" in you:
				robot_brain="Okay"
				PDV="Được thôi"
				f=os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe") 
			if "open Teamviewer" in you:
				robot_brain="Okay"
				PDV="Được thôi"
				f=os.startfile("C:\\Program Files\\TeamViewer\\TeamViewer.exe")
			if "open Garena" in you:
				robot_brain="Okay"
				PDV="Được thôi"
				f=os.startfile("C:\\Program Files (x86)\\Garena\\Garena\\Garena.exe") 
			if "open Microsoft Edge" in you:
				robot_brain="Okay"
				PDV="Được thôi"
				f=os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
			if "Contact" in you:
				url5="https://mail.google.com/mail/u/0/#sent?compose=GTvVlcSHxjNTDBtJNWHVzvsPKHVNhNDKQbMmwGKqlJkNxcwDMwkPxWNKpvJtRmJxsSVCkPDqgTChS"
				runprf=webbrowser.open_new_tab(url5)
			if "f***" in you:
				robot_brain="Please Calm Down and control your speech"
				PDV="Vui lòng bình tĩnh và kiểm soát lời nói của bạn"
				print("Trợ lí ảo :"+robot_brain)
				print("You:"+you)
				print("Phiên Dịch viên :"+PDV)
				robot_mouth.say(robot_brain)
				robot_mouth.runAndWait()
				break
			elif "bye" in you:
				robot_brain="Goodbye"
				PDV="Tạm biệt "
				print("Trợ lí ảo :"+robot_brain)
				print("You:"+you)
				print("Phiên Dịch viên :"+PDV)
				robot_mouth.say(robot_brain)
				robot_mouth.runAndWait()
				break
			print("Trợ lí ảo:"+robot_brain)
			print("You:"+you)
			print("Phiên Dịch viên :"+PDV)
			robot_mouth.say(robot_brain)
			robot_mouth.runAndWait()

	elif key == False:
		os.system("cls")
		error=r['error']
		error2=r['error2']
		error3=r['error3']
		print(Fore.RED+error)
		print(Fore.RED+error2)
		print(Fore.RED+error3)
		print(Style.RESET_ALL)
		time.sleep(10)
		exit()

except:
	os.system("cls")
	error=r['error']
	error2=r['error2']
	error3=r['error3']
	print(Fore.RED+error)
	print(Fore.RED+error2)
	print(Fore.RED+error3)
	print(Style.RESET_ALL)
	time.sleep(10)
	exit()