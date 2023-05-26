import settings



def percentage_width(percent):
    """returns the percentage width of the game window for the frame"""
    return int((percent/100) * settings.WIDTH)

def percentage_height(percent):
    """returns the percentage height of the game window for the frame"""
    return int((percent/100)*settings.HEIGHT)

