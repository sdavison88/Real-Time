import os
from googleapiclient.discovery import build
from oauth2client.client import SignedJwtAssertionCredentials
import httplib2
import datetime
import time
import sys

        
        scope = ['https://www.googleapis.com/auth/analytics.readonly']
        service_account_email = 't-mobile@t-mobile-1203.iam.gserviceaccount.com'
        key_file_location = 'newfile.key.pem'
        api_name ='analytics'
        api_version ='v3'
        gametrics ="rt:activeusers"
        f = open(key_file_location, 'rb')
        key = f.read()
        f.close()

        credentials = SignedJwtAssertionCredentials(service_account_email, key,scope=scope)

        http = credentials.authorize(httplib2.Http())
        service = build(api_name, api_version, http=http)

     
        web_activeusers = 0
        amoe_activeusers = 0
        ios_activeusers = 0
        andriod_activeusers = 0

        
        web_pageviews = 0
        amoe_pageviews = 0

        ios_screenviews = 0
        andriod_screenviews = 0

        ios_totalevents = 0
        andriod_totalevents = 0

        
         # number of points to be plotted

        # Delay start of stream by 5 sec (time to switch tabs)
        #time.sleep(1)
        xx = datetime.datetime.now()
        xhour = datetime.datetime.now().hour
        if xhour >= 1 and xhour <= 15:
                xdelay = 300
                
        else:
                 xdelay = 15
                 
        xxcount= 0
        xxstop = xx + datetime.timedelta(minutes=4)
        xxstop = xxstop + datetime.timedelta(seconds=30)
        while datetime.datetime.now() <= xxstop:   # add to counter
                xxcount+=1 
                ga_web_activeusers = service.data().realtime().get(ids='ga:113841332',metrics="rt:activeusers").execute()
                ga_amoe_activeusers = service.data().realtime().get(ids='ga:113865394',metrics="rt:activeusers").execute()
                ga_ios_activeusers = service.data().realtime().get(ids='ga:115431021',metrics="rt:activeusers").execute()
                ga_andriod_activeusers = service.data().realtime().get(ids='ga:115372090',metrics="rt:activeusers").execute()

                web_activeusers_rows=[]
                amoe_activeusers_rows=[]
                ios_activeusers_rows=[]
                andriod_activeusers_rows=[]

          
                web_activeusers_rows = ga_web_activeusers.get('rows')
                amoe_activeusers_rows = ga_amoe_activeusers.get('rows')
                ios_activeusers_rows = ga_ios_activeusers.get('rows')
                andriod_activeusers_rows = ga_andriod_activeusers.get('rows')
                
                

                if web_activeusers_rows:
                        if web_activeusers_rows[0]:
                                web_activeusers = int(web_activeusers_rows[0][0])
                if amoe_activeusers_rows:
                        if amoe_activeusers_rows[0]:
                                amoe_activeusers  = int(amoe_activeusers_rows[0][0])
                if ios_activeusers_rows:
                        if ios_activeusers_rows[0]:
                                ios_activeusers = int(ios_activeusers_rows[0][0])
                if andriod_activeusers_rows:
                         if andriod_activeusers_rows[0]:
                                andriod_activeusers  = int(andriod_activeusers_rows[0][0])

                #time zone offset
                
                x = datetime.datetime.now()+datetime.timedelta(hours=-7)
             
                #do something with the data here

##########################################
                #call next metric
###########################################
     
                ga_web_pageviews = service.data().realtime().get(ids='ga:113841332',metrics="rt:pageviews").execute()
                ga_amoe_pageviews = service.data().realtime().get(ids='ga:113865394',metrics="rt:pageviews").execute()

                web_pageviews_rows=[]
                amoe_pageviews_rows=[]
                ios_pageviews_rows=[]
                andriod_pageviews_rows=[]

          
                web_pageviews_rows = ga_web_pageviews.get('rows')
                amoe_pageviews_rows = ga_amoe_pageviews.get('rows')
                
                

                if web_pageviews_rows:
                        if web_pageviews_rows[0]:
                                web_pageviews = int(web_pageviews_rows[0][0])
                if amoe_pageviews_rows:
                        if amoe_pageviews_rows[0]:
                                amoe_pageviews = int(amoe_pageviews_rows[0][0])
               
                #time zone offset
                                
                x = datetime.datetime.now()+datetime.timedelta(hours=-7)

                #do something with the data here

             
##########################################
                #call next metric
###########################################
                ga_ios_screenviews = service.data().realtime().get(ids='ga:115431021',metrics="rt:screenviews").execute()
                ga_andriod_screenviews = service.data().realtime().get(ids='ga:115372090',metrics="rt:screenviews").execute()


                
                ios_screenviews_rows=[]
                andriod_screenviews_rows=[]

          
                ios_screenviews_rows = ga_ios_screenviews.get('rows')
                andriod_screenviews_rows = ga_andriod_screenviews.get('rows')
                
                

                if ios_screenviews_rows:
                        if ios_screenviews_rows[0]:
                                ios_screenviews = int(ios_screenviews_rows[0][0])/30
                if andriod_screenviews_rows:
                        if andriod_screenviews_rows[0]:
                                andriod_screenviews = int(andriod_screenviews_rows[0][0])/30
                                
               #time zone offset
                
                x = datetime.datetime.now()+datetime.timedelta(hours=-7)
                


                #do something with the data here

##########################################
                #call next metric
###########################################
                ga_ios_totalevents = service.data().realtime().get(ids='ga:115431021',metrics="rt:totalevents").execute()
                ga_andriod_totalevents = service.data().realtime().get(ids='ga:115372090',metrics="rt:totalevents").execute()

                
                ios_totalevents_rows=[]
                andriod_totalevents_rows=[]
          
                ios_totalevents_rows = ga_ios_totalevents.get('rows')
                andriod_totalevents_rows = ga_andriod_totalevents.get('rows')
                
                
                if ios_totalevents_rows:
                        if ios_totalevents_rows[0]:
                                ios_totalevents = int(ios_totalevents_rows[0][0])/30
                if andriod_totalevents_rows:
                        if andriod_totalevents_rows[0]:
                                andriod_totalevents = int(andriod_totalevents_rows[0][0])/30
               
                #time zone offset
                x = datetime.datetime.now()+datetime.timedelta(hours=-7)
                 #do something with the data here         
                
                
##########################################
##########################################
                #all done, now sleep for the delay period
                time.sleep(xdelay)

    

     

