from subprocess import call                                    
import time                                                    
import random                                                       
                                                                    
# colors                                                                 
red = '\u001b[31m'                                                              
green = '\u001b[32m'                                                            
blue = '\u001b[34m'
cyan = '\u001b[36m'
aus_server_list = ['AU#13', 'AU#14', 'AU#15', 'AU#16', 'AU#17', 'AU#18', 'AU#19']

print(f"""
{green}[{red}^{green}]please run as sudo {green}[{red}^{green}]
{red}[{green}1{red}] connects randomly every 15 mins 
{red}[{green}2{red}] connects randomly every 30 mins 
{red}[{green}3{red}] connects through Secure Core
{red}[{green}4{red}] connects to fastest server
{red}[{green}5{red}] connects to popular servers
{red}[{green}6{red}] connects to fastest server in random country
{green}[{red}00{green}] exit
""")
select = input(f'select option:{red} ')

def aus_connect():
        call(f'protonvpn c {random.choice(aus_server_list)}')

if select == '1':
        start = True
        while start:
                call("protonvpn c -r", shell=True)
                time.sleep(900)

elif select == '2':
        start = True
        while start:
                call("protonvpn c -r", shell=True)
                time.sleep(1800)

elif select == '00':
        exit()

elif select == '3':
        call("protonvpn c --sc ", shell=True)

elif select == '4':
        call('protonvpn c -f', shell=True)

elif select == '5':
        try:
                aus_connect()
        except:
                call(f'protonvpn c {random.choice(aus_server_list)}')


elif select != "":
        print(f'{green}[{red}^{green}]please select valid option{green}[{red}^{green}]{red}')

