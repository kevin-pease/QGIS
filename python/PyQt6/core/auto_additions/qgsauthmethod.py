# The following has been generated automatically from src/core/auth/qgsauthmethod.h
QgsAuthMethod.NetworkRequest = QgsAuthMethod.Expansion.NetworkRequest
QgsAuthMethod.NetworkReply = QgsAuthMethod.Expansion.NetworkReply
QgsAuthMethod.DataSourceUri = QgsAuthMethod.Expansion.DataSourceUri
QgsAuthMethod.GenericDataSourceUri = QgsAuthMethod.Expansion.GenericDataSourceUri
QgsAuthMethod.NetworkProxy = QgsAuthMethod.Expansion.NetworkProxy
QgsAuthMethod.All = QgsAuthMethod.Expansion.All
QgsAuthMethod.Expansions = lambda flags=0: QgsAuthMethod.Expansion(flags)
def _force_int(v): return v if isinstance(v, int) else int(v.value)


QgsAuthMethod.Expansion.__bool__ = lambda flag: _force_int(flag)
QgsAuthMethod.Expansion.__eq__ = lambda flag1, flag2: _force_int(flag1) == _force_int(flag2)
QgsAuthMethod.Expansion.__and__ = lambda flag1, flag2: _force_int(flag1) & _force_int(flag2)
QgsAuthMethod.Expansion.__or__ = lambda flag1, flag2: QgsAuthMethod.Expansion(_force_int(flag1) | _force_int(flag2))
