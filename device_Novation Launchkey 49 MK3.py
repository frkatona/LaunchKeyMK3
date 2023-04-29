# name=FRK Launchkey 49 MKII
# forked from Shelton Chiramal - https://github.com/tenshells/LaunchKeyMK3

import transport
import midi
import mixer
import general
import device
import ui
import channels
import playlist
import launchMapPages
import plugins
# import pykeys

play_button = 115
stop_button = 114
record_button = 117
undo_button = 77
loop_button = 118

prev =103
next =102

capmidi = 74
quant = 75
metro = 76
DeviceSelect =51
DeviceLock = 52
DS = -1

RightArrow = 104
SSM = 105

UpArrow = 106
DownArrow = 107

fadbut1 = 11

fader = (71,72,73,74,75,76,77,78,79)
knobs = [21,22,23,24,25,26,27,28]

# def OnInit():
    # light up the buttons
    # for i in range(0, 16):
    #     device.midiOutMsg(0x90, i, 0x7F)

def OnMidiMsg(transport_controller):

    print(transport_controller.midiId,transport_controller.status, transport_controller.port, transport_controller.data1, transport_controller.data2)
    transport_controller.handled= False

    if transport_controller.midiId == midi.MIDI_CONTROLCHANGE:

        tc = transport_controller
        global Mr,Ml,Mu,Md
        if transport_controller.data2 > 0 and transport_controller.midiId ==176:
            
            ## Basic Transport Controls ##
            if transport_controller.data1 == play_button:
                transport.start()
                transport_controller.handled = True
            if transport_controller.data1 == stop_button:
                transport.stop()
                transport_controller.handled = True
            if transport_controller.data1 == record_button:
                transport.record()
                transport_controller.handled = True
            if transport_controller.data1 == loop_button:
                transport.setLoopMode()
            if transport_controller.data1 == next:
                ui.next()
                transport_controller.handled = True		
            if transport_controller.data1 == prev:
                ui.previous()
                transport_controller.handled = True	
            
            ## Plugin Preset Changes ##
            if transport_controller.data1 == UpArrow:
                print('prevPreset')
                plugins.prevPreset(channels.selectedChannel())
                transport_controller.handled = True	    
            if transport_controller.data1 == DownArrow:
                print('nextPreset')
                plugins.nextPreset(channels.selectedChannel())
                transport_controller.handled = True
            
            ## Editor Window Switching (Channel Rack -> Playlist -> Mixer) ##
            if transport_controller.data1 == DeviceSelect:
                if transport_controller.data2 == 127:
                    global DS
                    if DS == -1 or DS == 0:
                        ui.setFocused(1)
                        DS = 1
                        print("focus on racks yo")
                    elif DS == 1:
                        ui.setFocused(2)
                        DS = 2
                        print("focus on soul yo")
                    elif DS == 2:
                        ui.setFocused(0) 
                        DS = 0   
                        print("focus on picture yo")
                    transport_controller.handled = True
            
            #learn plugins 
            if transport_controller.data1 == DeviceLock:
                # print(f"the plugin in selected channel is {plugins.getPluginName(channels.selectedChannel())}")
                if plugins.getPluginName(channels.selectedChannel()) == "3x Osc":
                    print("Hey old triple :)")
                else:
                    print(f"Hey {plugins.getPluginName(channels.selectedChannel())} `)")
                print(f"I see you got {plugins.getParamCount(channels.selectedChannel())} parameters")
                for i in range(plugins.getParamCount(channels.selectedChannel())):
                    print(f"{i+1:2}  {plugins.getParamName(i,channels.selectedChannel()):25} is {plugins.getParamValue(i,channels.selectedChannel())}")
                transport_controller.handled = True
            
            #show editor at selected channel
            if transport_controller.data1 == RightArrow:
                print('RA: Show Editor at SC ')
                channels.showEditor(channels.selectedChannel())
                transport_controller.handled = True	
            
            #solo channel
            if transport_controller.data1 == SSM:
                print('Solo Channel')
                channels.soloChannel(channels.selectedChannel())
                transport_controller.handled = True	   
            
            #for transport controls who overlap with faders...
            if transport_controller.status == 191:
                if transport_controller.data1 == undo_button:    
                    print('Undo')
                    general.undo()
                    transport_controller.handled = True		
                if transport_controller.data1 == metro:
                    print('Metronome')
                    transport.globalTransport(midi.FPT_Metronome,110)
                    transport_controller.handled = True	
                if transport_controller.data1 == quant:
                    print('Quick Quantise, tbd')
                    channels.quickQuantize(channels.selectedChannel)
                    transport_controller.handled = True	
                if transport_controller.data1 == capmidi:
                    print('Capture Midi,  tbd')
                    # transport.globalTransport(midi.FPT_Metronome,110)
                    transport_controller.handled = True	
        
        #for faders
        if transport_controller.status == 176:
            if transport_controller.data1 == fader[8]:
                print('Master Volume')
                mixer.setTrackVolume(0,0.63 * (transport_controller.data2 / 100))
                # if transport_controller.data2 == 127:
                #     print("Master capped at 100 :)")
                transport_controller.handled = True
            if transport_controller.data1 == fader[0]:
                print('Mixer Channel 1 Volume')
                mixer.setTrackVolume(1,0.63 * transport_controller.data2 / 100)
                transport_controller.handled = True
            if transport_controller.data1 == fader[1]:
                print('Mixer Channel 2 Volume')
                mixer.setTrackVolume(2,0.63 * transport_controller.data2 / 100)
                transport_controller.handled = True

        #for knobs
        if transport_controller.data1 == knobs[0]:
            print('Control Volume of Selected Channel')
            channels.setChannelVolume(channels.selectedChannel(),tc.data2/127)
            transport_controller.handled = True	        

        if transport_controller.data1 == knobs[1]:
            print('Control Pan of Selected Channel')
            channels.setChannelPan(channels.selectedChannel(),tc.data2/63.5 - 1)
            transport_controller.handled = True	           
    
    if transport_controller.midiId == 224:
        #int midiId, int channel, int data1, int data2
        for i in range(1, 125):
            device.midiOutMsg(144, 16, i, 50)  

        channels.setChannelPitch(channels.selectedChannel(),2,2)
        pro = transport_controller.data2 * 128 + transport_controller.data1        
        channels.setChannelPitch(channels.selectedChannel(),pro/8192 -1)
        transport_controller.handled = True	
