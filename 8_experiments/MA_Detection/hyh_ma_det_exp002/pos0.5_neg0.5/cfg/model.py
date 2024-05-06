


_base_ = [
    './_base_/retinanet_r50_fpn.py',
    './_base_/retinanet_tta.py'
]



# log file and exoeriment info dir
work_dir = './9_logs/MA_Detection/hyh_ma_det_exp002/pos0.5_neg0.5'





conv_cfg = dict(type='ConvWS')  # weight standrized
norm_cfg = dict(type='GN', num_groups=32, requires_grad=True)  # group norm
mean=[27.89055289996231,58.857601182875676,124.78614245730006]
std=[30.259294194153544,109.07029260568576,334.6284058025839]



# model settings
model = dict(
    type='FSAF',
    data_preprocessor=dict(
        type='DetDataPreprocessor',
        mean=mean,
        std=std,
        bgr_to_rgb=True,
        pad_size_divisor=32),
     backbone=dict(
        type='ResNeXt',
        depth=50,
        groups=32,
        base_width=4,
        num_stages=4,
        out_indices=(0, 1, 2, 3),
        frozen_stages=1,
        style='pytorch',
        conv_cfg=conv_cfg,
        norm_cfg=norm_cfg,
        init_cfg=dict(
            type='Pretrained',
            checkpoint='open-mmlab://jhu/resnext50_32x4d_gn_ws')
    ),
    bbox_head=dict(
        type='FSAFHead',
        num_classes=1,
        in_channels=256,
        stacked_convs=4,
        feat_channels=256,
        reg_decoded_bbox=True,
        # Only anchor-free branch is implemented. The anchor generator only
        #  generates 1 anchor at each feature point, as a substitute of the
        #  grid of features.
        anchor_generator=dict(
            type='AnchorGenerator',
            octave_base_scale=1,
            scales_per_octave=1,
            ratios=[1.0],
            strides=[8, 16, 32, 64, 128]),
        bbox_coder=dict(_delete_=True, type='TBLRBBoxCoder', normalizer=4.0),
        loss_cls=dict(
            type='FocalLoss',
            use_sigmoid=True,
            gamma=2.0,
            alpha=0.25,

            loss_weight=1.0,
            reduction='none'),
        loss_bbox=dict(
            _delete_=True,
            type='IoULoss',
            eps=1e-6,
            loss_weight=1.0,
            reduction='none')),
    # training and testing settings
    train_cfg=dict(
        assigner=dict(
            _delete_=True,
            type='CenterRegionAssigner',
            # pos_scale=0.2,
            pos_scale=0.5,
            neg_scale=0.5,
            min_pos_iof=0.01),
        allowed_border=-1,
        pos_weight=-1,
        debug=False),
    test_cfg=dict(
        nms_pre=1000,
        min_bbox_size=0,
        score_thr=0.05,
        nms=dict(type='nms', iou_threshold=0.5),
        max_per_img=100))