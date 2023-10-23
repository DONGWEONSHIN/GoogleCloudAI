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

## update the conda package manager to the latest version
conda update conda
## use conda to update Anaconda to the latest version
conda update anaconda
## updates all packages in the current environment to the latest version
conda update --all
## update other environments
conda update -n myenv --all



## VS Code Marketplace
- Python
- Jupyter
- Rainbow CSV
- Excel Viewer
- Python Extension Pack