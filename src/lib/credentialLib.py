# This file is part of amasya-wifi-login.
#
# Copyright (C) 2024 bariscodefx
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

class credentialLib:
    def __init__(self):
        pass
    
    @staticmethod
    def read_credentials():
        try:
            with open('./ayarlar.txt', 'r') as file:
                username = file.readline().strip()
                password = file.readline().strip()
            return username, password
        except FileNotFoundError:
            print("Hata: ayarlar.txt dosya bulunamadi.")
            return None, None
        except IOError:
            print("Hata: ayarlar.txt dosyasini okunamadi.")
            return None, None