# This file is part of amasya-wifi-login.
#
# Copyright (C) 2024 bariscodefx
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

class parserLib:
	def __init__(self):
		pass

	@staticmethod
	def get_login_url(response):
		login_url = response.content.decode('utf-8')
		start_index = login_url.find('window.location="') + len('window.location="')
		end_index = login_url.find('"', start_index)
		login_url = login_url[start_index:end_index]
		return login_url

	@staticmethod
	def extract_magic_value(content):
		magic_start = content.find('<input type="hidden" name="magic" value="') + len('<input type="hidden" name="magic" value="')
		magic_end = content.find('"', magic_start)
		return content[magic_start:magic_end]