# https://stackoverflow.com/questions/36976138/is-there-an-easy-way-to-convert-iso-8601-duration-to-timedelta
import isodate
# mediaPresentationDuration
# duration
print(isodate.parse_duration('PT605.1840209960938S'))

# 0:10:05.184021