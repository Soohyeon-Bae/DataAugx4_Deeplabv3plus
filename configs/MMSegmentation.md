
# How to use MMSegmentation

https://mmsegmentation.readthedocs.io/en/latest/
https://github.com/open-mmlab/mmsegmentation

1. 도커 이미지 빌드
2. 컨테이너 생성
3. mmsegmentation Git 다운로드
4. mmsegmentation 설치


## Train 

```
python3 tools/train.py configs/deeplabv3plus/[YOUR_CONFIG_FILE]
```

## Test

```
python tools/test.py configs/deeplabv3plus/[YOUR_CONFIG_FILE] work_dirs/[YOUR_PATH]/epoch_[].pth --eval mIoU --show-dir ./[YOUR_PATH]
```

