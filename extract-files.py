#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2025 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

module = ExtractUtilsModule(
    'dolby',
    'sony',
    device_rel_path='vendor/sony/dolby',
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
