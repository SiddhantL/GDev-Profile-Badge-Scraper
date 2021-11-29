"""
This Script is created by @Siddhant Lad
"""
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.chrome.options import Options

def remove_tags(html):
    soup = BeautifulSoup(html, "html.parser")
    for data in soup(['style', 'script']):
        data.decompose()

    return ' '.join(soup.stripped_strings)
df = pd.read_csv('test.csv')
df1 = df[['url', 'name','email']]
saved_column = df.url
paragraphs = ""
name=[]
badges=[]
email=[]
total=[]
scores=[]

introtokot=[]
firstapinas=[]
buildbasiclay=[]
diceroller=[]
getuip1=[]
getuip2=[]
scrollist=[]
navscreen=[]
navcomp=[]
archcom=[]
navapp=[]
coroutine=[]
displayinternet=[]
sql=[]
datapers=[]
workmanager=[]

for v,w,z in zip(df1.url,df1.name,df1.email):
    paragraphs=""
    introtokotstr = "No"
    firstapinasstr = "No"
    buildbasiclaystr = "No"
    dicerollerstr = "No"
    getuip1str = "No"
    getuip2str = "No"
    scrolliststr = "No"
    navscreenstr = "No"
    navcompstr = "No"
    archcomstr = "No"
    navappstr = "No"
    coroutinestr = "No"
    displayinternetstr = "No"
    sqlstr = "No"
    datapersstr = "No"
    workmanagerstr = "No"
    score = 0
    total = "No"
    options = Options()
    options.headless = True
    wd = webdriver.Chrome(options=options)
    responce = wd.get(v)
    name.append(w)
    email.append(z)
    time.sleep(8)  # page loads completely
    soup = BeautifulSoup(wd.page_source, 'lxml')
    div = soup.find_all('div', {'class':'badge-title'})
    badgelist=""
    for x in div:
        badgelist=remove_tags(str(x))+", "+badgelist
        paragraphs=paragraphs+(str(x))
    #modify the if statements according to your badges which you need to look for
    if "Introduction to Kotlin" in paragraphs:
        introtokotstr="Yes"
        score=score+1
    if "First App in Android Studio" in paragraphs:
        firstapinasstr="Yes"
        score=score+1
    if "Build a Basic Layout" in paragraphs:
        buildbasiclaystr="Yes"
        score=score+1
    if "Dice Roller App" in paragraphs:
        dicerollerstr="Yes"
        score=score+1
    if "Part 1" in paragraphs:
        getuip1str="Yes"
        score=score+1
    if "Part 2" in paragraphs:
        getuip2str="Yes"
        score=score+1
    if "Scrollable List" in paragraphs:
        scrolliststr="Yes"
        score=score+1
    if "Navigate between screens" in paragraphs:
        navscreenstr="Yes"
        score=score+1
    if "Navigation component" in paragraphs:
        navcompstr="Yes"
        score=score+1
    if "Architecture component" in paragraphs:
        archcomstr="Yes"
        score=score+1
    if "Advanced navigation" in paragraphs:
        navappstr="Yes"
        score=score+1
    if "Coroutines" in paragraphs:
        coroutinestr="Yes"
        score=score+1
    if "data from the internet" in paragraphs:
        displayinternetstr="Yes"
        score=score+1
    if "SQL" in paragraphs:
        sqlstr="Yes"
        score=score+1
    if "data persistence" in paragraphs:
        datapersstr="Yes"
        score=score+1
    if "WorkManager" in paragraphs:
        workmanagerstr="Yes"
        score=score+1
    introtokot.append(introtokotstr)
    firstapinas.append(firstapinasstr)
    buildbasiclay.append(buildbasiclaystr)
    diceroller.append(dicerollerstr)
    getuip1.append(getuip1str)
    getuip2.append(getuip2str)
    scrollist.append(scrolliststr)
    navscreen.append(navscreenstr)
    navcomp.append(navcompstr)
    archcom.append(archcomstr)
    navapp.append(navappstr)
    coroutine.append(coroutinestr)
    displayinternet.append(displayinternetstr)
    sql.append(sqlstr)
    datapers.append(datapersstr)
    workmanager.append(workmanagerstr)
    if introtokotstr and firstapinasstr and buildbasiclaystr and dicerollerstr and getuip1str and getuip2str and scrolliststr and navscreenstr and navcompstr and archcomstr and navappstr and coroutinestr and displayinternetstr and sqlstr and datapersstr and workmanagerstr == "Yes":
        total="Yes"
    scores.append(score)
    paragraphs = paragraphs + "<br><br>"
    badges.append(badgelist)
dict = {'Name': name,'Email':email, 'Badges': badges,'Introduction to Kotlin':introtokot,'First App in Android Studio':firstapinas,'Build Basic Layout':buildbasiclay,'Dice Roller App':diceroller,'Get User Input 1':getuip1,'Get User Input 2':getuip2,'Scroll List':scrollist,'Navigation Screen':navscreen,'Navigation Components':navcomp,'Architecture Components':archcom,'Navigation App':navapp,'Coroutine':coroutine,'Display Internet':displayinternet,'SQL':sql,'Data Persistence':datapers,'Work Manager':workmanager, 'Score Out of 16':scores,'All Badges':total}
df = pd.DataFrame(dict)
df.to_csv('datasheet.csv')
paragraphs=remove_tags(paragraphs)
