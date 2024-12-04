import pyvisa #type: ignore
import time
import matplotlib.pyplot as plt
import numpy as np
rm=pyvisa.ResourceManager()
function_generator_address='GPIB0::2::INSTR'
function_generator=rm.open_resource(function_generator_address)
function_generator.write(':FUNC:SHAP SIN')
function_generator.write(':VOLT 1')
function_generator.write(':FREQ 1000')
function_generator.write(':OUTP ON')
time.sleep(5)

frequencies=np.logspace(2,5,16)
voltage=[]
for freq in frequencies:
    function_generator.write(f':FREQ {freq}')
    time.sleep(1)
    amplitude=float(function_generator.query(':VOLT?'))
    voltage.append(amplitude)
    function_generator.write(':MEAS:VOLT?')
    response=function_generator.read()
    print(f'取得電圧 :{response}\n')
function_generator.close()
rm.close()
