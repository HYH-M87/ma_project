# 集成所有配置文件

_base_ = [
    'cfg/model.py',
    'cfg/dataset.py',
    'cfg/runtime.py',
    'cfg/schedule.py'
]

# log file and exoeriment info dir
work_dir = './logs/MA_Detection/hyh_ma_det_exp006/res50_cbam_dcn/finetune'
