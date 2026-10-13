from pathlib import Path
from nuscenes.nuscenes import NuScenes


project_root = Path(__file__).resolve().parents[1]

dataroot = project_root / "data" / "nuscenes"


nusc = NuScenes(version="v1.0-trainval",dataroot=str(dataroot), verbose=False)
print("total scenes:", len(nusc.scene))
print("total sample for mini-dataset:", len(nusc.sample))

