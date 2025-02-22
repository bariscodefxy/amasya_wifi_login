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
import random
from const._version import VERSION, DEBUG

from lib.connection_testing_lib import connection_testing_lib
from lib.credential_lib import credential_lib
from lib.login_lib import login_lib
from lib.logger_lib import logger_lib

g_username, g_password = credential_lib.read_credentials()
if g_username is None or g_password is None:
    logger_lib.info("Kimlik bilgileri okunamadı. Çıkılıyor.")
    exit(1)

logger_lib.info(f"Versiyon: {VERSION}")
logger_lib.info(f"Hata ayıklama: {DEBUG}")

is_first_connection = False

test_url = "https://bariscodefx.com.tr"

while True:
	logger_lib.info(f"Request testi yapılıyor: {test_url}")

	if not connection_testing_lib.test_connection(test_url):
		login_lib.perform_login(g_username, g_password)
		logger_lib.info("Giriş yapılmamış. Giriş işlemi yapılıyor.")
		is_first_connection = True
	else:
		logger_lib.debug("Request testi yapıldı. Giriş işlemi yapılmıyor.")

	time.sleep(10)

	if connection_testing_lib.test_connection('https://internet.amasya.edu.tr', check_captive=False):
		is_first_connection = False
