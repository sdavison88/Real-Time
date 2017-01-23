"""
Created on Wed Feb  3 12:36:09 2016

@author: spencer.davison
"""
import os
#import OpenSSL
from plotly import plotly
import plotly.plotly as py
from plotly.graph_objs import *
import plotly.tools as tls
from googleapiclient.discovery import build
from oauth2client.client import SignedJwtAssertionCredentials
import httplib2
import datetime
import time
import sys

def lambda_handler(event, context):
        #tls.set_credentials_file(username="sdavison88",api_key="ls005fl7r5")
        #tls.set_credentials_file(stream_ids=['81iryp10uc'])
        plotly.plotly.sign_in(username="sdavison88",api_key="ls005fl7r5",stream_ids=['81iryp10uc','065urwxs6h','4or606ax2k','yw0vorv2re', 'mg64use15n', 'umuqd6xeib', 'lz6o04lny2','pvkdux9hhv','bqy7wf7z7n','5al5am79gh'])

        #credentials = tls.get_credentials_file()
        #print(credentials)

        #stream_ids = tls.get_credentials_file()['stream_ids']
        

        
        ac_stream_id1='81iryp10uc'
        ac_stream_id2='065urwxs6h'
        ac_stream_id3='4or606ax2k'
        ac_stream_id4='yw0vorv2re'
        pv_stream_id1='mg64use15n'
        pv_stream_id2='umuqd6xeib'
        sv_stream_id1='lz6o04lny2'
        sv_stream_id2='pvkdux9hhv'
        te_stream_id1='bqy7wf7z7n'
        te_stream_id2='5al5am79gh'

        
        ac_Website=Scatter(x=[],y=[],stream=Stream(token=ac_stream_id1,maxpoints=20),mode ='lines',line = dict(color='rgb(0,0,0)',width='2'),name='Website')
        ac_AMOE=Scatter(x=[],y=[],stream=Stream(token=ac_stream_id2,maxpoints=20),mode ='lines',line = dict(color='rgb(232,232,232)',width='2'),name='AMOE')
	ac_IOS=Scatter(x=[],y=[],stream=Stream(token=ac_stream_id3,maxpoints=20), mode ='lines',line = dict(color='rgb(226,0,116)',width='2'),name='IOS')
 	ac_Android=Scatter(x=[],y=[],stream=Stream(token=ac_stream_id4,maxpoints=20), mode='lines',line = dict(color='rgb(226,0,116)',width='2.5', dash='dash'),name='Android')
        pv_Website=Scatter(x=[],y=[],stream=Stream(token=pv_stream_id1,maxpoints=20),mode ='lines',line = dict(color='rgb(0,0,0)',width='2'),name='Website')
        pv_AMOE=Scatter(x=[],y=[],stream=Stream(token=pv_stream_id2,maxpoints=20),mode ='lines',line = dict(color='rgb(232,232,232)',width='2'),name='AMOE')
       	sv_IOS=Scatter(x=[],y=[],stream=Stream(token=sv_stream_id1,maxpoints=20), mode ='lines',line = dict(color='rgb(226,0,116)',width='2'),name='IOS')
 	sv_Android=Scatter(x=[],y=[],stream=Stream(token=sv_stream_id2,maxpoints=20), mode='lines',line = dict(color='rgb(226,0,116)',width='2.5', dash='dash'),name='Android')
	te_IOS=Scatter(x=[],y=[],stream=Stream(token=te_stream_id1,maxpoints=20), mode ='lines',line = dict(color='rgb(226,0,116)',width='2'),name='IOS')
 	te_Android=Scatter(x=[],y=[],stream=Stream(token=te_stream_id2,maxpoints=20), mode='lines',line = dict(color='rgb(226,0,116)',width='2.5', dash='dash'),name='Android')

         
        #####
        ac_data=Data([ac_Website, ac_AMOE,ac_IOS,ac_Android])
        pv_data=Data([pv_Website, pv_AMOE])
        sv_data=Data([sv_IOS,sv_Android])
        te_data=Data([te_IOS,te_Android])
        
        # Add title to layout object
        ac_layout = Layout(
                        font=dict(family="Tele-GroteskNor",
                        color="#F0F0F0"),
                        xaxis=dict(linecolor="#898989",gridcolor='rgb(53,53,53)'),
                        yaxis=dict(linecolor="#898989",gridcolor='rgb(53,53,53)'),
                        paper_bgcolor='rgb(53,53,53)',plot_bgcolor='rgb(53,53,53)',
                        margin=dict(b=40,l=40,r=40,t=40),
                        hidesources=True,
                        showlegend=True)
        pv_layout = Layout(
                font=dict(family="Tele-GroteskNor",color="#F0F0F0"),
                xaxis=dict(linecolor="#898989",gridcolor='rgb(53,53,53)'),
                yaxis=dict(linecolor="#898989",gridcolor='rgb(53,53,53)'),
                paper_bgcolor='rgb(53,53,53)',
                plot_bgcolor='rgb(53,53,53)',
                margin=dict(b=40,l=40,r=40,t=40),
                hidesources=True,
                showlegend=False)
        sv_layout = Layout(
                font=dict(family="Tele-GroteskNor",color="#F0F0F0"),
                xaxis=dict(linecolor="#898989",gridcolor='rgb(53,53,53)'),
                yaxis=dict(linecolor="#898989",gridcolor='rgb(53,53,53)'),
                paper_bgcolor='rgb(53,53,53)',
                plot_bgcolor='rgb(53,53,53)',
                margin=dict(b=40,l=40,r=40,t=40),
                hidesources=True,
                showlegend=False)
        te_layout = Layout(
                font=dict(family="Tele-GroteskNor",color="#F0F0F0"),
                xaxis=dict(linecolor="#898989",gridcolor='rgb(53,53,53)'),
                yaxis=dict(linecolor="#898989",gridcolor='rgb(53,53,53)'),
                paper_bgcolor='rgb(53,53,53)',
                plot_bgcolor='rgb(53,53,53)',
                margin=dict(b=40,l=40,r=40,t=40),
                hidesources=True,
                showlegend=False)
        
        # Make a figure object
        ac_fig = Figure(data=ac_data, layout=ac_layout)
        pv_fig = Figure(data=pv_data, layout=pv_layout)
        sv_fig = Figure(data=sv_data, layout=sv_layout)
        te_fig = Figure(data=te_data, layout=te_layout)
        
        # (@) Send fig to Plotly, initialize streaming plot, open new tab
        #ac_unique_url = py.plot(ac_fig, filename='activeusers')
        #pv_unique_url = py.plot(pv_fig, filename='pageviews')
        #sv_unique_url = py.plot(sv_fig, filename='screenviews')
        #te_unique_url = py.plot(te_fig, filename='totalevents')
        
        ac_s_Website=py.Stream(ac_stream_id1)
        ac_s_AMOE=py.Stream(ac_stream_id2)
        ac_s_IOS=py.Stream(ac_stream_id3)
        ac_s_Android=py.Stream(ac_stream_id4)

        pv_s_Website=py.Stream(pv_stream_id1)
        pv_s_AMOE=py.Stream(pv_stream_id2)

        sv_s_IOS=py.Stream(sv_stream_id1)
        sv_s_Android=py.Stream(sv_stream_id2)
        
        te_s_IOS=py.Stream(te_stream_id1)
        te_s_Android=py.Stream(te_stream_id2)
        #######

        ac_s_Website.open()
        ac_s_AMOE.open()
        ac_s_IOS.open()
        ac_s_Android.open()
        pv_s_Website.open()
        pv_s_AMOE.open()
        sv_s_IOS.open()
        sv_s_Android.open()
        te_s_IOS.open()
        te_s_Android.open()
        
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
                xdelay = 600
                
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

                
                x = datetime.datetime.now()+datetime.timedelta(hours=-7)
                #x = x.strftime('%Y-%m-%d %H:%M:%S.%f')
             

                # (-) Both x and y are numbers (i.e. not lists nor arrays)

                # (@) write to Plotly stream!
                ac_s_Website.write({'x': x, 'y': web_activeusers})
                ac_s_AMOE.write({'x': x, 'y': amoe_activeusers})
                ac_s_IOS.write({'x': x, 'y': ios_activeusers})
                ac_s_Android.write({'x': x, 'y': andriod_activeusers})
                
                print('ActiveUsers_Start: '+ str(xx) + ',End: ' + str(xxstop) + ',delay in secs: '+ str(xdelay) + 'Hour: ' + str(xhour) + 'Count: '+str(xxcount)+';at: '+ str(x)+' : '+ str(web_activeusers)+','+str(amoe_activeusers)+','+str(ios_activeusers)+','+str(andriod_activeusers)+': sent to plotly')
                #time.sleep(1)
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
               
                
                x = datetime.datetime.now()+datetime.timedelta(hours=-7)

                # (-) Both x and y are numbers (i.e. not lists nor arrays)

                # (@) write to Plotly stream!
                pv_s_Website.write({'x': x, 'y': web_pageviews})
                pv_s_AMOE.write({'x': x, 'y': amoe_pageviews})
                
                print('PAGEVVEIWS_Start: '+ str(xx) + ',End: ' + str(xxstop) + ',delay in secs: '+ str(xdelay) + 'Hour: ' + str(xhour) + 'Count: '+str(xxcount)+';at: '+ str(x)+' : '+ str(web_pageviews)+','+str(amoe_pageviews)+': sent to plotly')
               
                #time.sleep(1)
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
               
                
                x = datetime.datetime.now()+datetime.timedelta(hours=-7)
                

                # (-) Both x and y are numbers (i.e. not lists nor arrays)

                # (@) write to Plotly stream!
                sv_s_IOS.write({'x': x, 'y': ios_screenviews})
                sv_s_Android.write({'x': x, 'y': andriod_screenviews})
                                
                print('SCREENVEIWS_Start: '+ str(xx) + ',End: ' + str(xxstop) + ',delay in secs: '+ str(xdelay) + 'Hour: ' + str(xhour) + 'Count: '+str(xxcount)+';at: '+ str(x)+' : '+ str(ios_screenviews)+','+str(andriod_screenviews)+': sent to plotly')
               
                
                #time.sleep(1)
##########################################
                #call next metric
###########################################
                ga_ios_totalevents = service.data().realtime().get(ids='ga:115431021',metrics="rt:goal1Completions").execute()
                ga_andriod_totalevents = service.data().realtime().get(ids='ga:115372090',metrics="rt:goal1Completions").execute()


                
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
               
                
                x = datetime.datetime.now()+datetime.timedelta(hours=-7)

                # (-) Both x and y are numbers (i.e. not lists nor arrays)

                # (@) write to Plotly stream!
                te_s_IOS.write({'x': x, 'y': ios_totalevents})
                te_s_Android.write({'x': x, 'y': andriod_totalevents})
                                
                print('TOTALEVENTS_Start: '+ str(xx) + ',End: ' + str(xxstop) + ',delay in secs: '+ str(xdelay) + 'Hour: ' + str(xhour) + 'Count: '+str(xxcount)+';at: '+ str(x)+' : '+ str(ios_totalevents)+','+str(andriod_totalevents)+': sent to plotly')
               
                
                
##########################################
##########################################
                #all done, now sleep for the delay period
                time.sleep(xdelay)

                # (!) Write numbers to stream to append current data on plot,
                #     write lists to overwrite existing data on plot (more in 7.2).

         # (!) plot a point every 80 ms, for smoother plotting

        # (@) Close the stream when done plotting
        ac_s_Website.close()
        ac_s_AMOE.close()
        ac_s_IOS.close()
        ac_s_Android.close()
        pv_s_Website.close()
        pv_s_AMOE.close()
        sv_s_IOS.close()
        sv_s_Android.close()
        te_s_IOS.close()
        te_s_Android.close()
        
##only for local testing
#lambda_handler('1','2')
