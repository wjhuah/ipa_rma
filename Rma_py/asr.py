pip install pympi-ling pydub
!apt-get install ffmpeg

import pympi
from pydub import AudioSegment
import os

eaf_path = '/Users/whua/Desktop/uic_暑校/hill/Yonghe Qiang/YH-999/YH-999.eaf'
wav_path = '/Users/whua/Desktop/uic_暑校/hill/Yonghe Qiang/YH-999/YH-999.wav'
output_dir = '/Users/whua/Desktop/uic_暑校/asr/preprocessed/YH-999'

os.makedirs(f'{output_dir}/wavs', exist_ok=True)

text, wav_scp, utt2spk = [], [], []

eaf = pympi.Elan.Eaf(eaf_path)
audio = AudioSegment.from_wav(wav_path)

for tier in eaf.get_tier_names():
    annotations = eaf.get_annotation_data_for_tier(tier)
    for i, (start_ms, end_ms, ipa) in enumerate(annotations):
        ipa = ipa.strip()
        if not ipa:
            continue
        start = int(start_ms)
        end = int(end_ms)

        utt_id = f'{tier}_{i:04d}'
        seg_path = os.path.join(output_dir, 'wavs', f'{utt_id}.wav')
        segment = audio[start:end]
        segment.export(seg_path, format='wav')

        text.append(f'{utt_id} {ipa}')
        wav_scp.append(f'{utt_id} {seg_path}')
        utt2spk.append(f'{utt_id} {tier}')

with open(os.path.join(output_dir, 'text'), 'w') as f:
    f.write('\n'.join(text) + '\n')

with open(os.path.join(output_dir, 'wav.scp'), 'w') as f:
    f.write('\n'.join(wav_scp) + '\n')

with open(os.path.join(output_dir, 'utt2spk'), 'w') as f:
    f.write('\n'.join(utt2spk) + '\n')
