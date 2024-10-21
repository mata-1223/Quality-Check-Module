<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 76e2ea0 (241021 first commit)
from NexR_qc.QualityCheck import *

PathDict = {}
PathDict["ROOT"] = os.getcwd()
PathDict["DATA"] = os.path.join(PathDict["ROOT"], "data", "data1")

DataDict = {}
for path in os.listdir(PathDict["DATA"]):
    if not path.startswith("."):
        data_name = os.path.splitext(os.path.basename(path))[0].upper()
        DataDict[data_name] = pd.read_csv(os.path.join(PathDict["DATA"], path))

if __name__ == "__main__":

    Process = QualityCheck(DataDict)
    Process.data_check()
    Process.document_check()
    Process.na_check()
    Process.run()
    Process.save()
<<<<<<< HEAD
=======
=======
from pathlib import Path

from NexR_qc.QualityCheck import *

DataName = "data2"
PATH = {}
PATH.setdefault("ROOT", Path.cwd())
PATH.setdefault("DATA", PATH["ROOT"] / "datasets" / DataName)


if __name__ == "__main__":

    Process = QualityCheck(DataName=DataName, PathDict=PATH)
>>>>>>> 43f2c33 (241021 first commit)
>>>>>>> 76e2ea0 (241021 first commit)
