import pickle
import os
from sklearn import neighbors

_E8_A8_93_E7_B7_B4_E7_9B_AE_E6_A8_99 = None
_E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99 = None
_E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F_E6_B8_85_E5_96_AE = None
_E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F = None
AI_E6_A8_A1_E5_9E_8B = None


_E8_A8_93_E7_B7_B4_E7_9B_AE_E6_A8_99 = []
_E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99 = []
_E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F_E6_B8_85_E5_96_AE = ['1P', '2P']
for _E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F in _E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F_E6_B8_85_E5_96_AE:
    with open(os.path.join(os.path.dirname(__file__), 'data/特徵資料_' + str(_E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F) + '.pickle'), 'rb') as f:
        _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99 = pickle.load(f)
    with open(os.path.join(os.path.dirname(__file__), 'data/訓練目標_' + str(_E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F) + '.pickle'), 'rb') as f:
        _E8_A8_93_E7_B7_B4_E7_9B_AE_E6_A8_99 = pickle.load(f)
    AI_E6_A8_A1_E5_9E_8B = neighbors.KNeighborsClassifier(5, weights='uniform', algorithm='auto')
    AI_E6_A8_A1_E5_9E_8B.fit(_E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99, _E8_A8_93_E7_B7_B4_E7_9B_AE_E6_A8_99)
    # 儲存1P的模型
    os.makedirs(os.path.dirname(os.path.join(os.path.dirname(__file__), 'AI模型_' + str(_E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F) + '.pickle')), exist_ok=True)
    with open(os.path.join(os.path.dirname(__file__), 'AI模型_' + str(_E7_8E_A9_E5_AE_B6_E7_B7_A8_E8_99_9F) + '.pickle'), 'wb') as f:
        pickle.dump(AI_E6_A8_A1_E5_9E_8B, f)
