"""python 3/ Windows OS
Usage:
    python swipe.py
"""
import os, sys
from selenium import webdriver
from selenium.webdriver.chrome.options import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pprint import pprint as pp
import autoit
import time
from random import randrange
import urllib.request as urllib
from os.path import join, isdir
e=sys.exit

IMAGE_LOC='images'
if not isdir(IMAGE_LOC):
    os.makedirs(IMAGE_LOC)
    

assert 'T_PWD' in os.environ
assert 'T_USERNAME' in os.environ
T_PWD=os.environ.get('T_PWD').strip('"')
T_USERNAME=os.environ.get('T_USERNAME').strip('"')
assert T_PWD
assert T_USERNAME

SAY_SOMETHING_NICE='Hey gorgeous ;)'


#e()
home = os.path.dirname(sys.argv[0])
if not home or not home.strip('.'):
    home = os.path.dirname(os.path.abspath(__file__))


driverpath = r".\driver\nt\chromedriver_86.exe"

phototext = """
#infinite swipe right for Tinder
"""

class dict2(dict):                                                              

	def __init__(self, **kwargs):                                               
		super(dict2, self).__init__(kwargs)                                     

	def __setattr__(self, key, value):                                          
		self[key] = value                                                       

	def __dir__(self):                                                          
		return self.keys()                                                      

	def __getattr__(self, key):                                                 
		try:                                                                    
			return self[key]                                                    
		except KeyError:                                                        
			raise AttributeError(key)                                           

	def __setstate__(self, state):                                              
		pass 
        
        
options = Options()
options.add_argument("--log-level=3")
options.add_argument("--silent")
#options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-logging")
options.add_argument("--mute-audio")
#mobile_emulation = {"deviceName": "Nexus 5"}
#options.add_experimental_option("mobileEmulation", mobile_emulation)
options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')


def popups(driver):
    try:  #allow location
        driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]/span').click()
        #time.sleep(1)
    except:
        print('Ignoring location.')
    try: #allow message notifications
        driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]/span').click()
        #time.sleep(1)
    except:
        print('Ignoring message notifications.')
    try:  #accept cookies
        driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button/span').click()
        #time.sleep(1)
    except:
        print('Ignoring cookies.')

    try: #Upgrade Your Like

        driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/button[2]').click()
    except:
        print('Passing on "Upgrade Your Like".')
    try: #Add Tinder to your Home Screen
        add=[]
        add.append('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        add.append('//*[@id="modal-manager"]/div/div/button[2]')
        for a in add:
            try:
                driver.find_element_by_xpath(a).click()
                break
            except:
                print('pass on "Add Tinder to your Home Screen" id: %d' % a)
    except:
        print('Passing on "Add Tinder to your Home Screen".')
    
    err='Say something nice'
    try: 
        
        frm = driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/div[3]/form')
        if frm:
            pp(dir(frm))
            err +=', Ta search'
            ta= frm.find_elements(By.XPATH, '//*[@id="chat-text-area"]')
            err +=', send_keys'
            ta[0].send_keys(SAY_SOMETHING_NICE)
            pp(dir(ta))
            err +=', send'
            driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/div[3]/form/button').click()
    except Exception as ex:
        print('Passing on: ', err)
        print(str(ex))
        

    time.sleep(1)
def save_images(imgs, conf):
    for uid, url in enumerate(imgs):
        print('Saving:', url)
        fname= url.split('/')[-1].strip('/')
        if conf.age:
            fname = '%s.%s' % (conf.age, fname)        
        if conf.name:
            fname = '%s.%s' % (conf.name, fname)
        try:
            urllib.urlretrieve(url, join(IMAGE_LOC,fname))
            print('Image ',uid, fname, 'is saved.')
        except Exception as ex:
            print('Passing on: ',uid, fname)
            print(str(ex))

        
if __name__=="__main__":
    #//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button/span/svg/path
    name=''
    age=''
    if 1:
        driver = webdriver.Chrome(executable_path=driverpath,options=options)
        driver.get("https://tinder.com/")
        
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button').click()
        time.sleep(2)
        if 0:
            driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[3]/button/span[2]').click()
            time.sleep(1)
            phone=driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div[2]/div/input')
            phone.click()
            time.sleep(.2)
            phone.send_keys("2125183000")
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[1]/div/button/span[2]').click()
        
        driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[1]/div/button').click()
        time.sleep(2)
        if 0:
            email=driver.find_element_by_xpath('//*[@id="identifierId"]')
            email.click()
            time.sleep(.2)
            email.send_keys("olek.buzu@gmail.com")
        if 0:
            email=driver.find_elements_by_class_name("whsOnd zHQkBf");
            print(email)
            print(dir(email[0]))
            email.click()
            time.sleep(.2)
            email.send_keys("olek.buzu@gmail.com")
        import autoit
        title="Sign in - Google Accounts - Google Chrome"
        autoit.win_active(title)
        time.sleep(1)
        autoit.send(T_USERNAME)
        time.sleep(.5)
        autoit.send('{ENTER}')
        time.sleep(2)
        autoit.send(T_PWD)
        time.sleep(.5)
        autoit.send('{ENTER}')
        time.sleep(4)
        if 0:
            go = input("Continue?")
            if go=='y':
                pass
            else:
                exit(1)
  
        #swipe right
        while True:
            name=None
            is_vertical=False
            popups(driver)
            rt=[]
            rt.append([False,'//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button'])
            rt.append([True,'//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[4]/button']) #zoom
            #rt.append('//*[@id="content"]/div/div[1]/div/div/main/div/div/div[2]/div/div/div[4]/button')
            #rt.append('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[2]/div/div/div[4]/button')
            for rid,r in enumerate(rt):
                try:
                    print('trying id:' ,rid, r)
                    is_vertical, xpath = r
                    driver.find_element_by_xpath(xpath).click()
                    print('Right OK: %d' % rid)
                    break
                except:
                    print('swipe right id ', rid, 'failed')
            else:
                go = input("Restart?")
                if go=='y':
                    pass
                else:
                    exit(1)
                            
            secs = randrange(2,5)
            print('Sleep for ', secs)
            time.sleep(secs)
            popups(driver)

            
            if 1: # get name
                nm=[]
                nm.append('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[4]/div/div[1]/div/div/span')
                nm.append('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[3]/div/div[1]/div/div[1]/span')
                nm.append('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[1]/div[3]/div[3]/div/div[1]/div/div/span')
                for sid,s in enumerate(nm):
                    try:
                        name=driver.find_element_by_xpath(s).text
                        print('%d: Name: %s' %  (sid,name))
                        break
                    except:
                        print("Passing on name: %d" % sid)
                
                if 0: #get name
                    q='//div[@itemprop="name"]'
                    elem=driver.find_elements_by_xpath(q);
                    name=elem[0].text
                    print('GOT NAME: ', name)
                
                        
            if 1: # get age
                sp=[]
                sp.append('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[3]/div/div[1]/div/span[2]')

                for sid,s in enumerate(sp):
                    try:
                        age=driver.find_element_by_xpath(s).text
                        print('%d: Age: %s' % (sid,age))
                        break
                    except:
                        print("Passing on age: %d" % sid)
            if 0: #inspect
                b='//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[3]/button'
                driver.find_element_by_xpath(b).click()
                time.sleep(.5)
                b='//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]/div/div/div[2]/div[1]/div[2]'
                country= driver.find_element_by_xpath(b)
                print('Country:', country.text)

                if 1: #uninspect
                    b='//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[1]/span/a'
                    driver.find_element_by_xpath(b).click()
            tid=2
            tabs={2:'//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[1]/div[2]/button[2]',
            3:'//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[1]/div[2]/button[3]',
            4:'//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[1]/div[2]/button[4]',
            5:'//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[1]/div[2]/button[5]',
            6:'//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[1]/div[2]/button[6]',
            7:'//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[1]/div[2]/button[7]',
            8:'//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[1]/div[2]/button[8]',
            9:'//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[1]/div[2]/button[9]',
            10:'//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[1]/div[2]/button[10]'}
            
            vtabs={2:'//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[1]/div[3]/div[1]/div[2]/button[2]',
            3:'//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[1]/div[3]/div[1]/div[2]/button[3]',
            4:'//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[1]/div[3]/div[1]/div[2]/button[4]',
            5:'//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[1]/div[3]/div[1]/div[2]/button[5]',
            6:'//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[1]/div[3]/div[1]/div[2]/button[6]',
            7:'//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[1]/div[3]/div[1]/div[2]/button[7]',
            8:'//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[1]/div[3]/div[1]/div[2]/button[8]',
            9:'//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[1]/div[3]/div[1]/div[2]/button[9]',
            10:'//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[1]/div[3]/div[1]/div[2]/button[10]'}
            imgs=[]
            if is_vertical: tabs= vtabs

            while True:
                try:
                   
                    #print(1234)
                    q='//div[@aria-label="%s"]' % name
                    q='//div[@class="Bdrs(8px) Bgz(cv) Bgp(c) StretchedBox"]'
                    #<div aria-label="Алина" class="Bdrs(8px) Bgz(cv) Bgp(c) StretchedBox" style="background-image: url(&quot;https://images-ssl.gotinder.com/5ddc37ba765537010079ba4c/640x800_75_2862c0c0-a74b-4765-b7e1-de16f3ac833d.webp&quot;); background-position: 50% 50%; background-size: auto 100%;"></div>
                    #<div aria-label="Виктория" class="Bdrs(8px) Bgz(cv) Bgp(c) StretchedBox" style="background-image: url(&quot;https://images-ssl.gotinder.com/5e42fa918a3ff0010014fc70/640x800_75_93efa0a9-b58f-48c9-b711-2ef9b5de92ec.webp&quot;); background-position: 50% 50%; background-size: auto 100%;"></div>
                    
                    
                    #print(3456, q)
                    
                    #pp(dir(driver))
                    elem=driver.find_elements_by_xpath(q);
                    #print(len(elem), elem)
                    assert elem
                    for el in elem:
                        #pp(dir(el))
                        #print(el.tag_name, el.text)
                        style=el.get_attribute('style')
                        alabel=el.get_attribute('aria-label')
                        
                        #pp(style)
                        img =  style.split('url("')[1].split('");')[0]
                        #print(name, '>>>>>>>>>>>',alabel, img)
                        assert img
                        if img not in imgs:
                            if alabel.strip().lower() == name.strip().lower():
                                imgs.append(img.strip('"'))
                        #print('imgs len:', len(imgs))
                    
                    if 0:
                        go = input("C?")
                        if go=='y':
                            pass
                        else:
                            exit(1)
                except:
                    raise
                #<div aria-label="" class="Bdrs(4px)" style="background-image: url(&quot;https://scontent-iad3-1.cdninstagram.com/v/t51.29350-15/121966268_717132778872784_3736837487942066695_n.jpg?_nc_cat=100&amp;ccb=2&amp;_nc_sid=8ae9d6&amp;_nc_ohc=bDJ-Jyk-Vh8AX8v3cOU&amp;_nc_ht=scontent-iad3-1.cdninstagram.com&amp;oh=3e222f0350a24d2422a992e6f831a0a2&amp;oe=5FEF5DE3&quot;); background-position: 50% 50%; background-size: auto 124.93%;"></div>
                #<div aria-label="Елизавета" class="Bdrs(8px) Bgz(cv) Bgp(c) StretchedBox" style="background-image: url(&quot;https://images-ssl.gotinder.com/5fce955c95fef0010067bc16/640x800_75_4f13f9af-d30e-481c-af82-0e2126998c6a.webp&quot;); background-position: 50% 0%; background-size: 168.421%;"></div>
                try:
                    print('Trying tab: %d' % tid)
                    driver.find_element_by_xpath(tabs[tid]).click()
                    print('Tab ok: %d' % tid)

                    try: #try video
                        
                        driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[1]/div[1]/span[3]/div[2]/div').click()

                    except:
                        print('Not a video: %d' % tid)
                    tid +=1
                    time.sleep(5)
                except Exception as ex:
                    print('Exiting tabs: %d' % tid)
                    print(str(ex))
                    if imgs:
                        save_images(imgs, dict2(name=name, age=age))
                    break
            time.sleep(.5)

