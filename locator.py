import requests
from datetime import datetime
import turtle

# Part A
astros = requests.get('http://api.open-notify.org/astros.json').json()
print('There are ' + str(astros['number']) + ' astronauts in space:')
for person in astros['people']:
    print('- ' + person['name'] + ' on ' + person['craft'])

# Part B
iss_now = requests.get('http://api.open-notify.org/iss-now.json').json()
ts = iss_now['timestamp']
ts = datetime.utcfromtimestamp(ts).strftime('%H:%M:%S on %Y-%m-%d')
iss_lat = iss_now['iss_position']['latitude']
iss_lon = iss_now['iss_position']['longitude']
print('As of ' + ts + ', the ISS is at (' +
      str(iss_lat) + ', ' + str(iss_lon) + ')')

# Part D
payload = {'lat': 39.768518, 'lon': -86.158092}
iss_pass = requests.get(
    'http://api.open-notify.org/iss-pass.json', params=payload).json()
ts2 = iss_pass['response'][0]['risetime']
ts2 = datetime.utcfromtimestamp(ts2).strftime('%H:%M:%S on %Y-%m-%d')
print('The next time the ISS will pass over Indianapolis, IN is ' + ts2)

# Part C
screen = turtle.Screen()
screen.setup(720, 360)
screen.bgpic('map.gif')
screen.addshape('iss.gif')
turtle.color('white')
turtle.penup()
turtle.setposition(-86.158092*2, 39.768518*2)
turtle.dot()
turtle.dot(5, "yellow")
turtle.setheading(45)
turtle.forward(5)
turtle.write(ts2, True, align="left")
turtle.setposition(float(iss_lon)*2, float(iss_lat)*2)
turtle.shape('iss.gif')
turtle.done()
