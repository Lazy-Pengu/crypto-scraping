"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from classes import UrlCreator, EmailInfo

from email.mime.text import MIMEText

##
##
API_access = UrlCreator()
email = EmailInfo()

def test_url():

    assert API_access.set_url('bitcoin') == None
    assert API_access.FINAL_URL == "https://api.coinmarketcap.com/v1/ticker/bitcoin"
    
    assert isinstance(API_access.get_name_listing(), list)
    assert isinstance(API_access.get_keys(), list)
    
    assert isinstance(API_access.get_answer('id'), str)
    assert API_access.get_answer('id') == 'bitcoin'
    
    
    
def test_email():
    assert email.user_name == 'cogs18.dummyAcc@gmail.com'
    assert email.password == 'somethingeasy'
    
    assert isinstance(email.setup_server(), bool)
    assert email.setup_server() == True
    
    assert email.setup_email('dummyEmail@gmail.com', 'dummySubject', 'dummyMsg') == None
    assert isinstance(email.msg, MIMEText)
    
    assert email.msg['From'] == 'cogs18.dummyAcc@gmail.com'
    assert email.msg['To'] == 'dummyEmail@gmail.com'
    assert email.msg['Subject'] == 'dummySubject'
   
    
    
