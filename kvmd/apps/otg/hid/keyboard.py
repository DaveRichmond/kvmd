# ========================================================================== #
#                                                                            #
#    KVMD - The main Pi-KVM daemon.                                          #
#                                                                            #
#    Copyright (C) 2018  Maxim Devaev <mdevaev@gmail.com>                    #
#                                                                            #
#    This program is free software: you can redistribute it and/or modify    #
#    it under the terms of the GNU General Public License as published by    #
#    the Free Software Foundation, either version 3 of the License, or       #
#    (at your option) any later version.                                     #
#                                                                            #
#    This program is distributed in the hope that it will be useful,         #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of          #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           #
#    GNU General Public License for more details.                            #
#                                                                            #
#    You should have received a copy of the GNU General Public License       #
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.  #
#                                                                            #
# ========================================================================== #


from . import Hid


# =====
KEYBOARD_HID = Hid(
    protocol=1,
    subclass=1,

    report_length=8,

    report_descriptor=bytes([
        # https://www.kernel.org/doc/Documentation/usb/gadget_hid.txt

        # Keyboard
        0x05, 0x01,  # USAGE_PAGE (Generic Desktop)
        0x09, 0x06,  # USAGE (Keyboard)
        0xA1, 0x01,  # COLLECTION (Application)

        # Modifiers
        0x05, 0x07,  # USAGE_PAGE (Keyboard)
        0x19, 0xE0,  # USAGE_MINIMUM (Keyboard LeftControl)
        0x29, 0xE7,  # USAGE_MAXIMUM (Keyboard Right GUI)
        0x15, 0x00,  # LOGICAL_MINIMUM (0)
        0x25, 0x01,  # LOGICAL_MAXIMUM (1)
        0x75, 0x01,  # REPORT_SIZE (1)
        0x95, 0x08,  # REPORT_COUNT (8)
        0x81, 0x02,  # INPUT (Data,Var,Abs)

        # Reserved byte
        0x95, 0x01,  # REPORT_COUNT (1)
        0x75, 0x08,  # REPORT_SIZE (8)
        0x81, 0x03,  # INPUT (Cnst,Var,Abs)

        # LEDs output
        0x95, 0x05,  # REPORT_COUNT (5)
        0x75, 0x01,  # REPORT_SIZE (1)
        0x05, 0x08,  # USAGE_PAGE (LEDs)
        0x19, 0x01,  # USAGE_MINIMUM (Num Lock)
        0x29, 0x05,  # USAGE_MAXIMUM (Kana)
        0x91, 0x02,  # OUTPUT (Data,Var,Abs)

        # Reserved 3 bits in output
        0x95, 0x01,  # REPORT_COUNT (1)
        0x75, 0x03,  # REPORT_SIZE (3)
        0x91, 0x03,  # OUTPUT (Cnst,Var,Abs)

        # 6 keys
        0x95, 0x06,  # REPORT_COUNT (6)
        0x75, 0x08,  # REPORT_SIZE (8)
        0x15, 0x00,  # LOGICAL_MINIMUM (0)
        0x25, 0x65,  # LOGICAL_MAXIMUM (101)
        0x05, 0x07,  # USAGE_PAGE (Keyboard)
        0x19, 0x00,  # USAGE_MINIMUM (Reserved)
        0x29, 0x65,  # USAGE_MAXIMUM (Keyboard Application)
        0x81, 0x00,  # INPUT (Data,Ary,Abs)

        0xC0,  # END_COLLECTION
    ]),
)