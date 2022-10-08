import os
import sys
import serial
import time
import streamlit as st
from PIL import Image
import plotly.graph_objects as go
import gauges as g
from streamlit_webrtc import webrtc_streamer
import av
import cv2

# Initiate Communication with Serial connection

# Arduino = serial.Serial('/dev/cu.usbmodem1101',9600, timeout=.1)      #Create Serial port object called ArduinoUnoSerialData time.sleep(1.5)                                                             #wait for 2 secounds for the communication to get established

# Sidebar Tips
st.sidebar.header("Rockville Junction")
st.subheader("Control Center")
tips = st.sidebar.selectbox("Operating Tips",options=["Select Engine Type","Legacy","Post-War"])
if tips == "Legacy":
        st.sidebar.info("Set all throttles to full power when using Legacy locomotives.",icon="🚂")
        st.sidebar.info("Set all blocks to ON when using Legacy locomotives.",icon="🚂")
if tips == "Post-War":
        st.sidebar.info("Set all throttles to zero power when using post-war locomotives.",icon="🚂")
        st.sidebar.info("Block control allowed when using post-war locomotives.",icon="🚂")

# Blocks, Switches, Acc, Map

tab1,tab2,tab3,tab4,tab5 = st.tabs(["Blocks", "Switches", "Acc.","Map", "Meters"])

with tab1:
        with st.spinner():
                        time.sleep(.75)
        col1,col2 = st.columns(2)
        with tab1,col1:
                    
                m1 = st.select_slider(label="Main Line 1",options=["OFF","ON"],value="ON")
                st.write("\n")
                m2 = st.select_slider(label="Main Line 2",options=["OFF","ON"],value="ON")
                st.write("\n")
                m3 = st.select_slider(label="Main Line 3",options=["OFF","ON"],value="ON")
                st.write("\n")
                s4 = st.select_slider(label='Station 1',options=["OFF","ON"],value="ON")
                st.write("\n")
                s5 = st.select_slider(label='Station 2',options=["OFF","ON"],value="ON")
                st.write("\n")     
                
        with tab1,col2:
                
                s1 = st.select_slider(label='Spur Line 1',options=["OFF","ON"],value="ON")
                st.write("\n")
                s2 = st.select_slider(label='Spur Line 2',options=["OFF","ON"],value="ON")
                st.write("\n")
                s3 = st.select_slider(label='Spur Line 3',options=["OFF","ON"],value="ON")  
                st.write("\n")
                s6 = st.select_slider(label='Engine Barn 1',options=["OFF","ON"],value="ON")
                st.write("\n")
                s7 = st.select_slider(label='Engine Barn 2',options=["OFF","ON"],value="ON")
                
with tab2:
        with st.spinner():
                        time.sleep(.75)
        col1_tab2,col2_tab2=st.columns(2)
        with tab2,col1_tab2:
                t1 = st.select_slider('Switch 1',options=["OFF","ON"],value="OFF")
                st.write("\n")
                t2 = st.select_slider('Switch 2',options=["OFF","ON"],value="OFF")
                st.write("\n")
                t3 = st.select_slider('Switch 3',options=["OFF","ON"],value="OFF")
                st.write("\n")
                t4 = st.select_slider('Switch 4',options=["OFF","ON"],value="OFF")

        with tab2,col2_tab2:
                t5 = st.select_slider('Switch 5',options=["OFF","ON"],value="OFF")
                st.write("\n")
                t6 = st.select_slider('Switch 6',options=["OFF","ON"],value="OFF")
                st.write("\n")
                t7 = st.select_slider('Switch 7',options=["OFF","ON"],value="OFF")
                st.write("\n")
                t8 = st.select_slider('Switch 8',options=["OFF","ON"],value="OFF")
      
with tab3:
        st.header("Accessories")



with tab4:
        threshold1 = st.slider("Threshold1", min_value=0, max_value=1000, step=1, value=100)
        threshold2 = st.slider("Threshold2", min_value=0, max_value=1000, step=1, value=200)


        def callback(frame):
                img = frame.to_ndarray(format="bgr24")
                img = cv2.cvtColor(cv2.Canny(img, threshold1, threshold2), cv2.COLOR_GRAY2BGR)

                return av.VideoFrame.from_ndarray(img, format="bgr24")


        webrtc_streamer(key="example", video_frame_callback=callback)


with tab5:
        col1_tab5,col2_tab5 = st.columns([2,2])
        with col1_tab5:
                st.write(g.AC_1_volts)  
                st.write(g.AC_2_volts)
                st.write(g.DC_1_volts)
                
        with col2_tab5:
                st.write(g.AC_1_amps)
                st.write(g.AC_2_amps)
                st.write(g.DC_1_amps)  

# while Arduino: 

#         if m1: 
#                 Arduino.write(("m1"+m1).encode()) 
#                 Arduino.write(("\n").encode())
                
#         if m2: 
#                 Arduino.write(("m2"+m2).encode())
#                 Arduino.write(("\n").encode())
                
#         if m3:
#                 Arduino.write(("m3"+m3).encode())
#                 Arduino.write(("\n").encode())
                
#         if s1:
#                 Arduino.write(("s1"+s1).encode())
#                 Arduino.write(("\n").encode())
                
#         if s2:
#                 Arduino.write(("s2"+s2).encode())
#                 Arduino.write(("\n").encode())    
                
#         if s3:
#                 Arduino.write(("s3"+s3).encode())
#                 Arduino.write(("\n").encode())
                
#         if s4:
#                 Arduino.write(("s4"+s4).encode())
#                 Arduino.write(("\n").encode())
                
#         if s5:
#                 Arduino.write(("s5"+s5).encode())
#                 Arduino.write(("\n").encode())
                
#         if s6:
#                 Arduino.write(("s6"+s6).encode())
#                 Arduino.write(("\n").encode())
                
#         if s7:
#                 Arduino.write(("s7"+s7).encode())
#                 Arduino.write(("\n").encode())
                
#         if t1:
#                 Arduino.write(("Switch1"+t1).encode())
#                 Arduino.write(("\n").encode())
                
#         if t2:
#                 Arduino.write(("Switch2"+t2).encode())
#                 Arduino.write(("\n").encode())
                
#         if t3:
#                 Arduino.write(("Switch3"+t3).encode())
#                 Arduino.write(("\n").encode())
                
#         if t4:
#                 Arduino.write(("Switch4"+t4).encode())
#                 Arduino.write(("\n").encode())
                
#         if t5:
#                 Arduino.write(("Switch5"+t5).encode())
#                 Arduino.write(("\n").encode())
                
#         if t6:
#                 Arduino.write(("Switch6"+t6).encode())
#                 Arduino.write(("\n").encode())
                
#         if t7:
#                 Arduino.write(("Switch7"+t7).encode())
#                 Arduino.write(("\n").encode())
                
#         if t8:
#                 Arduino.write(("Switch8"+t8).encode())
#                 Arduino.write(("\n").encode())
                
        
#         break
        
@st.cache(suppress_st_warning=True)
def saver():
        tips,m1,m2,m3,s1,s2,s3,s4,s5,s6,s7,t1,t2,t3,t4,t5,t6,t7,t8,g.AC_1_volts,g.AC_1_amps,g.AC_2_volts,g.AC_2_amps,g.DC_1_volts,g.DC_1_amps
        return tips,m1,m2,m3,s1,s2,s3,s4,s5,s6,s7,t1,t2,t3,t4,t5,t6,t7,t8,g.AC_1_volts,g.AC_1_amps,g.AC_2_volts,g.AC_2_amps,g.DC_1_volts,g.DC_1_amps

        

        