import pygame
import pickle
import os
import csv
import math

_E8_B2_9D_E9_AB_98_E8_8A_AC = None
_E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F = None
_E4_B8_8A_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 = None
_E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99 = None
_E4_B8_8B_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 = None
_E8_A8_93_E7_B7_B4_E7_9B_AE_E6_A8_99 = None
_E5_B7_A6_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 = None
_E5_8F_B3_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 = None
_E5_80_8B_E5_88_A5_E9_A3_9F_E7_89_A9 = None
_E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84X_E8_B7_9D_E9_9B_A2 = None
_E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84Y_E8_B7_9D_E9_9B_A2 = None

# 描述此函式...
def _E8_B2_9D_E9_AB_98_E8_8A_AC2():
    global _E8_B2_9D_E9_AB_98_E8_8A_AC, _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F, _E4_B8_8A_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99, _E4_B8_8B_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E8_A8_93_E7_B7_B4_E7_9B_AE_E6_A8_99, _E5_B7_A6_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E5_8F_B3_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E5_80_8B_E5_88_A5_E9_A3_9F_E7_89_A9, _E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84X_E8_B7_9D_E9_9B_A2, _E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84Y_E8_B7_9D_E9_9B_A2
    _E8_B2_9D_E9_AB_98_E8_8A_AC = 1
    if _E4_B8_8A_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 >= _E8_B2_9D_E9_AB_98_E8_8A_AC:
        _E8_B2_9D_E9_AB_98_E8_8A_AC = _E4_B8_8A_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8
        _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F = 1
    if _E4_B8_8B_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 >= _E8_B2_9D_E9_AB_98_E8_8A_AC:
        _E8_B2_9D_E9_AB_98_E8_8A_AC = _E4_B8_8B_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8
        _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F = 2
    if _E5_B7_A6_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 >= _E8_B2_9D_E9_AB_98_E8_8A_AC:
        _E8_B2_9D_E9_AB_98_E8_8A_AC = _E5_B7_A6_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8
        _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F = 3
    if _E5_8F_B3_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 >= _E8_B2_9D_E9_AB_98_E8_8A_AC:
        _E8_B2_9D_E9_AB_98_E8_8A_AC = _E5_8F_B3_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8
        _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F = 4

class MLPlayArgsSaver:
    def __init__(self):
        self.ai_name = None

        self.init_kwargs = None
        self.scene_info = None
        self.keyboard = None

mlplayArgs = MLPlayArgsSaver()

# 描述此函式...
def _E8_87_AA_E5_8B_95_E6_8E_A7_E5_88_B61P():
    global _E8_B2_9D_E9_AB_98_E8_8A_AC, _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F, _E4_B8_8A_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99, _E4_B8_8B_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E8_A8_93_E7_B7_B4_E7_9B_AE_E6_A8_99, _E5_B7_A6_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E5_8F_B3_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E5_80_8B_E5_88_A5_E9_A3_9F_E7_89_A9, _E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84X_E8_B7_9D_E9_9B_A2, _E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84Y_E8_B7_9D_E9_9B_A2
    if mlplayArgs.ai_name == '1P':
        if _E4_B8_8A_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 >= _E4_B8_8B_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 and _E4_B8_8A_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 >= _E5_8F_B3_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 and _E4_B8_8A_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 >= _E5_B7_A6_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8:
            _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F = 1
        elif _E4_B8_8B_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 >= _E4_B8_8A_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 and _E4_B8_8B_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 >= _E5_8F_B3_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 and _E4_B8_8B_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 >= _E5_B7_A6_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8:
            _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F = 1
        elif _E5_8F_B3_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 >= _E4_B8_8A_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 and _E5_8F_B3_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 >= _E4_B8_8B_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 and _E5_8F_B3_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 >= _E5_B7_A6_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8:
            _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F = 4
        elif _E5_B7_A6_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 >= _E4_B8_8A_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 and _E5_B7_A6_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 >= _E4_B8_8B_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 and _E5_B7_A6_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 >= _E5_8F_B3_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8:
            _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F = 3
    else:
        _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F = 0

# 描述此函式...
def _E8_87_AA_E5_8B_95_E6_8E_A7_E5_88_B62p():
    global _E8_B2_9D_E9_AB_98_E8_8A_AC, _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F, _E4_B8_8A_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99, _E4_B8_8B_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E8_A8_93_E7_B7_B4_E7_9B_AE_E6_A8_99, _E5_B7_A6_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E5_8F_B3_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E5_80_8B_E5_88_A5_E9_A3_9F_E7_89_A9, _E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84X_E8_B7_9D_E9_9B_A2, _E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84Y_E8_B7_9D_E9_9B_A2
    if mlplayArgs.ai_name == '2P':
        if _E4_B8_8A_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 >= _E4_B8_8B_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 and _E4_B8_8A_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 >= _E5_8F_B3_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 and _E4_B8_8A_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 >= _E5_B7_A6_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8:
            _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F = 1
        elif _E4_B8_8B_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 >= _E4_B8_8A_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 and _E4_B8_8B_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 >= _E5_8F_B3_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 and _E4_B8_8B_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 >= _E5_B7_A6_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8:
            _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F = 1
        elif _E5_8F_B3_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 >= _E4_B8_8A_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 and _E5_8F_B3_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 >= _E4_B8_8B_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 and _E5_8F_B3_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 >= _E5_B7_A6_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8:
            _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F = 4
        elif _E5_B7_A6_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 >= _E4_B8_8A_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 and _E5_B7_A6_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 >= _E4_B8_8B_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 and _E5_B7_A6_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 >= _E5_8F_B3_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8:
            _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F = 3
    else:
        _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F = 0

# 描述此函式...
def _E7_A7_BB_E5_8B_95_E6_8E_A7_E5_88_B6():
    global _E8_B2_9D_E9_AB_98_E8_8A_AC, _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F, _E4_B8_8A_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99, _E4_B8_8B_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E8_A8_93_E7_B7_B4_E7_9B_AE_E6_A8_99, _E5_B7_A6_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E5_8F_B3_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E5_80_8B_E5_88_A5_E9_A3_9F_E7_89_A9, _E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84X_E8_B7_9D_E9_9B_A2, _E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84Y_E8_B7_9D_E9_9B_A2
    if mlplayArgs.ai_name == '1P':
        _E8_B2_9D_E9_AB_98_E8_8A_AC2()
    elif mlplayArgs.ai_name == '2P':
        _E8_B2_9D_E9_AB_98_E8_8A_AC2()
    else:
        _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F = 0

# 只判斷自己和對手的相對位置和等級，不考慮其他食物
def _E6_94_B6_E9_9B_86_E8_B3_87_E6_96_99():
    global _E8_B2_9D_E9_AB_98_E8_8A_AC, _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F, _E4_B8_8A_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99, _E4_B8_8B_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E8_A8_93_E7_B7_B4_E7_9B_AE_E6_A8_99, _E5_B7_A6_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E5_8F_B3_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E5_80_8B_E5_88_A5_E9_A3_9F_E7_89_A9, _E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84X_E8_B7_9D_E9_9B_A2, _E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84Y_E8_B7_9D_E9_9B_A2
    if _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F > 0:
        _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99.append([(mlplayArgs.scene_info['self_x'] if mlplayArgs.scene_info is not None else None), (mlplayArgs.scene_info['self_y'] if mlplayArgs.scene_info is not None else None), (mlplayArgs.scene_info['opponent_x'] if mlplayArgs.scene_info is not None else None), (mlplayArgs.scene_info['opponent_y'] if mlplayArgs.scene_info is not None else None), (mlplayArgs.scene_info['self_lv'] if mlplayArgs.scene_info is not None else None) - (mlplayArgs.scene_info['opponent_lv'] if mlplayArgs.scene_info is not None else None), _E4_B8_8A_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E4_B8_8B_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E5_B7_A6_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E5_8F_B3_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8])
        _E8_A8_93_E7_B7_B4_E7_9B_AE_E6_A8_99.append([_E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F])

# 描述此函式...
def _E5_84_B2_E5_AD_98_E8_B3_87_E6_96_99():
    global _E8_B2_9D_E9_AB_98_E8_8A_AC, _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F, _E4_B8_8A_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99, _E4_B8_8B_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E8_A8_93_E7_B7_B4_E7_9B_AE_E6_A8_99, _E5_B7_A6_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E5_8F_B3_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E5_80_8B_E5_88_A5_E9_A3_9F_E7_89_A9, _E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84X_E8_B7_9D_E9_9B_A2, _E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84Y_E8_B7_9D_E9_9B_A2
    os.makedirs(os.path.dirname(os.path.join(os.path.dirname(__file__), 'data/特徵資料_' + str(mlplayArgs.ai_name) + '.pickle')), exist_ok=True)
    with open(os.path.join(os.path.dirname(__file__), 'data/特徵資料_' + str(mlplayArgs.ai_name) + '.pickle'), 'wb') as f:
        pickle.dump(_E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99, f)
    os.makedirs(os.path.dirname(os.path.join(os.path.dirname(__file__), 'data/訓練目標_' + str(mlplayArgs.ai_name) + '.pickle')), exist_ok=True)
    with open(os.path.join(os.path.dirname(__file__), 'data/訓練目標_' + str(mlplayArgs.ai_name) + '.pickle'), 'wb') as f:
        pickle.dump(_E8_A8_93_E7_B7_B4_E7_9B_AE_E6_A8_99, f)
    os.makedirs(os.path.dirname(os.path.join(os.path.dirname(__file__), 'data/特徵資料_' + str(mlplayArgs.ai_name) + '.csv')), exist_ok=True)
    with open(os.path.join(os.path.dirname(__file__), 'data/特徵資料_' + str(mlplayArgs.ai_name) + '.csv'), 'w', newline='', encoding='utf-8') as f:
        csv.writer(f).writerows(_E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99)
    os.makedirs(os.path.dirname(os.path.join(os.path.dirname(__file__), 'data/訓練目標_' + str(mlplayArgs.ai_name) + '.csv')), exist_ok=True)
    with open(os.path.join(os.path.dirname(__file__), 'data/訓練目標_' + str(mlplayArgs.ai_name) + '.csv'), 'w', newline='', encoding='utf-8') as f:
        csv.writer(f).writerows(_E8_A8_93_E7_B7_B4_E7_9B_AE_E6_A8_99)

# 描述此函式...
def _E8_A8_88_E7_AE_97_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8():
    global _E8_B2_9D_E9_AB_98_E8_8A_AC, _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F, _E4_B8_8A_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99, _E4_B8_8B_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E8_A8_93_E7_B7_B4_E7_9B_AE_E6_A8_99, _E5_B7_A6_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E5_8F_B3_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E5_80_8B_E5_88_A5_E9_A3_9F_E7_89_A9, _E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84X_E8_B7_9D_E9_9B_A2, _E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84Y_E8_B7_9D_E9_9B_A2
    _E4_B8_8A_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 = 0
    _E4_B8_8B_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 = 0
    _E5_B7_A6_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 = 0
    _E5_8F_B3_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 = 0
    for _E5_80_8B_E5_88_A5_E9_A3_9F_E7_89_A9 in (mlplayArgs.scene_info['foods'] if mlplayArgs.scene_info is not None else None):
        _E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84X_E8_B7_9D_E9_9B_A2 = _E5_80_8B_E5_88_A5_E9_A3_9F_E7_89_A9['x'] - (mlplayArgs.scene_info['self_x'] if mlplayArgs.scene_info is not None else None)
        _E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84Y_E8_B7_9D_E9_9B_A2 = _E5_80_8B_E5_88_A5_E9_A3_9F_E7_89_A9['y'] - (mlplayArgs.scene_info['self_y'] if mlplayArgs.scene_info is not None else None)
        if math.fabs(_E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84X_E8_B7_9D_E9_9B_A2) < 20 and _E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84Y_E8_B7_9D_E9_9B_A2 < 0:
            _E4_B8_8A_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 = _E4_B8_8A_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 + _E5_80_8B_E5_88_A5_E9_A3_9F_E7_89_A9['score']
        elif math.fabs(_E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84X_E8_B7_9D_E9_9B_A2) < 20 and _E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84Y_E8_B7_9D_E9_9B_A2 > 0:
            _E4_B8_8B_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 = _E4_B8_8B_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 + _E5_80_8B_E5_88_A5_E9_A3_9F_E7_89_A9['score']
        elif _E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84X_E8_B7_9D_E9_9B_A2 < 0 and math.fabs(_E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84Y_E8_B7_9D_E9_9B_A2) < 30:
            _E5_B7_A6_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 = _E5_B7_A6_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 + _E5_80_8B_E5_88_A5_E9_A3_9F_E7_89_A9['score']
        elif _E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84X_E8_B7_9D_E9_9B_A2 > 0 and math.fabs(_E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84Y_E8_B7_9D_E9_9B_A2) < 30:
            _E5_8F_B3_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 = _E5_8F_B3_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 + _E5_80_8B_E5_88_A5_E9_A3_9F_E7_89_A9['score']


if (pygame.K_w in mlplayArgs.keyboard if mlplayArgs.keyboard is not None else False):
    _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F = 1
elif (pygame.K_s in mlplayArgs.keyboard if mlplayArgs.keyboard is not None else False):
    _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F = 2
elif (pygame.K_a in mlplayArgs.keyboard if mlplayArgs.keyboard is not None else False):
    _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F = 3
elif (pygame.K_d in mlplayArgs.keyboard if mlplayArgs.keyboard is not None else False):
    _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F = 4
else:
    _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F = 0

class MLPlay:
    def __init__(self, ai_name, *args, **kwargs):
        global _E8_B2_9D_E9_AB_98_E8_8A_AC, _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F, _E4_B8_8A_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99, _E4_B8_8B_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E8_A8_93_E7_B7_B4_E7_9B_AE_E6_A8_99, _E5_B7_A6_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E5_8F_B3_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E5_80_8B_E5_88_A5_E9_A3_9F_E7_89_A9, _E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84X_E8_B7_9D_E9_9B_A2, _E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84Y_E8_B7_9D_E9_9B_A2
        mlplayArgs.ai_name = ai_name
        mlplayArgs.init_kwargs = kwargs
        _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F = 0
        _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99 = []
        _E8_A8_93_E7_B7_B4_E7_9B_AE_E6_A8_99 = []
        _E4_B8_8A_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 = 0
        _E4_B8_8B_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 = 0
        _E5_B7_A6_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 = 0
        _E5_8F_B3_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 = 0
    def update(self, scene_info, keyboard=[], *args, **kwargs):
        global _E8_B2_9D_E9_AB_98_E8_8A_AC, _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F, _E4_B8_8A_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99, _E4_B8_8B_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E8_A8_93_E7_B7_B4_E7_9B_AE_E6_A8_99, _E5_B7_A6_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E5_8F_B3_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E5_80_8B_E5_88_A5_E9_A3_9F_E7_89_A9, _E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84X_E8_B7_9D_E9_9B_A2, _E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84Y_E8_B7_9D_E9_9B_A2
        mlplayArgs.scene_info = scene_info
        mlplayArgs.keyboard = keyboard
        _E8_A8_88_E7_AE_97_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8()
        _E6_94_B6_E9_9B_86_E8_B3_87_E6_96_99()
        _E7_A7_BB_E5_8B_95_E6_8E_A7_E5_88_B6()
        if _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F == 1:
            return ['UP']
        elif _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F == 2:
            return ['DOWN']
        elif _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F == 3:
            return ['LEFT']
        elif _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F == 4:
            return ['RIGHT']
        else:
            return ['NONE']
        _E5_84_B2_E5_AD_98_E8_B3_87_E6_96_99()
    def reset(self):
        global _E8_B2_9D_E9_AB_98_E8_8A_AC, _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F, _E4_B8_8A_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99, _E4_B8_8B_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E8_A8_93_E7_B7_B4_E7_9B_AE_E6_A8_99, _E5_B7_A6_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E5_8F_B3_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E5_80_8B_E5_88_A5_E9_A3_9F_E7_89_A9, _E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84X_E8_B7_9D_E9_9B_A2, _E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84Y_E8_B7_9D_E9_9B_A2
        pass

if (pygame.K_UP in mlplayArgs.keyboard if mlplayArgs.keyboard is not None else False):
    _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F = 1
elif (pygame.K_DOWN in mlplayArgs.keyboard if mlplayArgs.keyboard is not None else False):
    _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F = 2
elif (pygame.K_LEFT in mlplayArgs.keyboard if mlplayArgs.keyboard is not None else False):
    _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F = 3
elif (pygame.K_RIGHT in mlplayArgs.keyboard if mlplayArgs.keyboard is not None else False):
    _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F = 4
else:
    _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F = 0

_E8_87_AA_E5_8B_95_E6_8E_A7_E5_88_B61P()

_E8_87_AA_E5_8B_95_E6_8E_A7_E5_88_B62p()
