import requests
from threading import Timer

CompactionInputSize_means=[]
compactionQueueLengths=[]
CompactionInputFileCount_num_opss=[]

def metricTask():
    response = requests.get(
        'http://10.26.32.89:18020/jmx'
    )
    compactedOutputBytes = 0;
    compactedInputBytes = 0;
    compactedCellsSize = 0;
    CompactionInputFileCount_min = 0
    CompactionInputFileCount_max = 0
    CompactionInputFileCount_mean = 0
    CompactionTime_num_ops = 0
    CompactionTime_min = 0
    CompactionTime_max = 0
    CompactionTime_mean = 0
    CompactionInputSize_mean = 0
    NamespaceDefaultTablePerfTestMetricCompactedInputBytes = 0
    compactionQueueLength = 0
    CompactionInputFileCount_num_ops = 0

    metrics = response.json().get("beans");
    for ele in metrics:
        if ele.get('name') == 'Hadoop:service=HBase,name=RegionServer,sub=Server':
            compactedOutputBytes = ele.get('compactedOutputBytes')
            compactedInputBytes = ele.get('compactedInputBytes')
            compactedCellsSize = ele.get('compactedCellsSize')
            CompactionInputFileCount_min = ele.get('CompactionInputFileCount_min')
            CompactionInputFileCount_max = ele.get('CompactionInputFileCount_max')
            CompactionInputFileCount_mean = ele.get('CompactionInputFileCount_mean')
            CompactionTime_num_ops = ele.get('CompactionTime_num_ops')
            CompactionTime_min = ele.get('CompactionTime_min')
            CompactionTime_max = ele.get('CompactionTime_max')
            CompactionTime_mean = ele.get('CompactionTime_mean')
            CompactionInputSize_mean = ele.get('CompactionInputSize_mean')
            compactionQueueLength = ele.get('compactionQueueLength')
            CompactionInputFileCount_num_ops = ele.get('CompactionInputFileCount_num_ops')
        elif ele.get('name') == 'Hadoop:service=HBase,name=RegionServer,sub=Tables':
            NamespaceDefaultTablePerfTestMetricCompactedInputBytes = ele.get(
                'Namespace_default_table_perf-test_metric_compactedInputBytes')

    print('regionserver-compactedOutputBytes:', compactedOutputBytes)
    print('regionserver-compactedInputBytes:', compactedInputBytes)
    # print('regionserver-compactedCellsSize:', compactedCellsSize)
    # print('regionserver-CompactionInputFileCount_min:', CompactionInputFileCount_min)
    # print('regionserver-CompactionInputFileCount_max:', CompactionInputFileCount_max)
    print('regionserver-CompactionInputFileCount_mean:', CompactionInputFileCount_mean)
    # print('regionserver-CompactionTime_num_ops:', CompactionTime_num_ops)
    # print('regionserver-CompactionTime_min:', CompactionTime_min)
    # print('regionserver-CompactionTime_max:', CompactionTime_max)
    print('regionserver-CompactionTime_mean:', CompactionTime_mean)
    # print('default_table_perf-test_metric_compactedInputBytes', NamespaceDefaultTablePerfTestMetricCompactedInputBytes)
    print('CompactionInputSize_mean:', CompactionInputSize_mean)
    CompactionInputSize_means.append(CompactionInputSize_mean)

    print('compactionQueueLength:', compactionQueueLength)
    compactionQueueLengths.append(compactionQueueLength)

    print('CompactionInputFileCount_num_ops:', CompactionInputFileCount_num_ops)
    CompactionInputFileCount_num_opss.append(CompactionInputFileCount_num_ops)


def loop_func(func, second):
    while True:
        timer = Timer(second, func)
        timer.start()
        timer.join()


loop_func(metricTask, 10)
