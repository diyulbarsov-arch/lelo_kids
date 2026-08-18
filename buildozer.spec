[app]

title = LE&LO kids
package.name = lelo_kids
package.domain = com.lelo

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0.0

requirements = python3,kivy==2.2.1,requests

orientation = portrait

fullscreen = 0

android.minapi = 21
android.api = 33
android.ndk = 28c
android.sdk = 33

android.enable_androidx = True
android.allow_backup = True
android.permissions = INTERNET

[buildozer]

log_level = 2
warn_on_root = 1
android.python_version = 3.10
android.p4a_blacklist = 3.14
