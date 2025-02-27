# The following has been generated automatically from src/core/qgsstatisticalsummary.h
QgsStatisticalSummary.Count = QgsStatisticalSummary.Statistic.Count
QgsStatisticalSummary.CountMissing = QgsStatisticalSummary.Statistic.CountMissing
QgsStatisticalSummary.Sum = QgsStatisticalSummary.Statistic.Sum
QgsStatisticalSummary.Mean = QgsStatisticalSummary.Statistic.Mean
QgsStatisticalSummary.Median = QgsStatisticalSummary.Statistic.Median
QgsStatisticalSummary.StDev = QgsStatisticalSummary.Statistic.StDev
QgsStatisticalSummary.StDevSample = QgsStatisticalSummary.Statistic.StDevSample
QgsStatisticalSummary.Min = QgsStatisticalSummary.Statistic.Min
QgsStatisticalSummary.Max = QgsStatisticalSummary.Statistic.Max
QgsStatisticalSummary.Range = QgsStatisticalSummary.Statistic.Range
QgsStatisticalSummary.Minority = QgsStatisticalSummary.Statistic.Minority
QgsStatisticalSummary.Majority = QgsStatisticalSummary.Statistic.Majority
QgsStatisticalSummary.Variety = QgsStatisticalSummary.Statistic.Variety
QgsStatisticalSummary.FirstQuartile = QgsStatisticalSummary.Statistic.FirstQuartile
QgsStatisticalSummary.ThirdQuartile = QgsStatisticalSummary.Statistic.ThirdQuartile
QgsStatisticalSummary.InterQuartileRange = QgsStatisticalSummary.Statistic.InterQuartileRange
QgsStatisticalSummary.First = QgsStatisticalSummary.Statistic.First
QgsStatisticalSummary.Last = QgsStatisticalSummary.Statistic.Last
QgsStatisticalSummary.All = QgsStatisticalSummary.Statistic.All
QgsStatisticalSummary.Statistics = lambda flags=0: QgsStatisticalSummary.Statistic(flags)
def _force_int(v): return v if isinstance(v, int) else int(v.value)


QgsStatisticalSummary.Statistic.__bool__ = lambda flag: _force_int(flag)
QgsStatisticalSummary.Statistic.__eq__ = lambda flag1, flag2: _force_int(flag1) == _force_int(flag2)
QgsStatisticalSummary.Statistic.__and__ = lambda flag1, flag2: _force_int(flag1) & _force_int(flag2)
QgsStatisticalSummary.Statistic.__or__ = lambda flag1, flag2: QgsStatisticalSummary.Statistic(_force_int(flag1) | _force_int(flag2))
