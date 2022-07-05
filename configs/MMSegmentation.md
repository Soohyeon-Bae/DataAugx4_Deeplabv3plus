
# How to use MMSegmentation
--

## Train

```
python3 tools/train.py configs/deeplabv3plus/[YOUR_CONFIG_FILE]
```

## Test

```
python tools/test.py configs/deeplabv3plus/[YOUR_CONFIG_FILE] work_dirs/[YOUR_PATH]/epoch_[].pth --eval mIoU --show-dir ./[YOUR_PATH]
```

