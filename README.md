# Semi-Supervised-Leaening-v1

## 실험 설계

1. kaggle+bigeye2로 모델 학습 후 bigeye1으로 추론

- 학습 데이터셋
    - kaggle_relevant_noncrack+bigeye2 : kaggle_relevant_noncrack (2,347장) + 2차년도 bigeye2_onlycrack (98장)
    - kaggle_original+bigeye2 : kaggle_original (11,299장) + 2차년도 bigeye2_onlycrack (98장)
    - kaggle_relevant_noncrack+bigeye2+bigeye1 : kaggle_relevant_noncrack (2,347장) + 2차년도 bigeye2_onlycrack (98장) + 1차년도 bigeye1_onlycrack  중 81장
    - kaggle_relevant_noncrack+bigeye1 : kaggle_relevant_noncrack (2,347장) + 1차년도 bigeye1_onlycrack  중 81장
- 추론 데이터셋
    - bigeye1_onlycrack : 1차년도 bigeye1_onlycrack (101장)
    - bigeye1_onlycrack_20 : 1차년도 bigeye1_onlycrack  중 20장
    
2. Deeplabv3plus 
 - 학습 파라미터
    - 2 classes
    - normalization
    - SGD optimizer
    - 0.01 lr
    - 0.9 momentum
    - 100 epochs
    
![image](https://user-images.githubusercontent.com/94159857/176847486-070f4a34-f80f-48ed-9264-5029c61ec1c1.png)
 
 
- 딥러닝은 robust하다고 하지만, 같은 도메인이더라도 noisy data를 함께 학습한 경우에 성능이 떨어짐(실험0, 1)
- 관련성이 낮은 데이터를 sorting하지 않고 학습한 경우 가장 성능이 나쁨(실험2)
- 관련성이 있는 데이터+같은 도메인 자료를 함께 학습할 때 성능이 좋음(실험3, 4)


## 실험 결과 
(updated 22.07.05)

![image](https://user-images.githubusercontent.com/94159857/177283437-d7162921-744b-4bcb-a6f7-2e8e34b0e7e6.png)

![image](https://user-images.githubusercontent.com/94159857/177283353-287036c1-bddf-4e05-9c38-735399ab274a.png)
