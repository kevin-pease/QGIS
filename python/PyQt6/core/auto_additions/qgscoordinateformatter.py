# The following has been generated automatically from src/core/qgscoordinateformatter.h
QgsCoordinateFormatter.FormatPair = QgsCoordinateFormatter.Format.FormatPair
QgsCoordinateFormatter.FormatDegreesMinutesSeconds = QgsCoordinateFormatter.Format.FormatDegreesMinutesSeconds
QgsCoordinateFormatter.FormatDegreesMinutes = QgsCoordinateFormatter.Format.FormatDegreesMinutes
QgsCoordinateFormatter.FormatDecimalDegrees = QgsCoordinateFormatter.Format.FormatDecimalDegrees
QgsCoordinateFormatter.FlagDegreesUseStringSuffix = QgsCoordinateFormatter.FormatFlag.FlagDegreesUseStringSuffix
QgsCoordinateFormatter.FlagDegreesPadMinutesSeconds = QgsCoordinateFormatter.FormatFlag.FlagDegreesPadMinutesSeconds
QgsCoordinateFormatter.FormatFlags = lambda flags=0: QgsCoordinateFormatter.FormatFlag(flags)
def _force_int(v): return v if isinstance(v, int) else int(v.value)


QgsCoordinateFormatter.FormatFlag.__bool__ = lambda flag: _force_int(flag)
QgsCoordinateFormatter.FormatFlag.__eq__ = lambda flag1, flag2: _force_int(flag1) == _force_int(flag2)
QgsCoordinateFormatter.FormatFlag.__and__ = lambda flag1, flag2: _force_int(flag1) & _force_int(flag2)
QgsCoordinateFormatter.FormatFlag.__or__ = lambda flag1, flag2: QgsCoordinateFormatter.FormatFlag(_force_int(flag1) | _force_int(flag2))
