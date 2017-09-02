#!/usr/bin/python
# -*- coding: utf-8 -*-
import json


from fbchat import Client
from fbchat.models import *

class FBManager():
    
    #### Memmber Variables
    receiver_ids = []
    login_id = ''
    login_pwd = ''
    session_cookies = {}
    
    
    
    #### Member Functions
    def __init__( self, username, password ):
        """
        asdfassdfasdf only run this once, otherwies..... fb will.
        """
        self.login_id = username
        self.login_pwd = password
        
        # Try to load session cookie
        try:
            self.session_cookies = json.load( open("session_cookie.json", "r") )
        except:
            # Session Cookie doesn't exist
            pass
        
        
    def login( self ):
        self.client = Client( self.login_id, self.login_pwd, session_cookies = self.session_cookies )
        
        # save login session as cookie if such cookie doesn't exists
        if len( self.session_cookies ) == 0:
            self.session_cookies = self.client.getSession()
            f = open("session_cookie.json", "w")
            json.dump( self.session_cookies, f )
            f.close()
        
        

    
    def set_receiver_ids(self, receivers):
        """
        setup FB accounts that want the deals messages sent to them
        """
        self.receiver_ids = receivers
        
        
    def send_message(self, message):
        """
        Call API to send message
        """
        for r in self.receiver_ids:
            self.client.sendMessage(message, thread_id=r, thread_type=ThreadType.USER)
