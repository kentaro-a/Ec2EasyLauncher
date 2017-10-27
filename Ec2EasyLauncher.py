# -*- coding: utf-8 -*-
import boto3

class Ec2EasyLauncher(object):

	"""
		Initialize.
	"""
	def __init__(self):
		self.ec2 = boto3.resource('ec2')


	"""
		Start instances.
	"""
	def start(self, instanceId=""):
		ret = False
		if instanceId:
			self.ec2.instances.filter(InstanceIds=[instanceId]).start()
			ins = self.getInstanceById(instanceId)
			ins.wait_until_running()
			ret = ins.state
		return ret


	"""
		Stop instances.
	"""
	def stop(self, instanceId=""):
		ret = False
		if instanceId:
			self.ec2.instances.filter(InstanceIds=[instanceId]).stop()
			ins = self.getInstanceById(instanceId)
			ins.wait_until_stopped()
			ret = ins.state
		return ret


	"""
		Get instance by instanceId.
	"""
	def getInstanceById(self, instanceId):
		return self.ec2.Instance(instanceId)


