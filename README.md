# IPA ASR Benchmark for Rma (Qiang) Language

This repository presents benchmark results on phoneme-level automatic speech recognition (ASR) and error correction for the endangered Rma language, based on the study "Language Model-Based Error Correction in Endangered Language Documentation".

## Experimental Overview

We evaluate six ASR models and two language model-based error correction methods for IPA transcription.

### ASR Systems

| ASR System        | Model Origin                     | Setting                           | PER ↓ | CER ↓ |
|-------------------|----------------------------------|-----------------------------------|-------|-------|
| Wav2Vec (v1.0)    | Facebook (Schneider et al., 2019) | Frozen encoder + linear decoder   | 0.91  | 0.79  |
| Wav2Vec 2.0       | Meta (Baevski et al., 2020)       | Fine-tuned on Rma IPA             | 0.71  | 0.62  |
| Whisper (base)    | OpenAI (Radford et al., 2022)     | Multilingual zero-shot            | 0.86  | 0.75  |
| MMS               | Meta (Pratap et al., 2023)        | Fine-tuned on Rma                 | 0.68  | 0.59  |
| UAPT (zero-shot)  | Taguchi et al., 2023              | Unadapted                         | 1.00  | 0.88  |
| UAPT (fine-tuned) | Taguchi et al., 2023              | Fine-tuned on Rma IPA             | 0.58  | 0.52  |

### Post-ASR Correction (GER)

| Language Model | Type        | Parameters | Fine-tuned | PER ↓ | Δ PER |
|----------------|-------------|------------|------------|--------|--------|
| Qwen-7B        | Generative  | 7B         | Yes        | 0.48   | -0.10  |
| Qwen-0.5B      | Generative  | 0.5B       | Yes        | 0.62   | +0.04  |
| No Correction  | –           | –          | –          | 0.58   | –      |

*PER = Phoneme Error Rate; CER = Character Error Rate.*

## Project Components

This repository includes:

- Wav2Vec2 fine-tuning scripts (`finetune_wav2vec2.py`)
- Inference interfaces for Whisper and MMS
- UAPT inference and adaptation utilities
- Generative error correction modules
- ELAN file preprocessing utility (`elan_split.py`)

## Citation
N / A

If you use this repository or find the results useful, please cite:

