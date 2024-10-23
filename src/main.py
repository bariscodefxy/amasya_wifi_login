# This file is part of amasya-wifi-login.
#
# Copyright (C) 2024 bariscodefx
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import time

from const._version import VERSION, DEBUG
from lib.pingLib import pingLib
from lib.credentialLib import credentialLib
from lib.loginLib import loginLib
from lib.loggerLib import loggerLib

g_username, g_password = credentialLib.read_credentials()
if g_username is None or g_password is None:
    loggerLib.info("Kimlik bilgileri okunamadı. Çıkılıyor.")
    exit(1)

loggerLib.info(f"Versiyon: {VERSION}")
loggerLib.info(f"Hata ayıklama: {DEBUG}")

is_first_connection = False

while True:
	if not pingLib.ping('8.8.8.8') and pingLib.ping('kimlikdogrulama.amasya.edu.tr'):
		loginLib.perform_login()
	else:
		loggerLib.debug("Ping testi yapıldı. Giriş işlemi yapılmıyor.")

	if not is_first_connection:
		time.sleep(1)
		is_first_connection = True
	else:
		time.sleep(30)

	if not pingLib.ping('kimlikdogrulama.amasya.edu.tr'):
		is_first_connection = False
