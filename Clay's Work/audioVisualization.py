import wave
import struct
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pylab as pylab
import scipy.io.wavfile as wavfile
import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

mpl.use('TkAgg') #set Tk as output for matplotlib

#set up device to receive output from matplotlib plotter ////////////////////////////
root = Tk.Tk() 								#make root window in Tk
root.wm_title("WAV waves") 					#title window
f = Figure(figsize=(5,4), dpi=100) 			#create figure w/ coordinates, pixel size
canvas = FigureCanvasTkAgg(f, master=root) 	#put figure in window and attach to canvas 
canvas.show() 								#show window
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
											#put drawing widget from canvas in window

#open WAV file & initialize variables ///////////////////////////////
afrate,adata = wavfile.read('eagle.wav') #open with read-only functionality
adsize = len(adata)		 	 	#audio data size in frames
#afrate = wf.getframerate() 	 	#audio frame rate
ofrate = 10 				 	#output frame rate
apf = int(afrate/ofrate) 	 	#number of audio frames per output frame
#adata = wf.readframes(adsize) 	#data from file
#wf.close()						#data is extracted, file can be closed

#set data format & unpack
#fmt = '%dh' % (adsize)
#print(adsize)
#adata = struct.unpack(fmt, adata)
#adata = list(adata) #convert from tuple to list

#FUNCTION: get average value of points in a list
def averagepts(points):
	pt_sum = 0
	total = 0
	avg = 0
	for p in points:
		pt_sum += p
		total += 1
	if total != 0:
		avg = int(pt_sum / total)
	return avg

#plot the wave in chunks of frames at a time onto the screen
yhigh = 0
ylow = 0
for i in range(0,adsize,apf) :
	if apf > adsize - i:  #if chunk size is larger than remaining bytes
		apf = adsize - i  #make chunk size smaller to fit

	lastidx = i+apf 			 #index of last frame in chunk
	avgstep = 2 				 #desired number of frames to average
	plt = f.add_subplot(111) 	 #plotter initialization
	avgpts = [] 				 #wave point list initialization
	avgidx = 0
	x = np.arange(0,apf,avgstep) #x-values to plot against wave values

	#fill avgpts with averages of wave values, avgstep number of points at a time
	for j in range(i,lastidx,avgstep):
		if j + avgstep > lastidx:
			avgpts.append(averagepts(adata[j:lastidx]))
			avgidx += 1
		else:
			avgpts.append(averagepts(adata[j:j+avgstep-1]))
			avgidx += 1
		if avgpts[avgidx-1] > yhigh:
			yhigh = avgpts[avgidx-1]
		else:
			if avgpts[avgidx-1] < ylow:
				ylow = avgpts[avgidx-1]

	#plot and render wave on screen//////////////////////
	plt.clear() 			#clear plotter of old points
	if len(x) == len(avgpts) : 
		plt.plot(x,avgpts) 	#plot points
	canvas.draw() 			#render on screen
	plt.set_ylim(ylow,yhigh)

Tk.mainloop()