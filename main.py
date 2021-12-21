"""                                                             
.-----.----.-----.--.--.--.--.    .-----.----.----.---.-.-----.-----.
|  _  |   _|  _  |_   _|  |  |    |__ --|  __|   _|  _  |  _  |  -__|
|   __|__| |_____|__.__|___  |    |_____|____|__| |___._|   __|_____|
|__|                   |_____|                          |__|         

        Scrapes proxies i guess, needs work.
        Create a pull request if you want to fix it :)
"""


import os, time, requests
from pystyle import Colorate, Colors
os.system('cls & mode 83, 22')


class Scraper:
    
    banner = """
      .-----.----.-----.--.--.--.--.    .-----.----.----.---.-.-----.-----.
      |  _  |   _|  _  |_   _|  |  |    |__ --|  __|   _|  _  |  _  |  -__|
      |   __|__| |_____|__.__|___  |    |_____|____|__| |___._|   __|_____|
      |__|                   |_____|                          |__|

             """
    print(Colorate.Vertical(Colors.red_to_white, banner, 1))
    input("Press enter to scrape proxies. ")
    r = requests.get(f"https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all")
    f = open('proxies.txt','wb')
    f.write(r.content)
    f.close()

print('Scraped proxies.')
input()
