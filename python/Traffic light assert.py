market_2nd = {'ns':'green','ew':'red'}
mission_24th = {'ew':'green','ns':'red'}

def switchlight(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] == 'yellow'
        elif stoplight[key] =='yellow':
            stoplight[key] == 'red'
        elif stoplight[key] =='red':
            stoplight[key] == 'green'
            assert 'red' in stoplight.values(), 'Neither light is red' + str(stoplight)

switchlight(market_2nd)
