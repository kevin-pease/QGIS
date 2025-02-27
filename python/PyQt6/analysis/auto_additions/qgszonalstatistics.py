# The following has been generated automatically from src/analysis/vector/qgszonalstatistics.h
QgsZonalStatistics.Count = QgsZonalStatistics.Statistic.Count
QgsZonalStatistics.Sum = QgsZonalStatistics.Statistic.Sum
QgsZonalStatistics.Mean = QgsZonalStatistics.Statistic.Mean
QgsZonalStatistics.Median = QgsZonalStatistics.Statistic.Median
QgsZonalStatistics.StDev = QgsZonalStatistics.Statistic.StDev
QgsZonalStatistics.Min = QgsZonalStatistics.Statistic.Min
QgsZonalStatistics.Max = QgsZonalStatistics.Statistic.Max
QgsZonalStatistics.Range = QgsZonalStatistics.Statistic.Range
QgsZonalStatistics.Minority = QgsZonalStatistics.Statistic.Minority
QgsZonalStatistics.Majority = QgsZonalStatistics.Statistic.Majority
QgsZonalStatistics.Variety = QgsZonalStatistics.Statistic.Variety
QgsZonalStatistics.Variance = QgsZonalStatistics.Statistic.Variance
QgsZonalStatistics.All = QgsZonalStatistics.Statistic.All
QgsZonalStatistics.Statistics = lambda flags=0: QgsZonalStatistics.Statistic(flags)
QgsZonalStatistics.Success = QgsZonalStatistics.Result.Success
QgsZonalStatistics.LayerTypeWrong = QgsZonalStatistics.Result.LayerTypeWrong
QgsZonalStatistics.LayerInvalid = QgsZonalStatistics.Result.LayerInvalid
QgsZonalStatistics.RasterInvalid = QgsZonalStatistics.Result.RasterInvalid
QgsZonalStatistics.RasterBandInvalid = QgsZonalStatistics.Result.RasterBandInvalid
QgsZonalStatistics.FailedToCreateField = QgsZonalStatistics.Result.FailedToCreateField
QgsZonalStatistics.Canceled = QgsZonalStatistics.Result.Canceled
def _force_int(v): return v if isinstance(v, int) else int(v.value)


QgsZonalStatistics.Statistic.__bool__ = lambda flag: _force_int(flag)
QgsZonalStatistics.Statistic.__eq__ = lambda flag1, flag2: _force_int(flag1) == _force_int(flag2)
QgsZonalStatistics.Statistic.__and__ = lambda flag1, flag2: _force_int(flag1) & _force_int(flag2)
QgsZonalStatistics.Statistic.__or__ = lambda flag1, flag2: QgsZonalStatistics.Statistic(_force_int(flag1) | _force_int(flag2))
