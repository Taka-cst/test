import pyvisa
import time
import numpy as np
import matplotlib.pyplot as plt
rm=pyvisa.ResourceManager()
measurement_device_address='GPIB0::9::INSTR'
measurement_device=rm.open_resource(measurement_device_address)
measurement_device.write(':MAIN:FUNC DCV')
measurement_device.write(':MAIN:RANG:VAL 1e0')
power_supply_address='COM14'
power_supply=rm.open_resource(power_supply_address)

power_supply.write('TRACK0')
power_supply.write('VSET1:0')
power_supply.write('ISET1:0')
power_supply.write('OUT1')

time.sleep(5)

time_data=[]
voltage_data=[]


max_time=200
measurement_interval= 0.1
supply_voltage=1.0

plt.ion()
fig, ax=plt.subplots()
line_measured, = ax.plot([],[],'o-',label='Measured[V]')
ax.set_xlabel('Time[s]')
ax.set_ylabel('Voltage[V]')
ax.set_title('down Voltage vs Time')
ax.legend()
ax.grid(True)

power_supply.write('VSET1:1.0')
power_supply.write('ISET1:0.3')

while(1):
    time.sleep(1)
    measurement_device.write(':MAIN:DATA?') 
    response=measurement_device.read()
    try:
        voltage_str=response.split(',')[3]
        voltage=float(voltage_str)
    except(IndexError,ValueError) as e:
        voltage=0.0
        print(f'\n----Error:{e}----\n')
        voltage=0.0
    print(voltage)
    if voltage >= 0.99*supply_voltage:
        break
power_supply.write('VSET1:0.0')
power_supply.write('ISET1:0.0')

start_time=time.time()


while True:
    current_time = time.time()-start_time
    measurement_device.write(':MAIN:DATA?')
    response=measurement_device.read()
    try:
        voltage_str=response.split(',')[3]
        voltage=float(voltage_str)
    except(IndexError,ValueError) as e:
        voltage=0.0
        print(f'\n----Error:{e}----\n')
        voltage=0.0
    time_data.append(current_time)
    voltage_data.append(voltage)
    print(f'Time:{current_time:.2f}s, Voltage:{voltage:.2f}V')
    if current_time >= max_time or voltage <= 0.01*supply_voltage:
        break

    line_measured.set_xdata(time_data)
    line_measured.set_ydata(voltage_data)

    ax.relim()
    ax.autoscale_view()
    plt.draw()
    plt.pause(0.01)
    np.savetxt('down.csv', np.array([time_data,voltage_data]).T, delimiter=',', header='Time[s],Voltage[V]', comments='')

measurement_device.close()
power_supply.close()
rm.close()
plt.ioff()
plt.show()