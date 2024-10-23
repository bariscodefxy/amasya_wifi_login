# This file is part of amasya-wifi-login.
#
# Copyright (C) 2024 bariscodefx
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

from const._version import DEBUG

class loggerLib:
	def __init__(self):
		pass
	
	@staticmethod
	def debug(message):
		if DEBUG:
			print(f"[DEBUG] {message}")
	
	@staticmethod
	def info(message):
		print(f"[INFO] {message}")
