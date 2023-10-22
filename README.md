# GoogleCloudAI
Google Cloud 기반 인공지능 개발자 과정

### git 토근 변경시
- git remote set-url origin https://\<username\>:\<token\>@github.com/...git

### git을 pull 하기전에 변경사항이 있는지 확인 함
- git fetch origin main

### git을 리셋 함
- git reflog
- git reset --hard HEAD@{16}

## conda 패키지 설치 (초반 필수 패키지)
conda install -y jupyter ipykernel pandas matplotlib seaborn xlrd openpyxl scikit-learn

## pyqt5 conda install
conda install -c anaconda pyqt

## 아나콘다 자체를 최신으로 업데이트
(base) conda update conda
(base) conda update anaconda
(base) conda update -n base conda

## conda 패키지 전체 업데이트
(base) conda update -all