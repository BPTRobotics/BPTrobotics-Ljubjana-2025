from .utils import set_angle

__angle : float = 0

def steer(direction) -> None:
    global __angle
    if direction > 1 or direction < -1:
        raise ValueError(f"Direction can only be between -1.0 and 1.0. [{direction}]")
    
    __angle = direction
    
    set_angle( 90 * (direction + 1) )
    
def get_direction() -> float:
    return __angle