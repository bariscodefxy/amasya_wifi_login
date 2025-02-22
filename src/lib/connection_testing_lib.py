# This file is part of amasya-wifi-login.
#
# Copyright (C) 2024 bariscodefx
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

import httpx

class connection_testing_lib:
    def __init__(self):
        pass

    @staticmethod
    def test_connection(url, check_captive = True):
        try:
            response = httpx.get(url, timeout=3)
            if not check_captive:
                return response.status_code == 200

            if not b"Captive Portal" in response.content:
                return response.status_code == 200
            
            return False
        except httpx.RequestError:
            return False