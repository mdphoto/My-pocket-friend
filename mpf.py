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
# 	print(rsync_command)
	return subprocess.check_call(rsync_command)	

# Controle de l'état de la liste "odir" tant que vide je boucle. Si liste avec contenue je sort de la boucle avec break
while 1:
# 	print("je suis dans la grosse liste")
	while len(odir) == 0:
		if len(odir) == 0:
			odir = os.listdir(dossierbase)
# 			print("la liste est 0", odir)
		else:
			break
	#  Je sais que la liste est ok donc je Rsync et a la fin je démonte la carte. donc la liste est vide le reprend la boucle du dessus.
	while len(odir) == 1 and os.path.ismount(dossierbase + odir[0]) == True:
		if os.path.exists(dossierbase + odir[0]) == True:
			source_path = (dossierbase + odir[0])
# 			print("la liste est 1", source_path)
# 			time.sleep(5)	
			rsync_backup(source_path, path_to_backup_file_name, exclude, engine_options)
			time.sleep(5)
			os.system("umount " + dossierbase + odir[0])
# 			print("fin", odir)	
			del odir[0]
		
