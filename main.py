"""                                                             
.-----.----.-----.--.--.--.--.    .-----.----.----.---.-.-----.-----.
|  _  |   _|  _  |_   _|  |  |    |__ --|  __|   _|  _  |  _  |  -__|
|   __|__| |_____|__.__|___  |    |_____|____|__| |___._|   __|_____|
|__|                   |_____|                          |__|         

        Scrapes proxies i guess, needs work.
        Create a pull request if you want to fix it :)
"""


import os, time, requests
from pystyle import Colorate, Colors, Box, Center
os.system('cls & mode 83, 22')


class Scraper:
    
    text = """
    1. Red to White
    2. Red to Blue
    3. Blue to White
    4. Blue to Cyan
    5. Blue to purple
    """
    banner = """
      .-----.----.-----.--.--.--.--.    .-----.----.----.---.-.-----.-----.
      |  _  |   _|  _  |_   _|  |  |    |__ --|  __|   _|  _  |  _  |  -__|
      |   __|__| |_____|__.__|___  |    |_____|____|__| |___._|   __|_____|
      |__|                   |_____|                          |__|

             """
    print(Colorate.Horizontal(Colors.rainbow, Center.XCenter(Box.SimpleCube(content=text)), 1))
    kkk = input(Colorate.Horizontal(Colors.rainbow, "Theme; ", 1))
   
    if kkk == "1":
     print(Colorate.Horizontal(Colors.red_to_white, banner, 1))
     input(Colorate.Horizontal(Colors.red_to_white, "Press enter to scrape proxies. ", 1))
     r = requests.get(f"https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all")
     f = open('proxies.txt','wb')
     f.write(r.content)
     f.close()

     print(Colorate.Horizontal(Colors.red_to_white, 'Scraped proxies.', 1))
     input()
     os._exit(0)

    if kkk == "2":
     print(Colorate.Horizontal(Colors.red_to_blue, banner, 1))
     input(Colorate.Horizontal(Colors.red_to_blue, "Press enter to scrape proxies. ", 1))
     r = requests.get(f"https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all")
     f = open('proxies.txt','wb')
     f.write(r.content)
     f.close()

     print(Colorate.Horizontal(Colors.red_to_blue, 'Scraped proxies.', 1))
     input()
     os._exit(0)

    if kkk == "3":
     print(Colorate.Horizontal(Colors.blue_to_white, banner, 1))
     input(Colorate.Horizontal(Colors.blue_to_white, "Press enter to scrape proxies. ", 1))
     r = requests.get(f"https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all")
     f = open('proxies.txt','wb')
     f.write(r.content)
     f.close()

     print(Colorate.Horizontal(Colors.blue_to_white, 'Scraped proxies.', 1))
     input()
     os._exit(0)

    if kkk == "4":
     print(Colorate.Horizontal(Colors.blue_to_cyan, banner, 1))
     input(Colorate.Horizontal(Colors.blue_to_cyan, "Press enter to scrape proxies. ", 1))
     r = requests.get(f"https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all")
     f = open('proxies.txt','wb')
     f.write(r.content)
     f.close()
     print(Colorate.Horizontal(Colors.blue_to_cyan, 'Scraped proxies.', 1))
     input()
     os._exit(0)

    if kkk == "5":
     print(Colorate.Horizontal(Colors.blue_to_purple, banner, 1))
     input(Colorate.Horizontal(Colors.blue_to_purple, "Press enter to scrape proxies. ", 1))
     r = requests.get(f"https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all")
     f = open('proxies.txt','wb')
     f.write(r.content)
     f.close()
 
     print(Colorate.Horizontal(Colors.blue_to_purple, 'Scraped proxies.', 1))
     input()
     os._exit(0)

    if kkk != "1" or "2" or "3" or "4" "5":
     print(Colorate.Horizontal(Colors.rainbow, "bruh", 1))

