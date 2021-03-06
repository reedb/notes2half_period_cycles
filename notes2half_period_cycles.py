#!/usr/bin/python
#
# Build a table of half period cycle counts.
# 
                               
import sys
import os 
import math

# Octive  	C	    C#	    D 	    Eb	    E	    F 	    F#	    G	    G# 	    A	    Bb	    B
# 0	        16.35	17.32	18.35	19.45	20.60	21.83	23.12	24.50	25.96	27.50	29.14	30.87
# 1	        32.70	34.65	36.71	38.89	41.20	43.65	46.25	49.00	51.91	55.00	58.27	61.74
# 2	        65.41	69.30	73.42	77.78	82.41	87.31	92.50	98.00	103.8	110.0	116.5	123.5
# 3	        130.8	138.6	146.8	155.6	164.8	174.6	185.0	196.0	207.7	220.0	233.1	246.9
# 4	        261.6	277.2	293.7	311.1	329.6	349.2	370.0	392.0	415.3	440.0	466.2	493.9
# 5	        523.3	554.4	587.3	622.3	659.3	698.5	740.0	784.0	830.6	880.0	932.3	987.8
# 6	        1047	1109	1175	1245	1319	1397	1480	1568	1661	1760	1865	1976
# 7	        2093	2217	2349	2489	2637	2794	2960	3136	3322	3520	3729	3951
# 8	        4186	4435	4699	4978	5274	5588	5920	6272	6645	7040	7459	7902

# Note name vs frequency
#     
note_name_freq_data = [["C3",  130.8],["C#3", 138.6],["D3",  146.8],["Eb3", 155.6],["E3",  164.8],["F3",  174.6],["F#3", 185.0],
                       ["G3",  196.0],["G#3", 207.7],["A3",  220.0],["Bb3", 233.1],["B3",  246.9],["C4",  261.6],["C#4", 277.2],
                       ["D4",  293.7],["Eb4", 311.1],["E4",  329.6],["F4",  349.2],["F#4", 370.0],["G4",  392.0],["G#4", 415.3],
                       ["A4",  440.0],["Bb4", 466.2],["B4",  493.9],["C5",  523.3],["C#5", 554.4],["D5",  587.3],["Eb5", 622.3],
                       ["E5",  659.3],["F5",  698.5],["F#5", 740.0],["G5",  784.0],["G#5", 830.6],["A5",  880.0],["Bb5", 932.3],
                       ["B5",  987.8]]
                       
# MCU oscilator frequency. Most instructions at 4MHz take 1 uS.
_XTAL_FREQ = 20000000.0
for name_freq in note_name_freq_data:
  cycles = (_XTAL_FREQ / 4000000.0) * 500000.0 / name_freq[1]
  print "%r\t%4.1f\t%r" % (name_freq[0], name_freq[1], round(cycles))
