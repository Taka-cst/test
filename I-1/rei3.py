import pyvisa #type: ignore
import time
import matplotlib.pyplot as plt
import numpy as np

def get_voltage(fq):
    function_generator.write(f':FREQ {fq}')
    time.sleep(1)
    measurement_device.write(':MEAS:VOLT?')
    response=measurement_device.read()
    try:
        voltage_str=response.split(',')[3]
        voltage=float(voltage_str)
    except(IndexError,ValueError) as e:
        voltage=0.0
        print(f'\n----Error:{e}----\n')
    return voltage

rm=pyvisa.ResourceManager()
function_generator_address=''
function_generator=rm.open_resource(function_generator_address)
function_generator.write(':FUNC:SHAP SIN')
function_generator.write(':VOLT 2')
function_generator.write(':FREQ 100')
function_generator.write(':OUTP ON')
measurement_device_address=''
measurement_device=rm.open_resource(measurement_device_address)
measurement_device.timeout=5000
time.sleep(5)
measurement_device.write(':MAIN:FUNC ACV')
measurement_device.write(':MAIN:RANG:VAL 5')
time.sleep(5)
frequencies=np.logspace(2,5,31)
voltage=[]
plt.ion()
fig,ax=plt.subplots()
line, =ax.semilogx(frequencies,[0]*len(frequencies), '-o')
ax.set_title('Frequency Response')
ax.set_xlabel('Frequency [Hz]')
ax.set_ylabel('Voltage [V]')

for freq in frequencies:
    voltage= get_voltage(freq)
    print(f'Frequency:{freq}Hz, Voltage:{voltage}V')
    voltage.append(voltage)
    line.set_ydata(voltage)
    line.set_xdata(frequencies[:len(voltage)])
    ax.relim()
    ax.autoscale_view()
    fig.canvas.draw()
    plt.pause(0.1)
    plt.pause(0.1)
    time.sleep(0.1)
    np.savetxt('frequency_response.csv',np.array([frequencies,voltage]).T,
               delimiter=',')

function_generator.close()
measurement_device.close()
rm.close()
plt.ioff()
plt.show()









