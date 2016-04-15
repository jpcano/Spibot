import webiopi
import time
from PololuQik import FourWheelBot


bot = FourWheelBot()

@webiopi.macro
def speed(val):
    # speed = int(round(int(val)*127/100))
    # print(int(val))
    bot.setSpeed(int(val))
    print('Speed: ' + val)

@webiopi.macro
def turnRatio(val):
    bot.setTurnSpeed(float(val))
    print('Turn ratio: ' + val)

@webiopi.macro
def rotSpeed(val):
    bot.setRotSpeed(int(val))
    print('Rot Speed: ' + val)

@webiopi.macro
def go_fl():
    bot.fl()
    print('Forward Left')

@webiopi.macro
def go_f():
    bot.f()
    print('Forward')
    # uart.write(bytes("\xAA\x09\x08\x7F", 'latin1'))
    # uart.write(bytes("\xAA\x09\x0C\x7F", 'latin1'))

@webiopi.macro
def go_fr():
    bot.fr()
    print('Forward Right')

@webiopi.macro
def go_l():
    bot.l()
    print('Left')

@webiopi.macro
def brake(value):
    print('Brake: ' + value)

@webiopi.macro
def go_r():
    bot.r()
    print('Right')


@webiopi.macro
def go_bl():
    bot.bl()
    print('Backward Left')

@webiopi.macro
def go_b():
    bot.b()
    print('Backward')
    # uart.write(bytes("\xAA\x09\x0A\x7F", 'latin1'))
    # uart.write(bytes("\xAA\x09\x0E\x7F", 'latin1'))

@webiopi.macro
def go_br():
    bot.br()
    print('Backward Right')

@webiopi.macro
def stop():
    # time.sleep(4)
    bot.setCoast()
    print('Stop')

# Called by WebIOPi at script loading
def setup():
    # uart.write(bytes("\xAA\x09\x04\x00\x0A\x55\x2A", 'latin1'))
    print('Starting cambot')
    print('Coasting motors...done')
    bot.setCoast()

a = 0
def loop():
    global a
    print('####### WatchDog ' + str(a) + ' minutes #######')
    a += 1
    time.sleep(60)

# Called by WebIOPi at server shutdown
def destroy():
    print('Stopping cambot')
    print('Coasting motors...done')
    bot.setCoast()
