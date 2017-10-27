# -*- coding: utf-8 -*-
from Ec2EasyLauncher import Ec2EasyLauncher

e = Ec2EasyLauncher()
r = e.stop("your instanceId")
if r["Name"] == "stopped":
	# success
	pass
else:
	# rror
	pass
