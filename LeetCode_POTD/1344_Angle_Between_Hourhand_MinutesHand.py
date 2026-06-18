# 1344. Angle Between Hands of a Clock
# TC = O(1) and SC = O(1)
def angleClock(self, hour, minutes):
    hour %= 12
    hour_angle = 30 * hour + 0.5 * minutes
    minute_angle = 6 * minutes
    angle = abs(hour_angle - minute_angle)
    return min(angle, 360- angle)


# gfg format where string is given with combine hours and minutes
# TC = O(1) and SC = O(1)

def getAngle(self, s: str) -> float:    
    hour , minutes = map(int, s.split(':'))
    hour %= 12
    hour_angle = 30 * hour + 0.5 * minutes
    minute_angle = 6 * minutes
    angle = abs(hour_angle - minute_angle)
    return min(angle, 360 - angle)