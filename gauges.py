import plotly.graph_objects as go

# Gauges

AC_1_volts = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = 16,
        title = {'text': "AC_1_Volts"},
        gauge = {'axis': {'range': [None, 24]},
             'steps' : [
                 {'range': [0, 10], 'color': "yellow"},
                 {'range': [10, 18], 'color': "orange"},
                 {'range': [18, 24], 'color': "red"}]}
))
AC_1_volts.update_layout(
        autosize=False,
        width=250,
        height=250,
        margin_b=0,
        margin_l=0,
        )
        



AC_1_amps = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = 5,
        title = {'text': "AC_1_Amps"},
        gauge = {'axis': {'range': [None, 20]},
             'steps' : [
                 {'range': [0, 10], 'color': "yellow"},
                 {'range': [10, 15], 'color': "orange"},
                 {'range': [15, 20], 'color': "red"}]}
))
AC_1_amps.update_layout(
        autosize=False,
        width=250,
        height=250,
        margin_b=0,
        margin_l=0,
)

AC_2_volts = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = 14.25,
        title = {'text': "AC_2_Volts"},
        gauge = {'axis': {'range': [None, 24]},
             'steps' : [
                 {'range': [0, 10], 'color': "yellow"},
                 {'range': [10, 18], 'color': "orange"},
                 {'range': [18, 24], 'color': "red"}]}
))
AC_2_volts.update_layout(
        autosize=False,
        width=250,
        height=250,
        margin_b=0,
        margin_l=0,
)

AC_2_amps = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = 7,
        title = {'text': "AC_2_Amps"},
        gauge = {'axis': {'range': [None, 20]},
             'steps' : [
                 {'range': [0, 10], 'color': "yellow"},
                 {'range': [10, 15], 'color': "orange"},
                 {'range': [15, 20], 'color': "red"}]}
))
AC_2_amps.update_layout(
        autosize=False,
        width=250,
        height=250,
        margin_b=0,
        margin_l=0,
)

DC_1_volts = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = 5,
        title = {'text': "DC_1_Volts"},
        gauge = {'axis': {'range': [None, 6]},
             'steps' : [
                 {'range': [0, 5], 'color': "yellow"},
                 {'range': [5,6], 'color': "red"}]}
))
DC_1_volts.update_layout(
        autosize=False,
        width=250,
        height=250, 
        margin_b=0,
        margin_l=0,      
)

DC_1_amps = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = 15,
        title = {'text': "DC_1_Amps"},
        gauge = {'axis': {'range': [None, 20]},
             'steps' : [
                 {'range': [0, 10], 'color': "yellow"},
                 {'range': [10, 15], 'color': "orange"},
                 {'range': [15, 20], 'color': "red"}]}
))
DC_1_amps.update_layout(
        autosize=False,
        width=250,
        height=250, 
        margin_b=0,
        margin_l=0,      
)


