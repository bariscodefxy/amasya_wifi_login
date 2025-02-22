# This file is part of amasya-wifi-login.
#
# Copyright (C) 2024 bariscodefx
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

import httpx

class login_lib:
	@staticmethod
	def create_login_data(username, password):
		return {
			"username": username,
			"password": password
		}

	@staticmethod
	def perform_login(g_username, g_password):
		client = httpx.Client(follow_redirects=True, verify=False)
		data = login_lib.create_login_data(g_username, g_password)
		client.post("https://internet.amasya.edu.tr:8000/api/v1/auth/token", data=data)