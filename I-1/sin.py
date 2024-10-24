import numpy as np
import matplotlib.pyplot as plt
import time
def get_sin(phase_shift):
    x=np.linspace(0,4*np.pi,1000)
    y=np.sin(x+phase_shift)
    return x,y

plt.ion()
fig, ax=plt.subplots()
freq,amp=get_sin(0)
line, = ax.plot(freq,amp)

ax.set_xlabel('Time')
ax.set_ylabel('Amplitude')
ax.set_title('Sin Wave')
ax.set_ylim(-1.5, 1.5)

phase_shift=0
while True:
    freq,amp=get_sin(phase_shift)
    line.set_ydata(amp)
    line.set_xdata(freq[:len(amp)])
    ax.relim()
    ax.autoscale_view()
    plt.draw()
    plt.pause(0.1)
    phase_shift+=0.1
    time.sleep(0.1)
    #csvとして保存
    np.savetxt('sin_wave.csv',np.array([freq,amp]).T,delimiter=',')




    