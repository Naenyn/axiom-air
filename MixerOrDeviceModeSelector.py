# Embedded file name: /Applications/Ableton Live 9 Suite.app/Contents/App-Resources/MIDI Remote Scripts/Axiom_AIR_Mini32/MixerOrDeviceModeSelector.py
from _Framework.ModeSelectorComponent import ModeSelectorComponent
from SessionNavigationComponent import SessionNavigationComponent
### Added by Naenyn 2013-11-05
from Push.SessionRecordingComponent import SessionRecordingComponent
from Push.ViewControlComponent import ViewControlComponent
from ClipCreator import ClipCreator
###

class MixerOrDeviceModeSelector(ModeSelectorComponent):
    """ Class that toggles between mixer and device modes """

    ### Modified by Naenyn 2013-11-05
    def __init__(self, parent, encoders, select_button, up_button, down_button, left_button, right_button, mixer, session, device, mixer_modes, device_nav):
        ModeSelectorComponent.__init__(self)
        self._parent = parent
    ###    
        self._session_navigation = SessionNavigationComponent(parent, name='Session_Navigation')
        self._encoders = encoders
        self._select_button = select_button
        self._up_button = up_button
        self._down_button = down_button
        self._left_button = left_button
        self._right_button = right_button
        self._mixer = mixer
        self._session = session
        self._device = device
        self._mixer_modes = mixer_modes
        self._device_nav = device_nav
        ### Added by Naenyn 2013-11-05
        self._clip_creator = ClipCreator()
        self._view_control = ViewControlComponent(name='View_Control')
        self._session_recording = SessionRecordingComponent(self._clip_creator, self._view_control, name='Session_Recording')
        ###

    def disconnect(self):
        self._encoders = None
        self._select_button = None
        self._up_button = None
        self._down_button = None
        self._left_button = None
        self._right_button = None
        self._mixer = None
        self._session = None
        self._device = None
        self._mixer_modes = None
        self._device_nav = None
        ModeSelectorComponent.disconnect(self)
	return

    def number_of_modes(self):
        return 3

    def update(self):
        if self.is_enabled():
            if self._mode_index == 0:
                self._device.set_parameter_controls(None)
                self._mixer_modes.set_controls(self._encoders)
                self._device.set_bank_nav_buttons(None, None)
                self._device_nav.set_device_nav_buttons(None, None)
                ### Modified by Naenyn 2013-11-05
                # self._mixer.set_select_buttons(self._down_button, self._up_button)
                # self._session.set_track_bank_buttons(self._right_button, self._left_button)
                # self._mixer.selected_strip().set_arm_button(self._select_button)
                self._session_navigation.set_prev_track_button(self._left_button)
                self._session_navigation.set_next_track_button(self._right_button)
                self._session_navigation.set_prev_scene_button(self._up_button)
                self._session_navigation.set_next_scene_button(self._down_button)
                self._device.set_on_off_button(None)
                self._session_recording.set_record_button(self._select_button)
                ###
            elif self._mode_index == 1:
                self._mixer_modes.set_controls(None)
                self._device.set_parameter_controls(self._encoders)
                self._mixer.set_select_buttons(None, None)
                self._session.set_track_bank_buttons(None, None)
                ### Modified by Naenyn 2013-11-05
                # self._mixer.selected_strip().set_arm_button(None)
                self._session_navigation.set_prev_track_button(None)
                self._session_navigation.set_next_track_button(None)
                self._session_navigation.set_prev_scene_button(None)
                self._session_navigation.set_next_scene_button(None)                
                self._device.set_bank_nav_buttons(self._up_button, self._down_button)
                self._device_nav.set_device_nav_buttons(self._left_button, self._right_button)
                self._session_recording.set_record_button(None)
                self._device.set_on_off_button(self._select_button)
                ###
            elif self._mode_index == 2:
                self._mixer_modes.set_controls(None)
                self._device.set_parameter_controls(None)
                self._device.set_bank_nav_buttons(None, None)
                self._device_nav.set_device_nav_buttons(None, None)
                self._mixer.set_select_buttons(None, None)
                self._session.set_track_bank_buttons(None, None)
                self._device.set_on_off_button(None)
                self._mixer.selected_strip().set_arm_button(None)
	return
