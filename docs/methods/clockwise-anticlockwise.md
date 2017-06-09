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


## Implementation Examples

```python
import l293d
motor = l293d.DC(15, 18, 11)
```


1. `motor.clockwise()`

   Turns `motor` on in the clockwise direction. Doesn't stop until `motor.stop()` is called

2. `motor.anticlockwise(3.5)`

   As `duration` is the first parameter of the `anticlockwise` and `clockwise` methods,
   the line above would make `motor` spin for 3.5 seconds before the method returns

3. `motor.clockwise(7, wait=False)`

   `motor` spins for 7 seconds, but the method returns immediately.
   This means that any code following this line won't be delayed. 
