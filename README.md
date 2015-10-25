Microsoft-27Mhz-Keyboard-Decoder
================================

This uses python and GNURadio to remotely decode keystrokes from a Microsoft 27mhz keyboard.  

The code quality and signal processing "reliablity" are not great.  If you are a government with a big budget for this and want it to be great, operators are standing by.  Additional filtering and receiver amplification and gain tweaking would greatly improve the range and reliability to an estimated 100' using an omnidirectional antenna.  

Keystrokes have been modified until I have another keyboard's data to segment out the keyboard ID's part of the signal.  Mouse data filtering/extraction has been removed since nothing was being done with the data. Update: After seeing Samy's work, the XOR key may be unique per keyboard, so this can either be cracked (Samy has done this), or just solved for the specific keyboard if you're trying to make  PoC.

Talk vid: https://www.youtube.com/watch?v=Jhak0hezZfg
