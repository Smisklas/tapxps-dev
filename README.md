# tapxps-dev
RaspberryPi control system for tapxps acquisition at the species bemline

Contains basic RPi GPIO classes for controlling two valves and a modified PWM device for detector gating. In addition, the repository contains a GUI which controls the valves and detector gating during acquisition. The different parameters can be set between acquisitions and the software works in automatic- and manual modes. Manual mode allows for independent operation of the valves but disables the detector triggereing while automatic mode disables manual operation of the valves but instead allows for cyclic pulsing and triggering.
