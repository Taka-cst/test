import pyvisa #type: ignore
import time
import numpy as np
import matplotlib.pyplot as plt
rm=pyvisa.ResourceManager()
measurement_device_address=''
measurement_device=rm.open_resource(measurement_device_address)
measurement_device.write(':MAIN:FUNC DCV')
measurement_device.write(':MAIN:RANG:VAL 5e0')
power_supply_address=''
power_supply=rm.open_resource(power_supply_address)

power_supply.write(':INST OUT1')
power_supply.write(':VOLT 0')
power_supply.write(':CURR 0')
power_supply.write(':OUTP ON')

time.sleep(5)

time_data=[]
voltage_data=[]
start_time=time.time()

max_time=100
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

power_supply.write(':VOLT 1')
power_supply.write(':CURR 0.3')

time.sleep(10)#充電待機
power_supply.write(':VOLT 0')

while True:
    current_time = time.time()-start_time
    measurement_device.write(':MEAS:VOLT?') 
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
    if current_time >= max_time or voltage >= 0.99*supply_voltage:
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

