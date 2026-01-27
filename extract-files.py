#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2025 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)

from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

blob_fixups: blob_fixups_user_type = {
    (
        'vendor/lib/libdlbpreg.so',
        'vendor/lib/soundfx/libdlbvol.so',
        'vendor/lib64/libcodec2_soft_ac4dec.so',
        'vendor/lib64/libcodec2_soft_ddpdec.so',
        'vendor/lib64/libcodec2_soft_dolby.so',
        'vendor/lib64/libdlbdsservice.so',
        'vendor/lib64/libdlbpreg.so',
        'vendor/lib64/soundfx/libdlbvol.so'
    ): blob_fixup().replace_needed('libstagefright_foundation.so', 'libstagefright_foundation-v33.so'),
    # > 0011d960:  28ee 0546 2046 f8f0 2cef b5fa 85f0 4709  (..F F..,.....G.
    # > 0021f020:  0300 0000 474e 5500 a35c 635d 9a10 729b  ....GNU..\c]..r.
    # > 0021f030:  81ef 2b73 fb6c f363 0000 0000 0000 0000  ..+s.l.c........
    # ---
    # > 0011d960:  28ee 0546 2046 f8f0 2cef b5fa 85f0 0127  (..F F..,......'
    # > 0021f020:  0300 0000 474e 5500 77ce 5a95 5458 540e  ....GNU.w.Z.TXT.
    # > 0021f030:  7fff 1f55 18c7 34f6 0000 0000 0000 0000  ...U..4.........
  'vendor/lib/soundfx/libswdap.so': blob_fixup()
    .binary_regex_replace(rb'\x28\xee\x05\x46\x20\x46\xf8\xf0\x2c\xef\xb5\xfa\x85\xf0\x47\x09',
                          b'\x28\xee\x05\x46\x20\x46\xf8\xf0\x2c\xef\xb5\xfa\x85\xf0\x01\x27')
    .binary_regex_replace(rb'\x03\x00\x00\x00\x47\x4e\x55\x00\xa3\x5c\x63\x5d\x9a\x10\x72\x9b',
                          b'\x03\x00\x00\x00\x47\x4e\x55\x00\x77\xce\x5a\x95\x54\x58\x54\x0e')
    .binary_regex_replace(rb'\x81\xef\x2b\x73\xfb\x6c\xf3\x63\x00\x00\x00\x00\x00\x00\x00\x00',
                          b'\x7f\xff\x1f\x55\x18\xc7\x34\xf6\x00\x00\x00\x00\x00\x00\x00\x00')
    .replace_needed('libstagefright_foundation.so', 'libstagefright_foundation-v33.so'),
    # < 00146c60: 1f00 0071 e003 0091 f317 9f1a 4162 0494  ...q........Ab..
    # < 00146d80: 0900 0012 8902 090b 3f01 086b ca01 0054  ........?..k...T
    # ---
    # > 00146c60: 1f00 0071 e003 0091 1300 8052 4162 0494  ...q.......RAb..
    # > 00146d80: 0900 0012 8902 090b 3f01 086b 0e00 0014  ........?..k....
  'vendor/lib64/soundfx/libswdap.so': blob_fixup()
    .binary_regex_replace(b'\x1f\x00\x00\x71\xe0\x03\x00\x91\xf3\x17\x9f\x1a\x41\x62\x04\x94',
                          b'\x1f\x00\x00\x71\xe0\x03\x00\x91\x13\x00\x80\x52\x41\x62\x04\x94')
    .binary_regex_replace(rb'\x09\x00\x00\x12\x89\x02\x09\x0b\x3f\x01\x08\x6b\xca\x01\x00\x54',
                          b'\x09\x00\x00\x12\x89\x02\x09\x0b\x3f\x01\x08\x6b\x0e\x00\x00\x14')
    .replace_needed('libstagefright_foundation.so', 'libstagefright_foundation-v33.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'dolby',
    'sony',
    blob_fixups=blob_fixups,
    device_rel_path='vendor/sony/dolby',
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
