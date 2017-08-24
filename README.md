# Bug Price Finder
-------------------------

There are many websites that are posting extremely good deals. I'm using Dealmoon a lot. Yesterday there was a deal for a really good hair dryer that takes down the price from $190 to $20 and I missed it because I didn't subcribe to the noticifications from Dealmoon. The reason is that it also pushes some deals I don't care much and if I keep it buzzing, it is annoying. However, when it comes to the deal I really want, deals go away even before I notice. So I decide to write my own deal detector.

This detector will send you noticification through Facebook's Messenger. The code uses Python 2.7. I'm using fbchat library for sending messages (https://fbchat.readthedocs.io/en/master/) and BeautifulSoup (https://www.crummy.com/software/BeautifulSoup/) for website parsing. I'm using cookie sessions to keep the login active.

The only file missing is fb_login_info.txt. In this file, the first line is a Facebook's account email at and its password is at the second line. This is the account that is used to send noticification to accounts who need the deals. The 3rd line and everything after it should be FB id that you want the deals to sent to. Every id occupies one line.

Then you just start "python main.py" and the detection would run every 3 minutes. You can set the frequency in the code. Since Dealmoon involves Chinese in it, you HAVE to have Chinese UTF-8 supported on your enviroment.

This detector is specilized to Dealmoon, but I saparated every module and you can change the content parser and keywords you need to make it work for other websites. I didn't write the parser suitable for every website similar to Dealmoon since their format are just too different from each other.