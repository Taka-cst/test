import pyvisa #type: ignore
import time
import matplotlib.pyplot as plt
import numpy as np

R = 0
C = 0

def calculate_capacitor_voltage(frequency, R, C):
    t1=1/((2*np.pi*frequency)*C)
    t2=np.sqrt(R**2+(1/((2*np.pi*frequency*C)))**2)
    return t1 / t2 / np.sqrt(2)


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
measurement_device.write(':MAIN:RANG:VAL 1e0')
frequencies=np.logspace(2,5,31)

measured_voltages=[]
theoretical_voltages=[]

plt.ion()
fig, ax=plt.subplots()
line_measured, = ax.plot([],[],'o-',label='Measured[V]')
line_theoretical, = ax.plot([],[],'r--',label='Theoretical[V]')
ax.set_xlabel('Frequency[Hz]')
ax.set_ylabel('Voltage[V]')
ax.set_title('Voltage vs Frequency')
ax.legend()
ax.grid(True,which='both', linestyle='--', linewidth=0.5)

for idx, freq in enumerate(frequencies):
    measured_voltage = get_voltage(freq)
    theoretical_voltage = calculate_capacitor_voltage(freq, R, C)
    print(f'Frequency:{freq:.2f}Hz, Measured Voltage:{measured_voltage:.2f}V, Theoretical Voltage:{theoretical_voltage:.2f}V')
    measured_voltages.append(measured_voltage)
    theoretical_voltages.append(theoretical_voltage)
    line_measured.set_xdata(frequencies[:len(measured_voltages)])
    line_measured.set_ydata(measured_voltages)
    line_theoretical.set_xdata(frequencies[:len(theoretical_voltages)])
    line_theoretical.set_ydata(theoretical_voltages)
    ax.relim()
    ax.autoscale_view()
    plt.draw()
    plt.pause(0.1)
    np.savetxt('rei4.csv',np.array([freq,measured_voltage,theoretical_voltage]).T,
               delimiter=',')

measurement_device.close()
function_generator.close()
rm.close()
