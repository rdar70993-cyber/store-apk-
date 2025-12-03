
[app]
title = Store AP
package.name = storeap
package.domain = org.reza
source.dir = .
source.include_exts = py,kv,png,jpg,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 1

[buildozer]
log_level = 2

[android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.build_tools_version = 33.0.2
android.arch = armeabi-v7a
android.permissions = INTERNET