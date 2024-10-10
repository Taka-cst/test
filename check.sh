!/bin/sh
while [ true ];
do
echo -n $(
vcgencmd measure_temp
cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq
)
echo Hz
sleep 5
done