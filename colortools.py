import random
import colorsys

def random_hue(saturation: float = 1) -> tuple[int, int, int]:
    """Create an rgb tuple for a random color
    

    Args:
        saturation (float, optional): maximum saturation represented by fractions 0 to 1. Defaults to 1.

    Returns:
        tuple[int, int, int]: 
    """
    hue = random.randint(0, 360)
    color = colorsys.hls_to_rgb(hue / 360, 0.5, saturation)
    rgb = tuple(round(v * 255) for v in color)
    return rgb