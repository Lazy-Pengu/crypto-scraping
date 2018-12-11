"""Collection of classes for doing my project"""
import requests as r
from time import sleep

class UrlCreator():
    """
    This class provides the information requested by the user from CoinMarketCap API
    
    Attributes
    ----------
    BASE_URL : str
        The base url link for the CoinMarketCap API
    FINAL_URL : str
        Final url link to access the specific info on the CoinMarketCap API
    final_json_response: dict
        Final data retrieved from the CoinMarketCap API 
    """
    
    def __init__(self):
        """
        Constructor for the UrlCreator class that sets the base url of the API
        """
        #Base url to access coinMarketCap API
        self.BASE_URL = "https://api.coinmarketcap.com/v1/ticker/"
        self.FINAL_URL = None
        
        self.final_json_response = None
        
    def get_name_listing(self):
        """
        Function to get the list crytocurrency from the base url of the API
        
        Returns
        -------
        cryt_name_list: list
            List of crytocurrencies the user can select from
        """
        #Request information from the url passed in and stores the info
        response = r.get(self.BASE_URL)
        json_response = response.json()
        
        #Stores the name of the crytocurrencies into a list
        index = 0
        crypt_name_list = []
        while index < len(json_response):    
            crypt_name_list.append(json_response[index]['id'])
            index+=1

        #Returns the list of crytocurrency names
        return crypt_name_list
    
    def get_keys(self):
        """
        Function to get the list of keys from the final url of the API
        
        Returns
        -------
        crypt_key_list: list
            List of crytocurrency attributes the user can select from
        """
        #Requests info from the url passed in and stores it
        response = r.get(self.FINAL_URL)
        self.final_json_response = response.json()
        
        #Gets the list of keys of the info
        crypt_key_list = list(self.final_json_response[0].keys())
        
        return crypt_key_list
    
    def get_answer(self, attribute):
        """
        Function to get the value of the specfic attribute passed in
        
        Parameters
        ----------
        attribute: str
            Attribute to get the value from
            
        Returns
        -------
        self.final_json_response: str
            The current value of the requested attribute
        """
        return self.final_json_response[0][attribute] 
    
    def set_url(self, crypt_type):
        """
        Function that sets the specific url to get the attribute of the type requested
        
        Parameters
        ----------
        crypt_type: str
            Name of the crytocurrency to get add to the base url
        """
        self.FINAL_URL = self.BASE_URL + crypt_type 
       
import time 
import sys
import smtplib #Email server library

from email.mime.text import MIMEText #Text object for creating the email

class EmailInfo():
    """
    This class provides the functionality for the user to send an email message to a 
    specified recipient
    
    Attributes
    ----------
    user_name: str='cogs18.dummyAcc@gmail.com'
        Email address to be used to send the email
    password: str='somethingeasy'
        Password to be used to access email address
    stmp: smtplib
        smtp server
    msg: MIMEText
        Message that will be sent
    """
    
    def __init__(self, user_name='cogs18.dummyAcc@gmail.com', password='somethingeasy'):
        """
        Constructor to set up the username and password of the email that will be used to 
        send the email
        
        Parameters
        ----------
        user_name: str
            Email address that will be used to send the email
        password: str
            Password to access the email address
            
        """
        #Stores values for email and password to set up server
        self.user_name = user_name
        self.password = password
        
        self.stmp = None
        self.msg = None
        
    def setup_server(self):
        """
        Function that sets up the email address with given password
        
        Returns
        -------
        succeeded: bol
            Statement of whether the email server setup was successful
        """

        try:
            print("\nSETTING UP SMTP MAIL SERVER.\n")
            # Set up the SMTP server & login
            self.smtp = smtplib.SMTP('smtp.gmail.com', 587)

            # Note: sometimes ttls has to be turned off (?)
            self.smtp.starttls()
            self.smtp.ehlo()
            self.smtp.login(self.user_name, self.password)
            succeeded = True
        except:
            succeeded = False
        
        return succeeded
                
    def setup_email(self, receiving_email, subject, msg_to_send):
        """
        Function that creates the email message to be send to the specified email address 
        
        Parameters
        ----------
        receiving_email: str
            Email address of the recipient
        subject: str
            Subject of the email message
        msg_to_send: str
            Actual message that will be sent
        """
        
        # Create the msg outline & set contents
        print("CREATING EMAIL.")
        time.sleep(2)
        self.msg = MIMEText(msg_to_send)
        self.msg['From'] = self.user_name
        self.msg['To'] = receiving_email
        self.msg['Subject'] = subject

        # Check out the email
        print("\nPRINT OUT CREATED EMAIL:\n")
        print(self.msg)

        time.sleep(4)

    
    def send_email(self):
        """
        Function that sends the email message 
        """
        # Send message
        print("SENDING EMAIL")
        self.smtp.send_message(self.msg)
        time.sleep(1)
        print('EMAIL SENT!')
        
        
        