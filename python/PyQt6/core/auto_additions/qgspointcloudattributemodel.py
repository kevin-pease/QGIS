# The following has been generated automatically from src/core/pointcloud/qgspointcloudattributemodel.h
QgsPointCloudAttributeModel.AttributeNameRole = QgsPointCloudAttributeModel.FieldRoles.AttributeNameRole
QgsPointCloudAttributeModel.AttributeIndexRole = QgsPointCloudAttributeModel.FieldRoles.AttributeIndexRole
QgsPointCloudAttributeModel.AttributeSizeRole = QgsPointCloudAttributeModel.FieldRoles.AttributeSizeRole
QgsPointCloudAttributeModel.AttributeTypeRole = QgsPointCloudAttributeModel.FieldRoles.AttributeTypeRole
QgsPointCloudAttributeModel.IsEmptyRole = QgsPointCloudAttributeModel.FieldRoles.IsEmptyRole
QgsPointCloudAttributeModel.IsNumericRole = QgsPointCloudAttributeModel.FieldRoles.IsNumericRole
QgsPointCloudAttributeProxyModel.Char = QgsPointCloudAttributeProxyModel.Filter.Char
QgsPointCloudAttributeProxyModel.Short = QgsPointCloudAttributeProxyModel.Filter.Short
QgsPointCloudAttributeProxyModel.Int32 = QgsPointCloudAttributeProxyModel.Filter.Int32
QgsPointCloudAttributeProxyModel.Float = QgsPointCloudAttributeProxyModel.Filter.Float
QgsPointCloudAttributeProxyModel.Double = QgsPointCloudAttributeProxyModel.Filter.Double
QgsPointCloudAttributeProxyModel.Numeric = QgsPointCloudAttributeProxyModel.Filter.Numeric
QgsPointCloudAttributeProxyModel.AllTypes = QgsPointCloudAttributeProxyModel.Filter.AllTypes
QgsPointCloudAttributeProxyModel.Filters = lambda flags=0: QgsPointCloudAttributeProxyModel.Filter(flags)
QgsPointCloudAttributeProxyModel.Filters.baseClass = QgsPointCloudAttributeProxyModel
Filters = QgsPointCloudAttributeProxyModel  # dirty hack since SIP seems to introduce the flags in module
def _force_int(v): return v if isinstance(v, int) else int(v.value)


QgsPointCloudAttributeProxyModel.Filter.__bool__ = lambda flag: _force_int(flag)
QgsPointCloudAttributeProxyModel.Filter.__eq__ = lambda flag1, flag2: _force_int(flag1) == _force_int(flag2)
QgsPointCloudAttributeProxyModel.Filter.__and__ = lambda flag1, flag2: _force_int(flag1) & _force_int(flag2)
QgsPointCloudAttributeProxyModel.Filter.__or__ = lambda flag1, flag2: QgsPointCloudAttributeProxyModel.Filter(_force_int(flag1) | _force_int(flag2))
