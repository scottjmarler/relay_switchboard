import os
import serial
import time
import streamlit as st
from PIL import Image

Arduino = serial.Serial('/dev/cu.usbmodem112201',9600, timeout=.1)      #Create Serial port object called ArduinoUnoSerialData time.sleep(1.5)                                                             #wait for 2 secounds for the communication to get established

st.header("Rockville Junction Switchboard")
begin= st.checkbox(label="Start/Stop")

with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True,)
        # image_of_layout = Image.open('##.png')
        # st.image(image_of_layout)


if begin:
        time.sleep(1.5)
        col1,col2,col3=st.columns(3)
        
        with col1:
                st.subheader("Block Control")
                m1 = st.select_slider(label="Main Line 1", options=["OFF","ON"], value="OFF")
                m2 = st.select_slider(label="Main Line 2", options=["OFF","ON"], value="OFF")
                m3 = st.select_slider(label="Main Line 3", options=["OFF","ON"], value="OFF")
                s1 = st.select_slider(label='Spur Line 1',options=['OFF', 'ON'], value="OFF")
                s2 = st.select_slider(label='Spur Line 2',options=['OFF', 'ON'], value="OFF")
                s3 = st.select_slider(label='Spur Line 3',options=['OFF', 'ON'], value="OFF")         
                s4 = st.select_slider(label='Spur Line 4',options=['OFF', 'ON'], value="OFF")
                s5 = st.select_slider(label='Spur Line 5',options=['OFF', 'ON'], value="OFF")
                s6 = st.select_slider(label='Engine Barn 1',options=['OFF', 'ON'], value="OFF")
                s7 = st.select_slider(label='Engine Barn 2',options=['OFF', 'ON'], value="OFF")
                
                if m1:  
                        Arduino.write(("m1"+m1).encode())
                        #time.sleep(1.5)                
                if m2:
                        Arduino.write(("m2"+m2).encode())
                        #time.sleep(1.5)
                if m3:
                        Arduino.write(("m3"+m3).encode())
                        #time.sleep(1.5)
                if s1:
                        Arduino.write(("s1"+s1).encode())
                        #time.sleep(1.5)
                if s2:
                        Arduino.write(("s2"+s2).encode())
                        
                if s3:
                        Arduino.write(("s3"+s3).encode())
                        
                if s4:
                        Arduino.write(("s4"+s4).encode())
                        
                if s5:
                        Arduino.write(("s5"+s5).encode())
                
                if s6:
                        Arduino.write(("s6"+s6).encode())
                        
                if s7:
                        Arduino.write(("s7"+s7).encode())
                        
               
                
        with col2:

                st.subheader("Switch Control")
                t1 = st.select_slider('Switch 1',options=['OFF','ON'], value="OFF")
                t2 = st.select_slider('Switch 2',options=['OFF','ON'], value="OFF")
                t3 = st.select_slider('Switch 3',options=['OFF','ON'], value="OFF")
                t4 = st.select_slider('Switch 4',options=['OFF','ON'], value="OFF")
                t5 = st.select_slider('Switch 5',options=['OFF','ON'], value="OFF")
                t6 = st.select_slider('Switch 6',options=['OFF','ON'], value="OFF")
                t7 = st.select_slider('Switch 7',options=['OFF','ON'], value="OFF")
                t8 = st.select_slider('Switch 8',options=['OFF','ON'], value="OFF")
                
                if t1:
                        Arduino.write(("Switch1"+t1).encode())
                        
                if t2:
                        Arduino.write(("Switch2"+t2).encode())
                        
                if t3:
                        Arduino.write(("Switch3"+t3).encode())
                        
                if t4:
                        Arduino.write(("Switch4"+t4).encode())
                        
                if t5:
                        Arduino.write(("Switch5"+t5).encode())
                        
                if t6:
                        Arduino.write(("Switch6"+t6).encode())
                        
                if t7:
                        Arduino.write(("Switch7"+t7).encode())
                        
                if t8:
                        Arduino.write(("Switch8"+t8).encode())
                        
                
        with col3:
                st.header("Accessories")

        
 


@st.cache(suppress_st_warning=True)
def saver():
        m1,m2,m3,s1,s2,s3,s4,s5,s6,s7,t1,t2,t3,t4,t5,t6,t7,t8
        return m1,m2,m3,s1,s2,s3,s4,s5,s6,s7,t1,t2,t3,t4,t5,t6,t7,t8

          
# Future Gauge Clusters to display voltage levels of each supply. Currently using .metric
# col_h1, col_h2, col_h3 = st.columns(3)
# with col_h1:
#         acv_black = 18.0
#         st.metric("Main Line Voltage", "AC", acv_black)
# with col_h2:
#         acv_blue = 18.0
#         st.metric("Spur Line Voltage", "AC", acv_blue)
# with col_h3:
#         dcv = 5.0
#         st.metric("Accesory Voltage", "DC", dcv)