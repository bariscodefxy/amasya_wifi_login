# This file is part of amasya-wifi-login.
#
# Copyright (C) 2024 bariscodefx
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

import httpx
from lib.parserLib import parserLib

class loginLib:
	@staticmethod
	def create_login_data(username, password, magic_value, login_url):
		return {
			"username": username,
			"password": password,
			"magic": magic_value,
			"4TRedir": login_url
		}

	@staticmethod
	def perform_login(g_username, g_password):
		client = httpx.Client(follow_redirects=True, verify=False)
		request = client.build_request("GET", "http://kimlikdogrulama.amasya.edu.tr:1000/logout?")

		login_url = None
		while login_url is None:
			response = client.send(request)
			login_url = parserLib.get_login_url(response)

            # If the response contains "Firewall Authentication Logout", it means the user is already logged in
			# Fortinet Firewall Authentication Logout
			if "Firewall Authentication Logout" in response.content.decode('utf-8'):
				login_url = None
			else:
				request = client.build_request("GET", login_url)
				response = client.send(request)
				content = response.content.decode('utf-8')
				
				magic_value = parserLib.extract_magic_value(content)
				
				data = loginLib.create_login_data(g_username, g_password, magic_value, login_url)

				response = client.post("http://kimlikdogrulama.amasya.edu.tr:1000/", data=data)