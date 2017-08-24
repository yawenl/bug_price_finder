#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import urllib2
from BeautifulSoup import BeautifulSoup

def ensure_unicode(v):
    if isinstance(v, str): v = v.decode('utf8')
    return unicode(v)  # convert anything not a string to unicode too

                    



    #%% ########################################## Class for getting posts you want ###################################
class DealmoonPost:
    id = 0
    home_url = "http://cn.dealmoon.com/"
    url = "dealmoon.com" 
    title = "No TITLE"
        
    def __init__( self, id_, title_ ):
        self.id = id_
        self.title = ensure_unicode( title_ )
        self.url = self.home_url  + str( self.id ) + ".html"
        self.url = ensure_unicode( self.url )
        

        
    def __repr__(self):
        return self.__unicode__( )

        
    def __unicode__(self):
        return self.title.encode('utf-8')  + " : " + self.url.encode('utf-8') 

    

    #%% ########################################## Detecting Deals on Dealmoon ###################################

class DealmoonPriceFinder:
    #%% ########################################## Member Constant ###################################
    home_url = "http://cn.dealmoon.com/"
    keywords =  ["bug", "错误" , "买一送",  "买1送", "疑似" ]
    num_pages_to_detect = 5
    
    sent_posts = [] # posts that we already sent in the past
    
    htmls = []

 
    #%% ########################################## Member Function ###################################
    def __init__( self, num_page = 5  ):
        self.num_pages_to_detect = num_page
        self.set_up_sent_posts()
        
    def set_up_sent_posts( self ):
        try:
            f = open("previous_posts.data", "rb")
        except: 
            return # databse doesn't exist. Ignore loading data.
        
        for line in f:
            self.sent_posts.append( line.strip().rstrip() )
        f.close()
        
    def write_existing_posts_to_database( self ):
        f = open("previous_posts.data", "wb")
        for _ in self.sent_posts:
            f.write( _ + "\n" )
        f.close()
    
    
    def detect_prices( self ):
        """
        Return an array of DealmoonPosts, which matches the "keywords"
        """
        rst = []
        
        print "\n\nBegin detecting price in", self.home_url, "now", "for", self.num_pages_to_detect, "pages"
 
        for i in range( self.num_pages_to_detect ):
            t_url = self.home_url + "?p=" + str( i + 1 )
        

            html = urllib2.urlopen( t_url )
            soup = BeautifulSoup( html )
            
            all_links = soup.findAll('a')
            

            for link in all_links:
                onclick = link.get( "onclick" )
                if not onclick: continue # There is not a "onclick" feature on the href.
            
                    
                # Get the post id of the post
                try:
                    id = re.search( "statistics.event_statistics_view\((\d+)", onclick ).group(1)
                except:
                    #  this is not a dealmoon post. it may be an ads or a link to wechat, etc
                    continue

                
                # Get the title of the post
                if link.string: # Case that the "title" of post is in the <a>
                    title = set( link.string )
                else: # Case that the title of post is in <span> section of the <a>
                    soup2 = BeautifulSoup( str(link) )
                    spans = soup2.findAll( "span", text = True )
                    # There might be multiple <span>, title, subtitle, etc
                    # "text = True" means we only care about the text of the HTMl element.
                    
                    if not spans: continue # we don't have any span property in <a>
                    

                    titles = set()
                    for _ in spans: 
                        _ = _.strip().rstrip()
                        if _ : titles.add( _ )


                if len( titles ) == 0 : continue # no title find in this <a> href.

                # Now, we have titles array (including title, subtitle, etc),
                # we want combine everything into one string
                title = ""
                for _ in titles: title += _
                title = title.lower()
                title = ensure_unicode( title )
          

                title_has_keywords = False
                for k in self.keywords:
                    k = k.lower()
                    k = ensure_unicode( k )
                    try:
                        if title.find( k ) >= 0:
                            title_has_keywords = True
                            break
                    except Exception as e:
                        print e
                        print title
                        print k
                
                if title_has_keywords:
                    if id not in self.sent_posts:
                        post = DealmoonPost( id, title )
                        rst.append( post )
                        self.sent_posts.append( id )
         
  
        self.write_existing_posts_to_database()
        
        print "Done detecting prices. There are", len(rst), "findings\n\n"
        return rst
    
