# Python Scripts

1. **Import the module**
   
   ```import l293d```

2. **Define motors**
   
   In this example, the GPIO pin numbers will be the same as listed in [Hardware Setup](#hardware-setup).
   
   ```motor1 = l293d.DC(22, 18, 16)```
   
   *Important note: `.DC` should only be used from version 0.2.2 onwards, `.Motor` should only be used for version 0.2.0 onwards and older versions: 0.1.7 or lower, use `.motor`.*
   
   'motor1' is what we're calling the motor. You can call it whatever you want, for example `wheel_motor`, `london_eye` or `evil_avocado`.
   
   The numbers correspond to which GPIO pins are connected to L293D pins 1, 2 and 7 respectively: the pins we set up in [Hardware Setup](#hardware-setup).

3. **Control motors**
   
   The statements to make the motor(s) spin are as follows:
   
   - `motor1.clockwise()`
   - `motor1.anticlockwise()`
   - `motor1.stop()`
   
   If, `clockwise()` and `anticlockwise()` spin the motor the wrong way, swap the two motor connections to the L293D chip, as explained in [Hardware Setup: Adding a motor](#adding-a-motor).

4. **Cleanup**
   
   I recommend that at the end of your script, you include the line: `l293d.cleanup()`, to cleanup the GPIO pins being used by the l293d library. This avoids damage to the GPIO pins; see [here](http://raspi.tv/2013/rpi-gpio-basics-3-how-to-exit-gpio-programs-cleanly-avoid-warnings-and-protect-your-pi).

   I also recommend that you set up '`try` `catch`' around motor calls to cleanup if any exceptions are encountered during use of this library.
