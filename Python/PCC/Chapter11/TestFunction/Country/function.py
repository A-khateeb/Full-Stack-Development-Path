def Country(city, country, population=''):
    if population:
        out_msg = city + ', ' + country +' -population: ' + population
    else:
        out_msg = city + ', ' + country
    return out_msg.title()
