import requests
def checker():
    ssid = input("Enter SSID: ")
    user = input("Enter username: ")
    cookies = {
        'entry_url': 'https://myaccount.ea.com/cp-ui/aboutme/index?gameId=ebisu',
        'JSESSIONID': f'{ssid}',
        'cp-cookie': '"596c8d7b5f2e89ba"',
        'ealocale': 'en-us',
        'notice_behavior': 'implied,eu',
        'notice_location': 'be',
        'ak_bmsc': 'FAF1D9BF14FC9094AB8A2ECE15AA052D~000000000000000000000000000000~YAAQpsURAjuJ06yFAQAASQJWyxLErAyNS51ksdl8qMYyjCWAzKvlflACm7h2Qt0bYjG3Py8yRshPsEE0LXa3BKw+M8dg+92/c9SPFfyrbCRtv4xhc54nStfiQ7CsKzgNIUiv4svgBih/lF33o4fzRKZUWyuXqN+KfJx7ukmkEnqex1KQPN7+HT1pFkBnjqr+a5iRyayuFbCoJkMK/W4nxiyIaDwey4Mp3PBZN50gqCDqoyCSFlZC359yavawnzxM/lnhSRiUmg+o+0A76XBQJH92OKSifTPQyewdw9UYJNSgclUq9gqZah7p3/jfkxtspxXeU9P9y0p330xk4vNkfbt4RCecc1xsyXLCxMmvTLcq6s+E0OAnVQaTc80xRDA4uwppt7YoPJ8Hv4MplTAqYEvxjFOjCi1+SkG6fkSDVYzRxiPPxrlZe1Rs7jVvyQ+uZK69ysZQsxoLrI8rI/BABe0IqGnJVHteuSQsUeC8EQCO0Ah0nYVtXw==',
        'notice_gdpr_prefs': '0,1,2:',
        'cmapi_cookie_privacy': 'permit 1,2,3',
        'cmapi_gtm_bl': '',
        'notice_preferences': '2:',
        'notice_poptime': '1599001200000',
        '_gid': 'GA1.2.165319214.1674153691',
        '_nx_mpcid': 'd164fcde-6846-42c7-875e-5cf78c16f2f7',
        '_gcl_au': '1.1.1691610957.1674153729',
        'bm_sv': '83A33E13C4DF520698F178E847B93DC7~YAAQpsURAlWV06yFAQAAeJ5WyxLdkRj9WrE7uZvIP8N37DkaZmNXkrPD82FragPFk7aVHl/FGYHEe8kxmArIoIjqnz7XzLA06QPztz1hB9WIxtGAz/cNtRC7OfDZf4DfhwntYqy7O4M6K55idl/fFGf60/PU96JqUgwDIVmkAvHDavEhkqB7o4tLcnyZfK12yj+LOQQVJ88P9hYM6nm770NKTvf//jHCQC2mEbN3BH3vngeZZuHhi3j3LXM=~1',
        '_ga': 'GA1.2.1565018874.1674153691',
        '_ga_Q3MDF068TF': 'GS1.1.1674153729.1.0.1674153735.54.0.0',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.9,nl-NL;q=0.8,nl;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://myaccount.ea.com',
        'Referer': 'https://myaccount.ea.com/cp-ui/aboutme/index?gameId=ebisu',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'b04a8359-b5ed-4f06-b266-8d293f2510b6',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'originId': f'{user}',
    }

    r = requests.post(
        'https://myaccount.ea.com/cp-ui/aboutme/validateCheckOriginId',
        cookies=cookies,
        headers=headers,
        data=data,
    ).json()
    if r['status'] == False:
        print(f"{user} Taken")
    elif r['status'] == True:
        print(f"{user} Available")
checker()