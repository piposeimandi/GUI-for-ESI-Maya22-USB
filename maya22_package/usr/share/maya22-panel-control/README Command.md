command / maya22-control.py
==========

This is control application for the [ESI Maya22](http://www.esi-audio.com/products/maya22usb/) usb sound device.

Features
--------

* Monitoring: Enable/Disable
* All output Enable/Disable
* Switch input: Line In, Mic, High-Z, Mic+High-Z, Mute
* Level: Input L&R, Output L&R


```
$ maya22-control.py -h
Usage: maya22-control.py [options]
Options:
  -e              Enumerate HID devices
  -i              Enable all outputs
  -I              Disable all outputs
  -d              Enable all options
  -c [channel]    Set input channel (mic, hiz, line, mic_hiz, mute)
  -M              Enable monitor
  -m              Disable monitor
  -l [volume]     Set input left volume (0-127)
  -r [volume]     Set input right volume (0-127)
  -L [volume]     Set output left volume (0-145)
  -R [volume]     Set output right volume (0-145)
  -h              Show this help message
```


