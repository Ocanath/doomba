# Doomba

This is a top-level repository aggregating all resources developed for the doomba project, including PCB's, firmware, API's, and control software. It is an all-in-one package containing everything used to make doomba in one place.

## Embedded Workspace
This directory contains submoduled eFW for this project. Make sure to check out all submodules with `git submodule update --init --recursive`.

**Use the project root as your STM32CubeIDE workspace.**

Eclipse recursively finds projects from the workspace root. So foc-code within foc-actuator will show up no problem.

### ESP32 Firmware

The WIFI/ESP32 firmware can be found in [wifi-uart-bridge-esp32](doomba-embedded/wifi-uart-bridge-esp32/). You can build it using platformio. It is recommended to use the vscode extension for this.
