import requests
from bs4 import BeautifulSoup
import smtplib
import time

# url of the product to be parsed (not all the webpage will work)
url = '''https://www.amazon.in/Canon-EOS-6D-Mark-II/dp/B0749MNH83/ref=sr_1_6?crid=ZA85PTPZXKBG&keywords=canon+80d+dslr+camera&qid=1562179327&s=gateway&sprefix=canon+%2Caps%2C407&sr=8-6'''
header = {"user agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

def price_drop():

	page = requests.get(url, headers=header)                             # requests for the web page
	soup = BeautifulSoup(page.content, "html.parser")                    # parsing the page
	price = soup.find(id="priceblock_ourprice").get_text()               # find the priceblock_ourprice for the of the product
	price = price.replace(',' , '')                                      # parsing the price string into numbers from string 
 	print(price)
	d_price = float(price)
	if (d_price < 73900):                                                # checks for price less than actual price
		send_mail()
  if (d_price > 73900):                                                # just for checking the program 
		send_mail()


def send_mail():

  # connect to the gmail server
	server = smtplib.SMTP("smtp.gmail.com", 587)                         # 587 is the port number for the gmail
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login('mail_id', 'password')                                  # login using your mail id and password
	subject='price droped'
	body= 'https://www.amazon.in/Canon-EOS-6D-Mark-II/dp/B0749MNH83/ref=sr_1_6?crid=ZA85PTPZXKBG&keywords=canon+80d+dslr+camera&qid=1562179327&s=gateway&sprefix=canon+%2Caps%2C407&sr=8-6'
	message = f"subject:{subject}\n\n{body}"
	server.sendmail('from mail id','to mail id',message)
	print('mail sent')
	server.quit()                                                        # quit from the server


count = 0
whilte count <= 7:                                                     # run the program for 7 days 

  price_drop()
  time.sleep(60*60*24)                                                
  count += 1                                                          
