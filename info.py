#!/usr/bin/env python
# -*- coding: utf-8 -*-
import commands
import os

def main():
    # 查看GPU温度
	gpu = commands.getoutput( '/opt/vc/bin/vcgencmd measure_temp' ).replace( 'temp=', '' ).replace( '\'C', '' )
	gpu = float(gpu)
	print('gpu Temp: %.2f ' % gpu)

    # 查看CPU温度
	file = open("/sys/class/thermal/thermal_zone0/temp")
	cpu = float(file.read()) / 1000
	file.close()
	print('cpu Temp: %2.2f' % cpu)
  		
	load_1min = str(os.popen("top -n1 | awk '/load average:/ {print $12}'").readline().strip()).replace(',', '' )
	load_5min = str(os.popen("top -n1 | awk '/load average:/ {print $13}'").readline().strip()).replace(',', '' )
	load_1min=float(load_1min)
	load_5min=float(load_5min)
	print('')	
	print('load_1min: %.2f'%load_1min)
	print('load_5min: %.2f'%load_5min)
	
	Ramused = str(os.popen("top -n1 | awk '/KiB/ {print $6}'").readline().strip()).replace(',', '' )
	Ramused = int(Ramused)
	Ramused = Ramused / 1000
	print('')
	print('Ramused: %d '%Ramused +' Mb')
	
	def getDiskSpace():
		p = os.popen("df -h /")
		i = 0
		while 1:
			i = i +1
			line = p.readline()
			if i==2:
				return(line.split()[1:5])

	# Disk information
	DISK_stats = getDiskSpace()
	DISK_total = DISK_stats[0].replace('G','')
	DISK_used = DISK_stats[1].replace('G', '' )
	DISK_perc = DISK_stats[3].replace('%', '' )
	print('')
	print('DISK_total: '+str(DISK_total)+' Gb')
	print('DISK_used: '+str(DISK_used)+' Gb')
	print('DISK_perc: '+str(DISK_perc)+' %')
if __name__ == '__main__':
    main()
