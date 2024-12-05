import pyvisa
import time
import matplotlib.pyplot as plt
import numpy as np

R = 5150
C = 1e-8

def calculate_capacitor_voltage(frequency, R, C):
    t1 = 1 / ((2 * np.pi * frequency) * C)
    t2 = np.sqrt(R**2 + (1 / ((2 * np.pi * frequency * C)))**2)
    return t1 / t2 / np.sqrt(2)
    # return 1/np.sqrt(2)
def get_voltage(fq):
    function_generator.write(f':FREQ {fq}')
    time.sleep(2)
    measurement_device.write(':MAIN:DATA?')
    response = measurement_device.read()
    try:
        voltage_str = response.split(',')[3]
        voltage = float(voltage_str)
    except (IndexError, ValueError) as e:
        voltage = 0.0
        print(f'\n----Error: {e}----\n')
    return voltage

rm = pyvisa.ResourceManager()
function_generator_address = 'GPIB0::2::INSTR'
function_generator = rm.open_resource(function_generator_address)
function_generator.write(':FUNC:SHAP SIN')
function_generator.write(':VOLT 1')
function_generator.write(':FREQ 100')
function_generator.write(':OUTP ON')

measurement_device_address = 'GPIB0::9::INSTR'
measurement_device = rm.open_resource(measurement_device_address)
measurement_device.timeout = 10000
time.sleep(5)
measurement_device.write(':MAIN:FUNC ACV')
measurement_device.write(':MAIN:RANG:VAL 1e0')
frequencies = np.logspace(2, 5, 31)

measured_voltages = []
theoretical_voltages = []

plt.ion()
fig, ax = plt.subplots()
line_measured, = ax.semilogx([], [], 'bo-', label='Measured [V]')  # 青のプロット
line_theoretical, = ax.semilogx([], [], 'r--', label='Theoretical [V]')  # 赤のプロット
ax.set_xlabel('Frequency [Hz]')
ax.set_ylabel('Voltage [V]')
ax.set_title('Voltage vs Frequency')
ax.legend()
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

for idx, freq in enumerate(frequencies):
    measured_voltage = get_voltage(freq)
    theoretical_voltage = calculate_capacitor_voltage(freq, R, C)
    print(f'Frequency: {freq:.2f} Hz, Measured Voltage: {measured_voltage:.2f} V, Theoretical Voltage: {theoretical_voltage:.2f} V')
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

np.savetxt('rei4in.csv', np.array([frequencies, measured_voltages, theoretical_voltages]).T, delimiter=',')
measurement_device.close()
function_generator.close()
rm.close()
plt.show()
