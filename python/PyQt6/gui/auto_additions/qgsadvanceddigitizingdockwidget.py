# The following has been generated automatically from src/gui/qgsadvanceddigitizingdockwidget.h
QgsAdvancedDigitizingDockWidget.AbsoluteAngle = QgsAdvancedDigitizingDockWidget.CadCapacity.AbsoluteAngle
QgsAdvancedDigitizingDockWidget.RelativeAngle = QgsAdvancedDigitizingDockWidget.CadCapacity.RelativeAngle
QgsAdvancedDigitizingDockWidget.RelativeCoordinates = QgsAdvancedDigitizingDockWidget.CadCapacity.RelativeCoordinates
QgsAdvancedDigitizingDockWidget.Distance = QgsAdvancedDigitizingDockWidget.CadCapacity.Distance
QgsAdvancedDigitizingDockWidget.CadCapacities = lambda flags=0: QgsAdvancedDigitizingDockWidget.CadCapacity(flags)
QgsAdvancedDigitizingDockWidget.CadCapacities.baseClass = QgsAdvancedDigitizingDockWidget
CadCapacities = QgsAdvancedDigitizingDockWidget  # dirty hack since SIP seems to introduce the flags in module
QgsAdvancedDigitizingDockWidget.ReturnPressed = QgsAdvancedDigitizingDockWidget.WidgetSetMode.ReturnPressed
QgsAdvancedDigitizingDockWidget.CadConstraint.NoLock = QgsAdvancedDigitizingDockWidget.CadConstraint.LockMode.NoLock
QgsAdvancedDigitizingDockWidget.CadConstraint.SoftLock = QgsAdvancedDigitizingDockWidget.CadConstraint.LockMode.SoftLock
QgsAdvancedDigitizingDockWidget.CadConstraint.HardLock = QgsAdvancedDigitizingDockWidget.CadConstraint.LockMode.HardLock
def _force_int(v): return v if isinstance(v, int) else int(v.value)


QgsAdvancedDigitizingDockWidget.CadCapacity.__bool__ = lambda flag: _force_int(flag)
QgsAdvancedDigitizingDockWidget.CadCapacity.__eq__ = lambda flag1, flag2: _force_int(flag1) == _force_int(flag2)
QgsAdvancedDigitizingDockWidget.CadCapacity.__and__ = lambda flag1, flag2: _force_int(flag1) & _force_int(flag2)
QgsAdvancedDigitizingDockWidget.CadCapacity.__or__ = lambda flag1, flag2: QgsAdvancedDigitizingDockWidget.CadCapacity(_force_int(flag1) | _force_int(flag2))
