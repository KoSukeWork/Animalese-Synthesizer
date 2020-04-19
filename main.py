#!/usr/bin/env python3
import json
import random
import re
import sys
from typing import Dict, List, Tuple

import sox
from pypinyin import Style, lazy_pinyin


def load_voice_features() -> Dict:
    """加载声音特征参数"""
    with open('voice_features.json', 'r') as f:
        config = json.load(f)
        return config


def clean_text(text):
    """去掉文本的空白字符、标点符号"""
    return re.sub(r'[？ 、；！，。“”?.~…,$\r\n《》——]|(<.*>)', '', text.strip())


def hanzi_to_pinyin(hanzi: str) -> List[Tuple[str, str]]:
    """汉字转拼音音节（声韵母元组）"""
    cleaned_hanzi = clean_text(hanzi)
    initials = lazy_pinyin(cleaned_hanzi, style=Style.INITIALS,
                           errors='ignore', strict=True)
    finals = lazy_pinyin(cleaned_hanzi, style=Style.FINALS,
                         errors='ignore', strict=True)
    syllables = list(zip(initials, finals))
    return syllables


def phonemes_to_audio(syllables: Tuple[str, str], voice_features: Dict, name: str = 'tom_nook') -> None:
    """音素转音频"""
    phonemes = []
    for initial, final in syllables:
        if initial:
            phonemes.append(initial)
        if final:
            phonemes.append(final)

    phoneme_sounds = [
        f'pinyin_phonemes/{phoneme}.wav' for phoneme in phonemes]

    synthesized = sox.Combiner()
    vf = voice_features[name]
    pitch_shift_random_range, tempo = vf['pitch_shift_random_range'], vf['tempo']
    synthesized.pitch(random.uniform(*pitch_shift_random_range))
    synthesized.tempo(tempo)
    synthesized.build(phoneme_sounds, 'synthesized.wav', 'concatenate')


if __name__ == "__main__":
    if len(sys.argv) > 1:
        vfs = load_voice_features()
        syllables = hanzi_to_pinyin(sys.argv[1])
        print(syllables)
        phonemes_to_audio(syllables, vfs)
