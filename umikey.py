#!/usr/bin/env python3

from yubikit.yubiotp import YubiOtpSession, SLOT, UpdateConfiguration
from ykman import scripting as s

try:
    yubikey = s.single()
except:
        print("Please plug in your YubiKey!")
        exit()

session = YubiOtpSession(yubikey.otp())
try:
    serial_number = bytes.fromhex(f"{yubikey.info.serial:#0{12}d}")
    session.update_configuration(
        slot=SLOT.ONE,
        cur_acc_code=serial_number,
        configuration=UpdateConfiguration(),
    )
    print("Access code removed. Enjoy!")
    exit()
except:
    print("Access code was not serial number, this is not a UMich YubiKey!\n(Who else would make this kind of mistake?)")
    exit()
