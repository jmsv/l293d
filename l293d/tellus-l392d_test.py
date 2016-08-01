from time import sleep
import l293d

m1 = l293d.motor(22, 16, 18)

m1.spin_clockwise(1)
sleep(1)
m1.spin_anticlockwise()
m1.stop(2)

