#!/usr/bin/python
# -*- coding: utf-8 -*-
import time

from dealmoon_bug_detector import DealmoonPost, DealmoonPriceFinder
from fb_login import FBManager

# Login Information
f = open( "fb_login_info.txt", "rb" )

username = f.readline().strip().rstrip()
password = f.readline().strip().rstrip()
receiver_id = []
for line in f: receiver_id.append( line.strip().rstrip() )
f.close()

# Create FB Object
fb  = FBManager( username, password )
fb.login()
fb.set_receiver_ids( receiver_id )


# create dealmoon object
finder = DealmoonPriceFinder( 2 )


# run it every 5 mins
while True:
    finding_rst = finder.detect_prices()
    
    print finding_rst
    
    
    msg = ""
    for post in finding_rst:
        msg += ( post.title + " : " + post.url + "\n" )
        
    if len( msg ) > 0:
        fb.send_message( msg )
        
    print "..."
    time.sleep( 60 * 3 ) 

    
    
print "All Done ~ Have a nice day!"
    
#%% debug code
#count = 0
#for _ in finder.htmls:
#    count += 1
#    f = open( "temp{}.html".format(count) ,  "wb" )
#    f.write( html )
#    f.close()