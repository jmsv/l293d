This documentation should help create a basic Python script to get a motor working.
I'm currently working on better documentation for the methods used, as some have functionality not documented here.

### 1. Import the module

```python
import l293d 
```


### 2. Define motors

In this example, the GPIO pin numbers will be the same as listed in [Hardware Setup](hardware-setup.md).

```python
motor1 = l293d.DC(22, 18, 16)
```

In some cases, it may be necessary to use some pins that aren't considered valid, but we can force it 
by expliciting the `force_selection` parameter as `True` in DC class initialization (by default, this
parameter is `False`).

```python
motor1 = l293d.DC(19, 21, 23, force_selection=True)
```

In this case, 'motor1' is what we're calling the DC motor object. You can call it whatever you want,
for example `wheel_motor`, `london_eye` or `spinny_thing`.

The numbers correspond to which GPIO pins are connected to L293D pins 1, 2 and 7 respectively: the pins we set up in [Hardware Setup](hardware-setup.md).


### 3. Control motors

The statements to make the motor(s) spin are as follows:

- `motor1.clockwise()`
- `motor1.anticlockwise()`
- `motor1.stop()`

If, `clockwise()` and `anticlockwise()` spin the motor the wrong way, swap the two motor connections to
the L293D chip, as explained in [Hardware Setup: Adding a motor](hardware-setup.md#adding-a-motor).

I strongly recommend looking at the [Clockwise & Anticlockwise](../methods/clockwise-anticlockwise.md) docs -
these methods are more powerful than demonstrated above.


### 4. Cleanup

I recommend that at the end of your script, you include the line: `l293d.cleanup()`, to cleanup the GPIO pins being used by the l293d library. This avoids damage to the GPIO pins; see [here](http://raspi.tv/2013/rpi-gpio-basics-3-how-to-exit-gpio-programs-cleanly-avoid-warnings-and-protect-your-pi).

It would also be a good idea to set up '`try` `catch`' around motor driving calls to cleanup if any exceptions are raised.
