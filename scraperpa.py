

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
i = 0

urls = ['url_to_scrape']
for url in urls:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all the member profile urls then visits the profile and gets the points
    tags = soup.find_all("a",class_="liste")
    for tag in tags:
        if i < 10: #for testing purposes
            try:
                print(tag.contents[0].contents[0].contents[0])
            except:
                print(tag.contents[0])
            print(tag.get('href',None))
            memberurl = "url_to_scrape"+tag.get('href', None);
            memberhtml = urllib.request.urlopen(memberurl, context=ctx).read()
            membersoup = BeautifulSoup(memberhtml, 'html.parser')
            membertag = membersoup.find_all('tr')
            print(membertag[13].contents[1].contents[0].contents[0].contents[0])
            i += 1 #for testing purposes
