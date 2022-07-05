# Train

```
python3 tools/train.py configs/deeplabv3plus/[YOUR_CONFIG_FILE]
```

# Test

```
python tools/test.py configs/deeplabv3plus/[YOUR_CONFIG_FILE] work_dirs/[YOUR_PATH]/epoch_[].pth --eval mIoU --show-dir ./[YOUR_PATH]
```

# Result
![image](https://user-images.githubusercontent.com/94159857/177282323-202657f8-4df3-4dca-b732-753f35f2c0e1.png)
![image](https://user-images.githubusercontent.com/94159857/177282406-077e3b1b-e687-44a4-9140-93698245de2e.png)
