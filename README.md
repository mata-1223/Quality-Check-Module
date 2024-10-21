# NexR_qc
[![PyPI version](https://badge.fury.io/py/NexR-qc.svg)](https://badge.fury.io/py/NexR-qc)
<br><br>

## 요구사항
- python >= 3.6
- numpy
- pandas
- openpyxl
<br>

## 설치

### pip 설치
```
#!/bin/bash
pip install NexR_qc
```

### 정형데이터 QC

#### 디렉토리 기본 구성
- documents 하위 항목(테이블정의서, 컬럼정의서, 코드정의서)은 필수 항목은 아니지만, 테이블별 정확한 정보를 얻기위해서 작성되는 문서임 ([Github 링크](https://github.com/mata-1223/NexR_qc)의 document 폴더 내 문서 양식 참고)
- log, output 폴더는 초기에 생성되어 있지않아도 수행 결과로 자동 생성됨
- config.json 파일은 데이터 내 결측값을 커스텀하기 위한 파일로 초기에 생성되어 있지않아도 수행 결과로 자동 생성됨 (결측처리 default 값: "?", "na", "null", "Null", "NULL", " ", "[NULL]")

```
.
├── datasets/
│   ├── DataName
│   │    ├── 데이터_001.csv
│   │    ├── 데이터_002.csv
│   │    ├── 데이터_003.xlsx
│   │    ├── ...
├── documents/
│   ├── DataName
│   │    ├── 테이블정의서.xlsx
│   │    ├── 컬럼정의서.xlsx
│   │    └── 코드정의서.xlsx
├── log/
│   ├── DataName
│   │    ├── QualityCheck_yyyymmdd_hhmmss.log
│   │    ├── ...
├── output/
│   ├── DataName
│   │    └── QC결과서_yyyymmdd_hhmmss.xlsx
└── config.json
``` 
<br>

#### 예제 실행 
```
#!bin/usr/python3
from pathlib import Path
from NexR_qc.QualityCheck import *
DataName = "data1"
PATH = {}
PATH.setdefault("ROOT", Path.cwd())
PATH.setdefault("DATA", PATH["ROOT"] / "datasets" / DataName)
ext_fmt = [".csv", ".xlsx", "xls", ".ftr", ".feather", ".pkl", ".pickle"]
if __name__ == "__main__":
    Process = QualityCheck(DataName=DataName, PathDict=PATH)
```

<br>

#### Input / Output 정보

##### Input
* 데이터 타입: Dictionary 형태
	* 상세 형상: {data_name1: Dataframe1, data_name2: Dataframe2,…}
		* data_name: 데이터 테이블명 or 데이터 파일명 
		* Dataframe: 데이터를 불러온 Dataframe 형상
* 예시
![NexR_qc_Info_002](https://github.com/mata-1223/NexR_qc/assets/131343466/5e28e8bf-37f2-4cc0-acca-c288bfbd5ccb)

##### Output
* 결과 파일 경로: output/QC_결과서.xlsx
* 예시
1) 예시 1: 테이블 리스트 시트
![NexR_qc_Info_003](https://github.com/mata-1223/NexR_qc/assets/131343466/54605ebe-d45c-4ba9-b219-dd177e08a6b7)

2) 예시 2: 데이터 별 QC 수행 결과 시트
![NexR_qc_Info_001](https://github.com/mata-1223/NexR_qc/assets/131343466/a1613944-4812-40a2-9ec3-6452c104a96b)

### 이미지 데이터 QC

#### 디렉토리 기본 구성
- documents 하위 항목(데이터정의서)은 필수 항목은 아니지만, 테이블별 정확한 정보를 얻기위해서 작성되는 문서임 ([Github 링크](https://github.com/mata-1223/NexR_qc)의 document 폴더 내 문서 양식 참고)
  * 초기 파일이 없는 경우 최초 모듈 실행으로 생성됨
- log, output 폴더는 초기에 생성되어 있지않아도 수행 결과로 자동 생성됨

##### 일반
```
.
├── datasets/
│   ├── DataName/
│   │    ├── (optional) train/
│   │    │   ├── img_00001.png
│   │    │   ├── img_00002.png
│   │    │   ├── img_00003.png
│   │    │   ├── ...
├── documents/
│   ├── DataName
│   │    └── (optional) 데이터정의서.xlsx
├── log/
│   ├── DataName
│   │    ├── QualityCheck_yyyymmdd_hhmmss.log
│   │    ├── ...
├── output/
│   ├── DataName
│   │    └── QC결과서_yyyymmdd_hhmmss.xlsx
``` 
<br>

##### 분류
```
.
├── datasets/
│   ├── DataName/
│   │    ├── train/
│   │    │   ├── 분류Class001명/
│   │    │   │   ├── img_00001.png
│   │    │   │   ├── img_00002.png
│   │    │   │   ├── ...
│   │    │   ├── 분류Class002명/
│   │    ├── 분류Class002명/
│   │    ├── 분류Class003명/
│   │    ├── ...
├── documents/
│   ├── DataName
│   │    └── (optional) 데이터정의서.xlsx
├── log/
│   ├── DataName
│   │    ├── QualityCheck_yyyymmdd_hhmmss.log
│   │    ├── ...
├── output/
│   ├── DataName
│   │    └── QC결과서_yyyymmdd_hhmmss.xlsx
└── config.json
``` 
<br>

##### 객체탐지
```
.
├── datasets/
│   ├── DataName/
│   │    ├── images/
│   │    │   ├── train/
│   │    │   │   ├── img_00001.png
│   │    │   │   ├── img_00002.png
│   │    │   │   ├── ...
│   │    │   ├── val/
│   │    │   │   ├── img_10001.png
│   │    │   │   ├── img_10002.png
│   │    │   │   ├── ...
│   │    ├── labels/
│   │    │   ├── train/
│   │    │   │   ├── img_00001.txt
│   │    │   │   ├── img_00002.txt
│   │    │   │   ├── ...
│   │    │   ├── val/
│   │    │   │   ├── img_10001.txt
│   │    │   │   ├── img_10002.txt
│   │    │   │   ├── ...
│   │    ├── ...
├── documents/
│   ├── DataName
│   │    └── (optional) 데이터정의서.xlsx
├── log/
│   ├── DataName
│   │    ├── QualityCheck_yyyymmdd_hhmmss.log
│   │    ├── ...
├── output/
│   ├── DataName
│   │    └── QC결과서_yyyymmdd_hhmmss.xlsx
└── DataName.yaml
``` 
<br>

#### 예제 실행
```
#!bin/usr/python3
from pathlib import Path
from NexR_qc.QualityCheck import *
DataName = "한국음식_sample2" # 분류 Case 예시
# DataName = "fire_smoke"
# DataName = "coco8"
# DataName = "AI_기반_아동_미술심리_진단을_위한_그림_데이터_구축"
PATH = {}
PATH.setdefault("ROOT", Path.cwd())
PATH.setdefault("DATA", PATH["ROOT"] / "datasets" / DataName)
PATH.setdefault("IMAGE", PATH["DATA"])
# PATH.setdefault("IMAGE", PATH["DATA"] / "images")
# PATH.setdefault("LABEL", PATH["DATA"] / "labels")
# PATH.setdefault("YAML", PATH["ROOT"] / "coco8.yaml")
# PATH.setdefault("YAML", PATH["ROOT"] / "fire_smoke.yaml")
logger_save = False
# mode = "일반"
mode = "분류"
# mode = "객체탐지"
if __name__ == "__main__":
    Process = QualityCheck(DataName=DataName, DataType="image", Mode=mode, PathDict=PATH, logger_save=logger_save)
```

#### Output 형상
##### 일반
![NexR_qc_Info_003](https://github.com/mata-1223/NexR_qc/blob/test/img/NexR_qc_Info_001.png)

![NexR_qc_Info_003](https://github.com/mata-1223/NexR_qc/blob/test/img/NexR_qc_Info_002.png)

![NexR_qc_Info_003](https://github.com/mata-1223/NexR_qc/blob/test/img/NexR_qc_Info_003.png)