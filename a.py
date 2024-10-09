#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import subprocess

def GetCpuFreq():
    Cmd = 'vcgencmd measure_clock arm'
    result = subprocess.Popen(Cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    Rstdout, Rstderr = result.communicate()
    CpuFreq = Rstdout.split('=')
    return int(CpuFreq[1])

def GetCpuTemp():
    Cmd = 'vcgencmd measure_temp'
    result = subprocess.Popen(Cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    Rstdout, Rstderr = result.communicate()
    CpuTemp = Rstdout.split()
    return CpuTemp[0]

def GetDevVolt():
    Cmd = 'vcgencmd measure_volts'
    result = subprocess.Popen(Cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    Rstdout, Rstderr = result.communicate()
    devvolt = Rstdout.split()
    return devvolt[0]

def GetCpuStat():
    Cmd = 'cat /proc/stat | grep cpu'
    result = subprocess.Popen(Cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    Rstdout, Rstderr = result.communicate()
    LineList = Rstdout.splitlines()

    TckList = []
    for Line in LineList:
        ItemList = Line.split()
        TckIdle = int(ItemList[4])
        TckBusy = int(ItemList[1]) + int(ItemList[2]) + int(ItemList[3])
        TckAll = TckBusy + TckIdle
        TckList.append([TckBusy, TckAll])
    return TckList

def GetMemoryUsage():
    Cmd = 'free -m'  # メモリ使用量をMB単位で取得
    result = subprocess.Popen(Cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    Rstdout, Rstderr = result.communicate()
    MemInfo = Rstdout.splitlines()[1].split()
    TotalMem = MemInfo[1]
    UsedMem = MemInfo[2]
    return int(UsedMem), int(TotalMem)

def GetTopMemoryProcess():
    Cmd = "ps -eo pid,comm,%mem --sort=-%mem | head -n 2 | tail -n 1"  # メモリ使用量が最も多いプロセスを取得
    result = subprocess.Popen(Cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    Rstdout, Rstderr = result.communicate()
    return Rstdout.strip()

class CpuUsage:
    def __init__(self):
        self._TckList = GetCpuStat()

    def get(self):
        TckListPre = self._TckList
        TckListNow = GetCpuStat()
        self._TckList = TckListNow
        CpuRateList = []
        for (TckNow, TckPre) in zip(TckListNow, TckListPre):
            TckDiff = [Now - Pre for (Now, Pre) in zip(TckNow, TckPre)]
            TckBusy = TckDiff[0]
            TckAll = TckDiff[1]
            CpuRate = int(TckBusy * 100 / TckAll)
            CpuRateList.append(CpuRate)
        return CpuRateList

if __name__ == '__main__':
    gCpuUsage = CpuUsage()  # 初期化
    for _ in range(10000):
        time.sleep(1)
        CpuRateList = gCpuUsage.get()
        CpuRate = CpuRateList[0]
        CpuRate_str = "  CPU:%3d" % CpuRate
        del CpuRateList[0]
        CpuTemp = GetCpuTemp()
        CpuFreq = int(GetCpuFreq() / 1000000)
        CpuFreq_str = "ARM %4dMHz  " % CpuFreq
        DevVolt = GetDevVolt() + " "
        
        UsedMem, TotalMem = GetMemoryUsage()
        MemUsage_str = "MEM: %d/%dMB " % (UsedMem, TotalMem)
        
        TopProcess = GetTopMemoryProcess()
        Info_str = DevVolt + CpuFreq_str + CpuTemp + CpuRate_str + "%" + " " + MemUsage_str + "TOP: " + TopProcess
        print(Info_str, CpuRateList)
