
from struct import *
import winreg

key=winreg.OpenKey(winreg.HKEY_CURRENT_USER,"Software\Microsoft\Windows\CurrentVersion\Internet Settings\Connections", 0, winreg.KEY_ALL_ACCESS)
set_register = b'F\x00\x00\x00T\x01\x00\x00\x03\x00\x00\x00\x0e\x00\x00\x00127.0.0.1:8080\x0b\x00\x00\x00<-loopback>\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
winreg.SetValueEx(key, "DefaultConnectionSettings", None, winreg.REG_BINARY, set_register)

# (value, regtype) = winreg.QueryValueEx(key, "DefaultConnectionSettings")
# original_register = unpack("=8sc7s19sc20s51s", value)

# print(value)

# # x = original_register

# # if x[1] == bytes(chr(0x03), "utf-8"):
# #     x1 = bytes(chr(0x01), "utf-8")
# # else:
# #     x1 = bytes(chr(0x03), "utf-8")

# # myregister = pack("=8sc7s19sc20s51s", *(x[0], x1, x[2], *x[3:]))

# # print(myregister)
# print(set_register)
# print(value)

# winreg.SetValueEx(key, "DefaultConnectionSettings", None, regtype, set_register)