## Change logs

# v2.0.0
* Changed the default target sampling rate from 44.1 kHz to 48 kHz because YTM recently changed its streaming format from AAC (141; 44.1 kHz & 256 kbps stereo) to Opus (774; 48 kHz & 256 kbps vbr stereo), Am@zon music had already changed its SD format from AAC (44.1 kHz & 256 kbps stereo) to Opus (48 kHz & 192 kbps vbr stereo) and YT had adopted Opus (251; 48 kHz & 160 kbps vbr stereo); Though this change affects very little for 44.1 kHz tracks (of which cut-off changes 20 kHz to 19 kHz)
* Note that Opus encoders enforce low-pass filtering (cut-off: 20 kHz), but their decoders output ultra sonic noise by noise-shaping dithering when 16 bit depth outputting

# v1.0.3
* Changed the cut-off frequency from 94% to 93% for casual people to be appealed by its transparent

# v1.0.2
* Added a note for adjusting the cut-off for your devices

# v1.0.1
* Added settings for Hires. tracks commented out in "service.sh" for those who like Hires. tracks even on "cheapie" devices anyhow

# v1.0.0
* Initial Release

##
