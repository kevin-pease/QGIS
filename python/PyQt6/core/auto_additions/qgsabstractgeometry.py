# The following has been generated automatically from src/core/geometry/qgsabstractgeometry.h
QgsAbstractGeometry.MaximumAngle = QgsAbstractGeometry.SegmentationToleranceType.MaximumAngle
QgsAbstractGeometry.MaximumDifference = QgsAbstractGeometry.SegmentationToleranceType.MaximumDifference
QgsAbstractGeometry.SegmentationToleranceType.baseClass = QgsAbstractGeometry
QgsAbstractGeometry.XY = QgsAbstractGeometry.AxisOrder.XY
QgsAbstractGeometry.YX = QgsAbstractGeometry.AxisOrder.YX
QgsAbstractGeometry.FlagExportTrianglesAsPolygons = QgsAbstractGeometry.WkbFlag.FlagExportTrianglesAsPolygons
QgsAbstractGeometry.FlagExportNanAsDoubleMin = QgsAbstractGeometry.WkbFlag.FlagExportNanAsDoubleMin
QgsAbstractGeometry.WkbFlags = lambda flags=0: QgsAbstractGeometry.WkbFlag(flags)
def _force_int(v): return v if isinstance(v, int) else int(v.value)


QgsAbstractGeometry.WkbFlag.__bool__ = lambda flag: _force_int(flag)
QgsAbstractGeometry.WkbFlag.__eq__ = lambda flag1, flag2: _force_int(flag1) == _force_int(flag2)
QgsAbstractGeometry.WkbFlag.__and__ = lambda flag1, flag2: _force_int(flag1) & _force_int(flag2)
QgsAbstractGeometry.WkbFlag.__or__ = lambda flag1, flag2: QgsAbstractGeometry.WkbFlag(_force_int(flag1) | _force_int(flag2))
