# The following has been generated automatically from src/gui/qgsmaptool.h
QgsMapTool.Transient = QgsMapTool.Flag.Transient
QgsMapTool.EditTool = QgsMapTool.Flag.EditTool
QgsMapTool.AllowZoomRect = QgsMapTool.Flag.AllowZoomRect
QgsMapTool.ShowContextMenu = QgsMapTool.Flag.ShowContextMenu
QgsMapTool.Flags = lambda flags=0: QgsMapTool.Flag(flags)
def _force_int(v): return v if isinstance(v, int) else int(v.value)


QgsMapTool.Flag.__bool__ = lambda flag: _force_int(flag)
QgsMapTool.Flag.__eq__ = lambda flag1, flag2: _force_int(flag1) == _force_int(flag2)
QgsMapTool.Flag.__and__ = lambda flag1, flag2: _force_int(flag1) & _force_int(flag2)
QgsMapTool.Flag.__or__ = lambda flag1, flag2: QgsMapTool.Flag(_force_int(flag1) | _force_int(flag2))
