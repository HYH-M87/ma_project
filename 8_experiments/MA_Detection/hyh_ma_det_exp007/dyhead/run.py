# 集成所有配置文件

_base_ = [
    'cfg/model.py',
    'cfg/dataset.py',
    'cfg/runtime.py',
    'cfg/schedule.py'
]

# log file and exoeriment info dir
work_dir = './9_logs/MA_Detection/hyh_ma_det_exp007/dyhead_112patch'
