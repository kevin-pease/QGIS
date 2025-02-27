# The following has been generated automatically from src/core/locator/qgslocatorfilter.h
QgsLocatorFilter.Highest = QgsLocatorFilter.Priority.Highest
QgsLocatorFilter.High = QgsLocatorFilter.Priority.High
QgsLocatorFilter.Medium = QgsLocatorFilter.Priority.Medium
QgsLocatorFilter.Low = QgsLocatorFilter.Priority.Low
QgsLocatorFilter.Lowest = QgsLocatorFilter.Priority.Lowest
QgsLocatorFilter.Priority.baseClass = QgsLocatorFilter
QgsLocatorFilter.FlagFast = QgsLocatorFilter.Flag.FlagFast
QgsLocatorFilter.Flags = lambda flags=0: QgsLocatorFilter.Flag(flags)
QgsLocatorFilter.Flags.baseClass = QgsLocatorFilter
Flags = QgsLocatorFilter  # dirty hack since SIP seems to introduce the flags in module
def _force_int(v): return v if isinstance(v, int) else int(v.value)


QgsLocatorFilter.Flag.__bool__ = lambda flag: _force_int(flag)
QgsLocatorFilter.Flag.__eq__ = lambda flag1, flag2: _force_int(flag1) == _force_int(flag2)
QgsLocatorFilter.Flag.__and__ = lambda flag1, flag2: _force_int(flag1) & _force_int(flag2)
QgsLocatorFilter.Flag.__or__ = lambda flag1, flag2: QgsLocatorFilter.Flag(_force_int(flag1) | _force_int(flag2))
