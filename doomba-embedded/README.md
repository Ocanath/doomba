# Embedded Workspace
This directory contains submoduled eFW for this project. Make sure to check out all submodules with `git submodule update --init --recursive`.

There is a mix of STM32 and platformio for ESP32 firmware linked here. Each has an associated README. See below for toolchain setup.

## Building

### STM32 Firmware

 Use embedded/ as your STM32CubeIDE workspace and import each as an existing STM32CubeIDE project.
 They should build within STM32CubeIDE (1.14.0) without issue.

### ESP32 Firmware

Use the platformio extension to build the ESP32 code.

