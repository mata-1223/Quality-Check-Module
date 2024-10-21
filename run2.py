from pathlib import Path

from NexR_qc.QualityCheck import *

# DataName = "fire_smoke"
# DataName = "coco8"
# DataName = "한국음식_sample2"
DataName = "AI_기반_아동_미술심리_진단을_위한_그림_데이터_구축"

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
