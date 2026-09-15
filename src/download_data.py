from pathlib import Path
import shutil
import kagglehub


dataset_id = "anirudhchauhan/retail-store-inventory-forecasting-dataset"

project_root = Path(__file__).resolve().parents[1]
raw_dir = project_root / "data" / "raw"

raw_dir.mkdir(parents=True, exist_ok= True)
dataset_path = Path(kagglehub.dataset_download(dataset_id))

source_file = dataset_path / "retail_store_inventory.csv"
destination_file = raw_dir / "retail_store_inventory.csv"

shutil.copy2(source_file, destination_file)

print("dataset descargado correctamente:")



for file in dataset_path.rglob("*"):
    if file.is_file():
        print(file)