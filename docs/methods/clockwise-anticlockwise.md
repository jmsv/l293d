The `DC.clockwise()` and `DC.anticlockwise()` methods can
take optional parameters to extend their functionality

## Parameters

 
### `duration`

- **Type:** Number - _`int` or `float`_
- **Default:** `None` - _Turns motor on until `stop` is manually called_

The `duration` parameter can be used to make the motor spin for a number of seconds.
For example, use `motor.clockwise(duration=3)` to make a motor (`DC` object named `motor`)
spin clockwise for 3 seconds.


### `wait`

- **Type:** Boolean - _`bool`_
- **Default:** `True` - _Method doesn't return until motor has stopped_

If the `duration` parameter is being used to make the motor spin for a number of seconds,
the `wait` parameter can be used


### `speed`

- **Type:** Tuple - _`tuple`_ / _`PWM`_
- **Default:** `100` - _Motor runs at a 100% duty cycle (full speed)_

The `speed` parameter can be used to control how fast the motor spins using
[PWM (Pulse Width Modulation)](https://en.wikipedia.org/wiki/Pulse-width_modulation).

`speed` can be either a tuple or an integer. When using a tuple, order matters
and it should be `(frequency, duty_cycle)`.

There is also the option to be explict and use the `l293d.PWM` namedtuple which
takes the 2 keyword arguments: `l293d.PWM(freq=x, cycle=x)`.

#### PWM examples

```python
import l293d

motor = l293d.DC(22, 18, 16)

# pre-define a pwm
pwm = l293d.PWM(freq=30, cycle=70)
motor.clockwise(speed=pwm)

# or use it directly in the method call
motor.clockwise(speed=l293d.PWM(freq=50, cycle=50))

# keywords aren't required
motor.clockwise(speed=l293d.PWM(50, 50))

# normal tuples work too
motor.clockwise(speed=(20, 30))

# an integer can be used if you want the same frequency and duty cycle
motor.clockwise(speed=50)
```



## Implementation Examples

```python
import l293d
motor = l293d.DC(15, 18, 11)
```


- `motor.clockwise()`

   Turns `motor` on in the clockwise direction. Doesn't stop until `motor.stop()` is called

- `motor.anticlockwise(3.5)`

   As `duration` is the first parameter of the `anticlockwise` and `clockwise` methods,
   the line above would make `motor` spin for 3.5 seconds before the method returns

- `motor.clockwise(7, wait=False)`

   `motor` spins for 7 seconds, but the method returns immediately.
   This means that any code following this line won't be delayed. 
