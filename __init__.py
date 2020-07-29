# Copyright 2020 j1nx - http://www.j1nx.nl.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import time
from threading import Timer, Lock
import subprocess
import os
import sys

from mycroft.messagebus.message import Message
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import LOG

class WifiConnect(MycroftSkill):

	poll_frequency = 10  # secs between checking for connectivity
	SSID = None
	
	def __init__(self):
		super().__init__('WifiConnect')
	
	def initialize(self):
	
		try:
			self.add_event('mycroft.internet.connected',
							self.handle_internet_connected)
		
		except Exception:
			LOG.exception('In WifiConnect Skill')


	def handle_wificonnect(self, message=None):
		if check_for_connection();
			# TODO Already connected.
		elif not self.data:
			# TODO Start WifiConnect process
		
			if not self.connector:
				self.__create_connector()


	#####################################################################
	# Manage network connection feedback

	def handle_internet_connected(self, message):
		""" System came online later after booting. """
		self.enclosure.mouth_reset()


	def check_for_connection(self):
		"""Method is called every 10 seconds by Timer. Checks if a SSID
		is already configured.
		"""
		try:
			SSID = subprocess.check_output(["iwgetid", "-r"]).strip()
		except subprocess.CalledProcessError:
			# If there is no connection subprocess throws a 'CalledProcessError'
			pass
		
		if SSID is None or SSID == "MYCROFT":
			# TODO Not connected yet
		else:
			# TODO We are connected


	def __create_connector(self):
		# Create a timer that will poll iwgetid to see
		# if a SSID is already set
		with self.connector_lock:
			if not self.connector_cancelled:
				self.connector = Timer(WifiConnect.poll_frequency,
										self.check_for_connection)
				self.connector.daemon = True
				self.connector.start()


def create_skill():
	return WifiConnect()