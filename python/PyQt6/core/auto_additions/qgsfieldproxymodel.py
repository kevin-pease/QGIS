# The following has been generated automatically from src/core/qgsfieldproxymodel.h
QgsFieldProxyModel.String = QgsFieldProxyModel.Filter.String
QgsFieldProxyModel.Int = QgsFieldProxyModel.Filter.Int
QgsFieldProxyModel.LongLong = QgsFieldProxyModel.Filter.LongLong
QgsFieldProxyModel.Double = QgsFieldProxyModel.Filter.Double
QgsFieldProxyModel.Numeric = QgsFieldProxyModel.Filter.Numeric
QgsFieldProxyModel.Date = QgsFieldProxyModel.Filter.Date
QgsFieldProxyModel.Time = QgsFieldProxyModel.Filter.Time
QgsFieldProxyModel.HideReadOnly = QgsFieldProxyModel.Filter.HideReadOnly
QgsFieldProxyModel.DateTime = QgsFieldProxyModel.Filter.DateTime
QgsFieldProxyModel.Binary = QgsFieldProxyModel.Filter.Binary
QgsFieldProxyModel.Boolean = QgsFieldProxyModel.Filter.Boolean
QgsFieldProxyModel.AllTypes = QgsFieldProxyModel.Filter.AllTypes
QgsFieldProxyModel.Filters = lambda flags=0: QgsFieldProxyModel.Filter(flags)
QgsFieldProxyModel.Filters.baseClass = QgsFieldProxyModel
Filters = QgsFieldProxyModel  # dirty hack since SIP seems to introduce the flags in module
def _force_int(v): return v if isinstance(v, int) else int(v.value)


QgsFieldProxyModel.Filter.__bool__ = lambda flag: _force_int(flag)
QgsFieldProxyModel.Filter.__eq__ = lambda flag1, flag2: _force_int(flag1) == _force_int(flag2)
QgsFieldProxyModel.Filter.__and__ = lambda flag1, flag2: _force_int(flag1) & _force_int(flag2)
QgsFieldProxyModel.Filter.__or__ = lambda flag1, flag2: QgsFieldProxyModel.Filter(_force_int(flag1) | _force_int(flag2))
