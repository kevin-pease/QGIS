# The following has been generated automatically from src/gui/qgsmaptoolidentify.h
QgsMapToolIdentify.DefaultQgsSetting = QgsMapToolIdentify.IdentifyMode.DefaultQgsSetting
QgsMapToolIdentify.ActiveLayer = QgsMapToolIdentify.IdentifyMode.ActiveLayer
QgsMapToolIdentify.TopDownStopAtFirst = QgsMapToolIdentify.IdentifyMode.TopDownStopAtFirst
QgsMapToolIdentify.TopDownAll = QgsMapToolIdentify.IdentifyMode.TopDownAll
QgsMapToolIdentify.LayerSelection = QgsMapToolIdentify.IdentifyMode.LayerSelection
QgsMapToolIdentify.IdentifyMode.baseClass = QgsMapToolIdentify
QgsMapToolIdentify.VectorLayer = QgsMapToolIdentify.Type.VectorLayer
QgsMapToolIdentify.RasterLayer = QgsMapToolIdentify.Type.RasterLayer
QgsMapToolIdentify.MeshLayer = QgsMapToolIdentify.Type.MeshLayer
QgsMapToolIdentify.VectorTileLayer = QgsMapToolIdentify.Type.VectorTileLayer
QgsMapToolIdentify.PointCloudLayer = QgsMapToolIdentify.Type.PointCloudLayer
QgsMapToolIdentify.AllLayers = QgsMapToolIdentify.Type.AllLayers
QgsMapToolIdentify.LayerType = lambda flags=0: QgsMapToolIdentify.Type(flags)
QgsMapToolIdentify.LayerType.baseClass = QgsMapToolIdentify
LayerType = QgsMapToolIdentify  # dirty hack since SIP seems to introduce the flags in module
def _force_int(v): return v if isinstance(v, int) else int(v.value)


QgsMapToolIdentify.Type.__bool__ = lambda flag: _force_int(flag)
QgsMapToolIdentify.Type.__eq__ = lambda flag1, flag2: _force_int(flag1) == _force_int(flag2)
QgsMapToolIdentify.Type.__and__ = lambda flag1, flag2: _force_int(flag1) & _force_int(flag2)
QgsMapToolIdentify.Type.__or__ = lambda flag1, flag2: QgsMapToolIdentify.Type(_force_int(flag1) | _force_int(flag2))
