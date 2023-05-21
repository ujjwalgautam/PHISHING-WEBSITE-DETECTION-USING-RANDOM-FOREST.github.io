import whois
import subprocess
import ipaddress
from urllib.parse import urlparse,urlencode
import re

import re
from bs4 import BeautifulSoup
#import whois
import urllib
import urllib.request


#-------------------------------------------------1---------------------------------------
def havingIP(url):
  url1=urlparse(url).netloc
  # print(url1)
  try:
    ipaddress.ip_address(url1)
    ip = 1
  except:
    ip = 0
  return ip

# print("having url=",havingIP("youtube.com"))
# print("having url=",havingIP("14.140.233.72"))


#-------------------------------------------------2---------------------------------------
def haveAtSign(url):
  # print("2")
  try:
    if "@" in url:
      at = 1    
    else:
      at = 0    
    return at
  except:
    return 1

# print("having @=",haveAtSign("medium.com"))

#-------------------------------------------------3---------------------------------------

def getLength(url):
  # print("3")
  try:
    if len(url) < 54:
      length = 0            
    else:
      length = 1            
    return length
  except:
    return 1

# print("Url length=",getLength("icicibank.com"))


#-------------------------------------------------4---------------------------------------

# 4.Gives number of '/' in URL (URL_Depth)...url depth
def getDepth(url):
  # print("4")
  s = urlparse(url).path.split('/')
  depth = 0
  for j in range(len(s)):
    if len(s[j]) != 0:
      depth = depth+1
  return depth

# print("Url depth=",getDepth("https://thenextweb.com/jdfskhg/hjdfs"))


#-------------------------------------------------5---------------------------------------
# 5.Checking for redirection '//' in the url (Redirection)


def redirection(url):
  # print("5")
  pos = url.rfind('//')
  if pos > 6:
    if pos > 7:
      return 1
    else:
      return 0
  else:
    return 0

# print("redirection=",redirection("https://www.youtube.com//jg"))

#-------------------------------------------------6---------------------------------------
# 6.Existence of “HTTPS” Token in the Domain Part of the URL (https_Domain)


def httpDomain(url):
  # print("6")
  domain = urlparse(url).netloc
  if 'https' in domain or 'http' in domain:
    return 1
  else:
    return 0


# print("http/https=",httpDomain("https://www.youtube.comhttp//jg"))


#-------------------------------------------------7---------------------------------------

#listing shortening services
# 8. Checking for Shortening Services in URL (Tiny_URL)





def tinyURL(url):
  # print("7")
  shortening_services = r"bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|" \
                      r"yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|" \
                      r"short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|" \
                      r"doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|db\.tt|" \
                      r"qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|q\.gs|is\.gd|" \
                      r"po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|x\.co|" \
                      r"prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|" \
                      r"tr\.im|link\.zip\.net"
  match=re.search(shortening_services,url)
  if match:
      return 1
  else:
      return 0

# print("tinyurl=",tinyURL("youtube.com"))
# print("tinyurl=",tinyURL("wwedvm.appspot.com"))

#-------------------------------------------------8---------------------------------------


def prefixSuffix(url):
  # print("8")
  
  if '-' in url:
      return 1            # phishing
  else:
      return 0            # legitimate

# print("prefixsuffix",prefixSuffix("youtube.com"))
# print("prefixsuffix",prefixSuffix("appleid.apple.com-sa.pm"))

#-------------------------------------------------9---------------------------------------
#check dns record

# url="youtubey.com"
# import dns.resolver
  
# # Finding AAAA record

# record=0
# try:
#     result = dns.resolver.resolve(url, 'A')
#     print("re=",result)
#     for val in result:
#         print('AAAA Record : ', val.to_text())
# except:
#     record=1
# # Printing record


# print("record=",record)

#-------------------------------------------------10---------------------------------------

def web_traffic(url):
    parsed_url = urlparse(url)

    # Extract netloc (www.example.com)
    original_string=parsed_url.netloc
    # print(original_string)
    # Extract domain name
    try:
      query= original_string.split(".")[1]
    except:
       return 1
    # print("query=",query)
    url = "https://www.google.com/search?q="+query
    response = requests.get(url)

    # Use BeautifulSoup to parse the HTML of the search results page
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all of the URLs in the search results
    sites = []
    for a in soup.find_all("a", href=True):
        if a["href"].startswith("/url?q="):
            url = a["href"].replace("/url?q=", "")
            try:
              site = url.split("/")[2]
              sites.append(site)
            except:
              print()

    # Print the top 5 sites
    for site in set(sites[:5]):
        check= site.split(".")[1]
        check2 = site.partition(".")[0]
        if(query==check or query==check2):
            return 0

    return 1

#-------------------------------------------------11---------------------------------------

import datetime

# 13.Survival time of domain: The difference between termination time and creation time (Domain_Age)  

# import whois



def Domain_age(url):
  # print("10")
  try:
    w = whois.whois(url)
  except:
    return 1

  expiration_date = w.expiration_date
  if type(expiration_date)==list:
      expiration_date=expiration_date[0]



  creation_date = w.creation_date
  if creation_date==None:
    return 1
  if type(creation_date)==list:
      creation_date=creation_date[0]

  try:
    ageofdomain = abs((expiration_date - creation_date).days)
  except:
    return 1
  if ((ageofdomain/30) <6):
      return 1
  else:
      return 0
    
# print(Domain_age("youtube.com"))

    


#-------------------------------------------------12---------------------------------------

from datetime import datetime


def Domain_end(url):
  # print("11")
  try:
    w = whois.whois(url)
  except:
    return 1

  expiration_date = w.expiration_date
  if expiration_date==None:
    return 1
  if type(expiration_date)==list:
      expiration_date=expiration_date[0]

  ageofdomain = abs((expiration_date - datetime.now()).days)
  if ((ageofdomain/30) <6):
      return 1
  else:
      return 0
    




#-------------------------------------------------13---------------------------------------

import requests
from bs4 import BeautifulSoup

def iFrame(url):
    # print("12")
    try:
        response = requests.get(url)
    except:
        return 1
    soup = BeautifulSoup(response.text, 'html.parser')
    iframe = soup.iframe

    if iframe==None:
        return 0
    try:
      frameborder = iframe['frameborder']
    except:
      return 0
    if frameborder==0:
        return 1
    else:
        return 0

# url = 'https://www.ncell.axiata.com/en'
# print("iframe=",iFrame(url))

#-------------------------------------------------14---------------------------------------
import requests

def mouseOver(response): 
  # print("13")
  if response == "" :
    return 1
  else:
    if re.findall("<script>.+onmouseover.+</script>", response.text):
      return 1
    else:
      return 0

# url = 'https://www.ncell.axiata.com/en'
# response = requests.get(url)



#-------------------------------------------------15---------------------------------------
import requests

def rightClick(response):
  # print("14")
  if response == "":
    return 1
  else:
    if re.findall(r"event.button ?== ?2", response.text):
      return 1
    else:
      return 0

# url = 'https://www.ncell.axiata.com/en'
# response = requests.get(url)
# print("right click=",rightClick(response))

#-------------------------------------------------16---------------------------------------
import requests

def forwarding(response):
  # print("15")
  if response == "":
    return 1
  else:
    if len(response.history) <= 2:
      return 0
    else:
      return 1


# response = requests.get(url)
# print("webfor=",forwarding(response))


def featureExtraction(url):
  import pandas as pd
  from urllib.parse import urlparse
  features = []
  #Address bar based features (10)
  #features.append(getDomain(url))
  
  features.append(havingIP(url))
  features.append(haveAtSign(url))
  features.append(getLength(url))
  features.append(getDepth(url))
  features.append(redirection(url))
  features.append(httpDomain(url))
  features.append(tinyURL(url))
  features.append(prefixSuffix(url))
  
  #Domain based features (4)

  import dns.resolver
  
# Finding AAAA record
  import dns.resolver
  from urllib.parse import urlparse
  dnss=0
  url1=urlparse(url).netloc
  try:
      domain_name = dns.resolver.resolve(url1, 'A')
  except:
      dnss=1

 

  features.append(dnss)
  # features.append(web_traffic(url))
  features.append(web_traffic(url))
  features.append(1 if dnss == 1 else Domain_age(url))
  features.append(1 if dnss == 1 else Domain_end(url))
  
  # HTML & Javascript based features

  features.append(iFrame(url))
  try:
    response = requests.get(url)
  except:
    response = ""
  features.append(mouseOver(response))
  features.append(rightClick(response))
  features.append(forwarding(response))


 
  # # # Convert the array to a DataFrame
  # df = pd.DataFrame(features, columns=['Domain', 'Have_IP', 'Have_At', 'URL_Length', 'URL_Depth','Redirection', 
  #                     'https_Domain', 'TinyURL', 'Prefix/Suffix', 'DNS_Record', 'Web_Traffic', 
  #                     'Domain_Age', 'Domain_End', 'iFrame', 'Mouse_Over','Right_Click', 'Web_Forwards', 'Label'])

  # # # Append the DataFrame to an existing CSV file
  # df.to_csv('example.csv', mode='a', header=False, index=False)
  
  return features



# print(featureExtraction("	https://www.facebook.com"))