# FRK Launchkey 49 MKII

# Forked from Shelton Chiramal - https://github.com/tenshells/LaunchKeyMK3
# Color library from Miguel Guthridge - https://github.com/MiguelGuthridge/Universal-Controller-Script/

To-do:
 - Launchkey
   - [Reclaim original utility]
     - Get stop button to visually depress
     - Are my faders fucked? Bring back in the 25 and write its script
   - Should I replace ifs with elifs?
   - Patch change (FLEX presets) with the midi channel track buttons
   - Focus/minimize playlist/piano roll etc.
   - ‘Function’ key
     - Double utility of CCs
     - Convert single notes into chords
   - Light show
     - blink on metronome or linked to a peak controller
     - OnProjectLoad
     - OnPitchBend
   - Send different buttons to different channels
   - Better color randomization
 - Drums
   - Change midi notes instead of manually in drums
   - Adjust kick velocity
 - Controllers
   - turn foot on/off to latch switches

# Manual helpful bits

 - MIDI messages: https://www.manua.ls/novation/launchkey-49-mk2/manual?p=20

# Notes from Shelton's original Readme

Availible in 25,37,49,61 :

Transport: Play/Pause, Stop, Record, switch from Song Mode/Pattern Mode, Undo, Metronome(Click).
Device Select can be used to add new plugin to channel rack/mixer
Device Lock button next to knobs can be used to switch from Channel Rack -> Playlist -> Mixer
Jog buttons for previous/next for use in browser/Mixer/Channel Rack/switching presets in FL Stock plug-ins like Flex etc.
Stop Solo Mute button for Soloing Channel
Pitch Wheel for selected channel with semitone range +-12
First knob, Second Knob (in pot mode 1) Controls selected channel volume, pan
Avalible for 49,61 key versions: Faders: The faders have a max ceiling at 100% volume (0dB) to avoid clipping/ruining speakers :)

Master fader controls Master Volume
First 2 faders linked to first two Mixer Channels
Upcoming Support:

Plugin Support for FLEX, 3xOsc, FL keys..
Switching to Mixer using Device Lock Mode enables first 8 faders to control 8 mixer channel volumes
Control, Alt, Shift support in Launchpad probably with Up, Down
Quantize quick Quantizes selected channel

# Notes from documentation 

source: https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/midi_scripting.htm

FL window constants
Parameter	Value	Documentation
widMixer	0	Mixer
widChannelRack	1	Channel rack
widPlaylist	2	Playlist
widPianoRoll	3	Piano roll
widBrowser	4	Browser
widPlugin	5	Plugin window (only available inside getFocused function)
widPluginEffect	6	Effect Plugin window (only available inside getFocused/setFocused/getFocusedFormID functions)
widPluginGenerator	7	Generator Plugin window (only available inside getFocused/setFocused/getFocusedFormID functions)

# Color key (from image-line forums contributors)

"""
devices > novation > launchkey > mk3 > colors

Color definitions for the Novation Launchkey Mk3

Authors:
* Miguel Guthridge [hdsq@outlook.com.au, HDSQ#2154]

This code is licensed under GPL v3.
https://github.com/MiguelGuthridge/Universal-Controller-Script/blob/main/LICENSE
"""

from common.types.color import Color


COLORS = {
    #                 0xRRGGBB
    Color.fromInteger(0x000000):   0,  # Off
    Color.fromInteger(0x222222):   1,
    Color.fromInteger(0x5C656A):   2,  # Grey (default FL Color)
    Color.fromInteger(0xFFFFFF):   3,  # White
    Color.fromInteger(0xFF6658):   4,
    Color.fromInteger(0xFF2900):   5,  # Red
    Color.fromInteger(0x6E0A00):   6,
    Color.fromInteger(0x614F51):   7,  # Dark dull red
    Color.fromInteger(0xFFC875):   8,  # Light orange
    Color.fromInteger(0xFF6D00):   9,
    Color.fromInteger(0x6E2900):  10,
    Color.fromInteger(0x301F00):  11,
    Color.fromInteger(0xFDFA29):  12,
    Color.fromInteger(0xFDFA00):  13,  # Yellow
    Color.fromInteger(0x6B6900):  14,
    Color.fromInteger(0x201F00):  15,
    Color.fromInteger(0x8EF836):  16,
    Color.fromInteger(0x45F800):  17,
    Color.fromInteger(0x176900):  18,  # Dark dull green
    Color.fromInteger(0x173300):  19,
    Color.fromInteger(0x32F838):  20,
    Color.fromInteger(0x00F800):  21,
    Color.fromInteger(0x006800):  22,
    Color.fromInteger(0x001F00):  23,  # Dark green
    Color.fromInteger(0x31F857):  24,
    Color.fromInteger(0x00F800):  25,  # Green
    Color.fromInteger(0x006800):  26,
    Color.fromInteger(0x001F00):  27,
    Color.fromInteger(0x2FF990):  28,
    Color.fromInteger(0x00F84A):  29,
    Color.fromInteger(0x006919):  30,
    Color.fromInteger(0x002412):  31,
    Color.fromInteger(0x2AF9BE):  32,
    Color.fromInteger(0x00F8A2):  33,
    Color.fromInteger(0x006940):  34,
    Color.fromInteger(0x001F12):  35,
    Color.fromInteger(0x42CBFF):  36,
    Color.fromInteger(0x00B7FF):  37,  # Light blue
    Color.fromInteger(0x005164):  38,
    Color.fromInteger(0x001420):  39,
    Color.fromInteger(0x509CFF):  40,  # Very light blue
    Color.fromInteger(0x006CFF):  41,
    Color.fromInteger(0x00276D):  42,
    Color.fromInteger(0x000721):  43,
    Color.fromInteger(0x5865FF):  44,
    Color.fromInteger(0x0433FF):  45,  # Blue
    Color.fromInteger(0x01106E):  46,
    Color.fromInteger(0x000221):  47,  # Dark blue
    Color.fromInteger(0x9766FF):  48,
    Color.fromInteger(0x6435FF):  49,  # Purple
    Color.fromInteger(0x1D137A):  50,  # Indigo
    Color.fromInteger(0x0C0641):  51,  # Dark purple
    Color.fromInteger(0xFF6DFF):  52,
    Color.fromInteger(0xFF40FF):  53,  # Pink
    Color.fromInteger(0xDD61DD):  54,
    Color.fromInteger(0x220221):  55,
    Color.fromInteger(0xFF6796):  56,
    Color.fromInteger(0xFF2C64):  57,
    Color.fromInteger(0x6E0C23):  58,
    Color.fromInteger(0x2D0214):  59,  # Dark red
    Color.fromInteger(0xFF3300):  60,
    Color.fromInteger(0xAD4800):  61,
    Color.fromInteger(0x8E6300):  62,  # Brown
    Color.fromInteger(0x4D7400):  63,
    Color.fromInteger(0x004600):  64,
    Color.fromInteger(0x006541):  65,
    Color.fromInteger(0x006791):  66,
    Color.fromInteger(0x0433FF):  67,
    Color.fromInteger(0x005560):  68,
    Color.fromInteger(0x252ADB):  69,
    Color.fromInteger(0x8F8F8F):  70,
    Color.fromInteger(0x332B33):  71,
    Color.fromInteger(0xFF2900):  72,
    Color.fromInteger(0xC4F900):  73,
    Color.fromInteger(0xB7EC00):  74,
    Color.fromInteger(0x61F800):  75,  # Lime
    Color.fromInteger(0x009600):  76,
    Color.fromInteger(0x00F88D):  77,  # Teal
    Color.fromInteger(0x00B7FF):  78,
    Color.fromInteger(0x023FFF):  79,
    Color.fromInteger(0x4633FF):  80,
    Color.fromInteger(0x8C37FF):  81,  # Violet
    Color.fromInteger(0xC33290):  82,  # Dull pink
    Color.fromInteger(0x532B00):  83,
    Color.fromInteger(0xFF6200):  84,  # Orange
    Color.fromInteger(0x92E200):  85,  # Dull lime
    Color.fromInteger(0x72F800):  86,
    Color.fromInteger(0x00F800):  87,
    Color.fromInteger(0x00F800):  88,
    Color.fromInteger(0x4CF874):  89,
    Color.fromInteger(0x00F9D4):  90,
    Color.fromInteger(0x619CFF):  91,
    Color.fromInteger(0x3266D3):  92,  # Dull blue
    Color.fromInteger(0x9592F1):  93,
    Color.fromInteger(0xDE3FFF):  94,  # Pinker
    Color.fromInteger(0xFF2D6D):  95,
    Color.fromInteger(0xFF9100):  96,
    Color.fromInteger(0xC5BC00):  97,
    Color.fromInteger(0x98F800):  98,
    Color.fromInteger(0x956F00):  99,
    Color.fromInteger(0x4A3400): 100,
    Color.fromInteger(0x065C03): 101,
    Color.fromInteger(0x006147): 102,
    Color.fromInteger(0x181A36): 103,
    Color.fromInteger(0x132D6D): 104,
    Color.fromInteger(0x7E4D1D): 105,
    Color.fromInteger(0xBC1A00): 106,  # Dull red
    Color.fromInteger(0xE96844): 107,
    Color.fromInteger(0xE57D00): 108,
    Color.fromInteger(0xFFE400): 109,  # Light yellow
    Color.fromInteger(0xA7E300): 110,
    Color.fromInteger(0x6FBE00): 111,  # Dull green
    Color.fromInteger(0x242540): 112,
    Color.fromInteger(0xE2FA66): 113,
    Color.fromInteger(0x84F9C5): 114,
    Color.fromInteger(0xA7ABFF): 115,  # Light lilac
    Color.fromInteger(0x9E7DFF): 116,  # Lilac
    Color.fromInteger(0x515151): 117,
    Color.fromInteger(0x878787): 118,
    Color.fromInteger(0xE4FCFD): 119,
    Color.fromInteger(0xB51900): 120,
    Color.fromInteger(0x460400): 121,
    Color.fromInteger(0x00D500): 122,
    Color.fromInteger(0x004F00): 123,
    Color.fromInteger(0xC5BC00): 124,
    Color.fromInteger(0x4E3E00): 125,
    Color.fromInteger(0xC37100): 126,  # Dull orange
    Color.fromInteger(0x5D1C00): 127,
}



"It's not the startup animation. You can make the lights either be stationary, blink or pulse depending on the MIDI channel you send the color message to. Look at "Colouring the surface"."


"To set this up, turn off the inControl button for the pads and create a MIDI track that is outputting (“MIDI To”) to the Launchkey MkII InControl Port (Or Launchkey MIDI2). You will also need to assign the output to Channel 2,3 or 16."
