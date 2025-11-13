import pickle
import os
import math

_E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F = None
_E4_B8_8A_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 = None
_E5_B0_8D_E6_89_8Bx_E8_B7_9D_E9_9B_A2 = None
_E4_B8_8B_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 = None
_E5_B0_8D_E6_89_8By_E8_B7_9D_E9_9B_A2 = None
AI_E6_A8_A1_E5_9E_8B = None
_E5_B7_A6_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 = None
_E7_AD_89_E7_B4_9A_E5_B7_AE_E8_B7_9D = None
_E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99_E6_B8_85_E5_96_AE = None
_E5_8F_B3_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 = None
_E5_80_8B_E5_88_A5_E9_A3_9F_E7_89_A9 = None
_E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84X_E8_B7_9D_E9_9B_A2 = None
_E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84Y_E8_B7_9D_E9_9B_A2 = None

class MLPlayArgsSaver:
    def __init__(self):
        self.ai_name = None

        self.init_kwargs = None
        self.scene_info = None
        self.keyboard = None

mlplayArgs = MLPlayArgsSaver()

# 描述此函式...
def _E8_A8_88_E7_AE_97_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8():
    global _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F, _E4_B8_8A_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E5_B0_8D_E6_89_8Bx_E8_B7_9D_E9_9B_A2, _E4_B8_8B_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E5_B0_8D_E6_89_8By_E8_B7_9D_E9_9B_A2, AI_E6_A8_A1_E5_9E_8B, _E5_B7_A6_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E7_AD_89_E7_B4_9A_E5_B7_AE_E8_B7_9D, _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99_E6_B8_85_E5_96_AE, _E5_8F_B3_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E5_80_8B_E5_88_A5_E9_A3_9F_E7_89_A9, _E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84X_E8_B7_9D_E9_9B_A2, _E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84Y_E8_B7_9D_E9_9B_A2
    _E4_B8_8A_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 = 0
    _E4_B8_8B_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 = 0
    _E5_B7_A6_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 = 0
    _E5_8F_B3_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 = 0
    for _E5_80_8B_E5_88_A5_E9_A3_9F_E7_89_A9 in (mlplayArgs.scene_info['foods'] if mlplayArgs.scene_info is not None else None):
        _E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84X_E8_B7_9D_E9_9B_A2 = _E5_80_8B_E5_88_A5_E9_A3_9F_E7_89_A9['x'] - (mlplayArgs.scene_info['self_x'] if mlplayArgs.scene_info is not None else None)
        _E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84Y_E8_B7_9D_E9_9B_A2 = _E5_80_8B_E5_88_A5_E9_A3_9F_E7_89_A9['y'] - (mlplayArgs.scene_info['self_y'] if mlplayArgs.scene_info is not None else None)
        if math.fabs(_E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84X_E8_B7_9D_E9_9B_A2) < 40 and _E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84Y_E8_B7_9D_E9_9B_A2 < 0:
            _E4_B8_8A_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 = _E4_B8_8A_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 + _E5_80_8B_E5_88_A5_E9_A3_9F_E7_89_A9['score']
        elif math.fabs(_E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84X_E8_B7_9D_E9_9B_A2) < 40 and _E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84Y_E8_B7_9D_E9_9B_A2 > 0:
            _E4_B8_8B_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 = _E4_B8_8B_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 + _E5_80_8B_E5_88_A5_E9_A3_9F_E7_89_A9['score']
        elif _E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84X_E8_B7_9D_E9_9B_A2 < 0 and math.fabs(_E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84Y_E8_B7_9D_E9_9B_A2) < 50:
            _E5_B7_A6_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 = _E5_B7_A6_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 + _E5_80_8B_E5_88_A5_E9_A3_9F_E7_89_A9['score']
        elif _E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84X_E8_B7_9D_E9_9B_A2 > 0 and math.fabs(_E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84Y_E8_B7_9D_E9_9B_A2) < 50:
            _E5_8F_B3_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 = _E5_8F_B3_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 + _E5_80_8B_E5_88_A5_E9_A3_9F_E7_89_A9['score']

# 描述此函式...
def _E8_A8_88_E7_AE_97_E9_82_8A_E7_95_8C_E5_88_86_E6_95_B8():
    global _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F, _E4_B8_8A_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E5_B0_8D_E6_89_8Bx_E8_B7_9D_E9_9B_A2, _E4_B8_8B_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E5_B0_8D_E6_89_8By_E8_B7_9D_E9_9B_A2, AI_E6_A8_A1_E5_9E_8B, _E5_B7_A6_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E7_AD_89_E7_B4_9A_E5_B7_AE_E8_B7_9D, _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99_E6_B8_85_E5_96_AE, _E5_8F_B3_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E5_80_8B_E5_88_A5_E9_A3_9F_E7_89_A9, _E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84X_E8_B7_9D_E9_9B_A2, _E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84Y_E8_B7_9D_E9_9B_A2
    _E4_B8_8A_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 = _E4_B8_8A_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 - 0 / ((mlplayArgs.scene_info['self_y'] if mlplayArgs.scene_info is not None else None) - (mlplayArgs.scene_info['env']['top'] if mlplayArgs.scene_info is not None else None))
    _E4_B8_8B_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 = _E4_B8_8B_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 - 0 / ((mlplayArgs.scene_info['env']['bottom'] if mlplayArgs.scene_info is not None else None) - (mlplayArgs.scene_info['self_y'] if mlplayArgs.scene_info is not None else None))
    _E5_B7_A6_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 = _E5_B7_A6_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 - 0 / ((mlplayArgs.scene_info['self_x'] if mlplayArgs.scene_info is not None else None) - (mlplayArgs.scene_info['env']['left'] if mlplayArgs.scene_info is not None else None))
    _E5_8F_B3_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 = _E5_8F_B3_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 - 0 / ((mlplayArgs.scene_info['env']['right'] if mlplayArgs.scene_info is not None else None) - (mlplayArgs.scene_info['self_x'] if mlplayArgs.scene_info is not None else None))

# 描述此函式...
def _E8_A8_88_E7_AE_97_E5_B0_8D_E6_89_8B_E5_88_86_E6_95_B8():
    global _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F, _E4_B8_8A_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E5_B0_8D_E6_89_8Bx_E8_B7_9D_E9_9B_A2, _E4_B8_8B_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E5_B0_8D_E6_89_8By_E8_B7_9D_E9_9B_A2, AI_E6_A8_A1_E5_9E_8B, _E5_B7_A6_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E7_AD_89_E7_B4_9A_E5_B7_AE_E8_B7_9D, _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99_E6_B8_85_E5_96_AE, _E5_8F_B3_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E5_80_8B_E5_88_A5_E9_A3_9F_E7_89_A9, _E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84X_E8_B7_9D_E9_9B_A2, _E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84Y_E8_B7_9D_E9_9B_A2
    _E5_B0_8D_E6_89_8Bx_E8_B7_9D_E9_9B_A2 = (mlplayArgs.scene_info['opponent_x'] if mlplayArgs.scene_info is not None else None) - (mlplayArgs.scene_info['self_x'] if mlplayArgs.scene_info is not None else None)
    _E5_B0_8D_E6_89_8By_E8_B7_9D_E9_9B_A2 = (mlplayArgs.scene_info['opponent_y'] if mlplayArgs.scene_info is not None else None) - (mlplayArgs.scene_info['self_y'] if mlplayArgs.scene_info is not None else None)
    _E7_AD_89_E7_B4_9A_E5_B7_AE_E8_B7_9D = (mlplayArgs.scene_info['self_lv'] if mlplayArgs.scene_info is not None else None) - (mlplayArgs.scene_info['opponent_lv'] if mlplayArgs.scene_info is not None else None)
    if math.fabs(_E5_B0_8D_E6_89_8By_E8_B7_9D_E9_9B_A2) < 30 and _E5_B0_8D_E6_89_8By_E8_B7_9D_E9_9B_A2 < 0:
        _E4_B8_8A_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 = _E7_AD_89_E7_B4_9A_E5_B7_AE_E8_B7_9D * 100
    elif math.fabs(_E5_B0_8D_E6_89_8Bx_E8_B7_9D_E9_9B_A2) < 30 and _E5_B0_8D_E6_89_8Bx_E8_B7_9D_E9_9B_A2 > 0:
        _E4_B8_8B_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 = _E7_AD_89_E7_B4_9A_E5_B7_AE_E8_B7_9D * 100
    elif _E5_B0_8D_E6_89_8By_E8_B7_9D_E9_9B_A2 < 0 and math.fabs(_E5_B0_8D_E6_89_8By_E8_B7_9D_E9_9B_A2) < 40:
        _E5_B7_A6_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 = _E7_AD_89_E7_B4_9A_E5_B7_AE_E8_B7_9D * 100
    elif _E5_B0_8D_E6_89_8Bx_E8_B7_9D_E9_9B_A2 > 0 and math.fabs(_E5_B0_8D_E6_89_8Bx_E8_B7_9D_E9_9B_A2) < 40:
        _E5_8F_B3_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8 = _E7_AD_89_E7_B4_9A_E5_B7_AE_E8_B7_9D * 100


class MLPlay:
    def __init__(self, ai_name, *args, **kwargs):
        global _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F, _E4_B8_8A_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E5_B0_8D_E6_89_8Bx_E8_B7_9D_E9_9B_A2, _E4_B8_8B_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E5_B0_8D_E6_89_8By_E8_B7_9D_E9_9B_A2, AI_E6_A8_A1_E5_9E_8B, _E5_B7_A6_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E7_AD_89_E7_B4_9A_E5_B7_AE_E8_B7_9D, _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99_E6_B8_85_E5_96_AE, _E5_8F_B3_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E5_80_8B_E5_88_A5_E9_A3_9F_E7_89_A9, _E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84X_E8_B7_9D_E9_9B_A2, _E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84Y_E8_B7_9D_E9_9B_A2
        mlplayArgs.ai_name = ai_name
        mlplayArgs.init_kwargs = kwargs
        _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F = 0
        with open(os.path.join(os.path.dirname(__file__), 'AI模型_' + str(mlplayArgs.ai_name) + '.pickle'), 'rb') as f:
            AI_E6_A8_A1_E5_9E_8B = pickle.load(f)
    def update(self, scene_info, keyboard=[], *args, **kwargs):
        global _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F, _E4_B8_8A_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E5_B0_8D_E6_89_8Bx_E8_B7_9D_E9_9B_A2, _E4_B8_8B_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E5_B0_8D_E6_89_8By_E8_B7_9D_E9_9B_A2, AI_E6_A8_A1_E5_9E_8B, _E5_B7_A6_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E7_AD_89_E7_B4_9A_E5_B7_AE_E8_B7_9D, _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99_E6_B8_85_E5_96_AE, _E5_8F_B3_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E5_80_8B_E5_88_A5_E9_A3_9F_E7_89_A9, _E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84X_E8_B7_9D_E9_9B_A2, _E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84Y_E8_B7_9D_E9_9B_A2
        mlplayArgs.scene_info = scene_info
        mlplayArgs.keyboard = keyboard
        _E8_A8_88_E7_AE_97_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8()
        _E8_A8_88_E7_AE_97_E9_82_8A_E7_95_8C_E5_88_86_E6_95_B8()
        _E8_A8_88_E7_AE_97_E5_B0_8D_E6_89_8B_E5_88_86_E6_95_B8()
        _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99_E6_B8_85_E5_96_AE = [[_E4_B8_8A_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E4_B8_8B_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E5_B7_A6_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E5_8F_B3_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8]]
        _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F = AI_E6_A8_A1_E5_9E_8B.predict(_E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99_E6_B8_85_E5_96_AE).tolist()[0]
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
    def reset(self):
        global _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91_E7_B7_A8_E8_99_9F, _E4_B8_8A_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E5_B0_8D_E6_89_8Bx_E8_B7_9D_E9_9B_A2, _E4_B8_8B_E6_96_B9_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E5_B0_8D_E6_89_8By_E8_B7_9D_E9_9B_A2, AI_E6_A8_A1_E5_9E_8B, _E5_B7_A6_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E7_AD_89_E7_B4_9A_E5_B7_AE_E8_B7_9D, _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99_E6_B8_85_E5_96_AE, _E5_8F_B3_E9_82_8A_E9_A3_9F_E7_89_A9_E5_88_86_E6_95_B8, _E5_80_8B_E5_88_A5_E9_A3_9F_E7_89_A9, _E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84X_E8_B7_9D_E9_9B_A2, _E9_A3_9F_E7_89_A9_E8_88_87_E8_A7_92_E8_89_B2_E7_9A_84Y_E8_B7_9D_E9_9B_A2
        pass
