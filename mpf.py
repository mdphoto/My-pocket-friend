#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pyudev
import os
import subprocess
import time

exclude = '"*."'
dossierbase = ('/media/')
odir = os.listdir(dossierbase)
path_to_backup_file_name = '/home/michel/photos'
engine_options = '-avrzt --info=progress2 --log-file=/home/michel/rsync.log'

def rsync_backup(source_path, path_to_backup_file_name, exclude, engine_options):
	exclusions = ['--exclude=%s' % x.strip() for x in exclude.split(',')]
	rsync_command = ['rsync'] + exclusions + engine_options.split() + [source_path + '/', path_to_backup_file_name]
	return subprocess.check_call(rsync_command)	

while 1:
	while len(odir) == 0:
		if len(odir) == 0:
			odir = os.listdir(dossierbase)
		else:
			break
	while len(odir) == 1 and os.path.ismount(dossierbase + odir[0]) == True:
		if os.path.exists(dossierbase + odir[0]) == True:
			source_path = (dossierbase + odir[0])	
			rsync_backup(source_path, path_to_backup_file_name, exclude, engine_options)
			time.sleep(5)
			os.system("umount " + dossierbase + odir[0])
			del odir[0]
		
