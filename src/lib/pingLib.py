# This file is part of amasya-wifi-login.
#
# Copyright (C) 2024 bariscodefx
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

import subprocess

class pingLib:
    def __init__(self):
        pass
    
    @staticmethod
    def ping(host):
        param = '-n' if subprocess.sys.platform.lower() == 'win32' else '-c'
        command = ['ping', param, '1', host]
        return subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0
