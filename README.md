Description 
-----------

This repo contains Ableton Live 9 python midi remote scripts for the M-Audio Axiom AIR Mini32 midi controller. The scripts included with Live out-of-the-box for this controller are buggy and needed enhancing. The scripts in this repo are based on decompiled python bytecode that is included with Ableton Live.

Features
--------

Volume/Pan Mode
- Navigation buttons up/down switch scenes in session view
- Navigation buttons left/right switch tracks in session (and arrange) view
- Select button (in the center of the navigation buttons) starts session recording
- Changing tracks auto-arms the newly selected track if it is armable

Instrument/FX Mode
- Navigation buttons up/down switch instrument banks
- Navigation buttons left/right switch devices in the device chain

The rest of the functionality was left as-is.

Installation
------------

1) Navigate to the Ableton Live bytecode directory:

 Mac OS:

/Applications/Ableton Live 9 Suite.app/Contents/App-Resources/MIDI Remote Scripts/Axiom_AIR_Mini32

 Windows:

C:\ProgramData\Ableton\Live 9\Resources\MIDI Remote Scripts\Axiom_AIR_Mini32 on Windows 7/8 and Vista and C:\Documents and Settings\All Users\Application Data\Ableton\Live 9\Resources\MIDI Remote Scripts\Axiom_AIR_Mini32 on Windows XP.

2) Move (not copy) the following files to a safe location:

AxiomAirMini32.pyc	 MixerOrDeviceModeSelector.pyc

3) Copy the three .py files from this repo in to the same directory.

4) Start up Live!
