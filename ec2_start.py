# -*- coding: utf-8 -*-
from Ec2EasyLauncher import Ec2EasyLauncher

e = Ec2EasyLauncher()
r = e.start("your instanceId")
if r["Name"] == "running":
	# success
	pass
else:
	# error
	pass
