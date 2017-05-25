### You will need:

- Raspberry Pi
- L293D chip(s)
- DC motor(s)
- Power-pack (4x AA or similar)
- Breadboard and wires

The L293D driver chips are very cheap to buy: I bought a bag of five [from Amazon](http://www.amazon.co.uk/dp/B008KYMVVY). Unless you intend to use more than two motors, only one driver chip is required; each L293D can drive up to two motors.

### 1. Powering the L293D chip

Power and ground setup - the chip should bridge the middle of the breadboard:

- The Pi's 5V → L293D pin 16 (see below image for numbering format)
- An empty power rail → L293D pin 8
- The Pi's ground (GND) → Breadboard ground rail(s)
- Ground rail(s) → L293D pins 4, 5, 12, and 13 pins (the middle ones)

![pin numbering image](http://i.imgur.com/RLGyWst.png?2)

The circuit should look like this:

![power pins image](http://i.imgur.com/awtfujg.png?1)

### 2. Data wires

The GPIO pins used in this example can be substitued for other valid pins, as long as continuity is maintained when [setting up a Python script](#python-scripts).

The Pi's GPIO needs to be wired to the L293D's data pins via the breadboard, as follows:

- GPIO 25 (pin 22) → L293D pin 1
- GPIO 24 (pin 18) → L293D pin 2
- GPIO 23 (pin 16) → L293D pin 7

Your circuit should now look something like this:

![data pins image](http://i.imgur.com/h5OQFZT.png?1)

### 3. Adding a motor

- Motor wire 1 → L293D pin 3
- Motor wire 2 → L293D pin 6

![one motor image](http://i.imgur.com/0PWp7vN.png?1)

You will also need to connect the battery pack to the power rail and the common ground rail - the one that connects to the L293D's pin 8.

_Note: It doesn't matter which motor wire is connected to 3 or 6, although this will affect the direction. When you've set up a [Python script](#python-scripts), if `clockwise()` makes the motor spin anti-clockwise, the two motor wires should be swapped._

### 4. Adding another motor (optional)

This is similar to how the first motor was connected, but the other side of the chip is used.

Data wires:

- GPIO 11 (pin 23) → L293D pin 9
- GPIO 9 (pin 21) → L293D pin 10
- GPIO 10 (pin 19) → L293D pin 15

Motor wires:

- Motor wire 1 → L293D pin 11
- Motor wire 2 → L293D pin 14

The circuit should now look something like this:

![two motors image](http://i.imgur.com/ryYQOr4.png?1)

More motors can be used with additional L293Ds. Just set up another chip as demonstrated above - each chip can drive a maximum of 2 motors.
