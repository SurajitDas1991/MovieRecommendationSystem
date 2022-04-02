import os
from pathlib import Path
import textwrap
import shutil

files = [
    # "dvc.yaml",
    # "params.yaml",
    os.path.join("src", "__init__.py"),
    os.path.join("src","Training", "__init__.py"),
    os.path.join("src","Prediction", "__init__.py"),
    os.path.join("src","dashboard.py")
]


def prepare_project():
    delete_create_existing_folders(VISUALIZATION_PATH)
    delete_create_existing_folders(METRICS_PATH)
    delete_create_existing_folders(MODELS_PATH)
    delete_create_existing_folders(NOTEBOOKS_PATH)
    delete_create_existing_folders(TRAINING_PROCESSED_DATA_FOLDER)
    delete_create_existing_folders(FINAL_MODEL_PATH)
    delete_create_existing_folders(DATABASE_FOLDER)
    #CreateTemplateFolders(LOGS_PATH)
    CreateTemplateFolders(TRAINING_RAW_DATA_FOLDER)
    #Create the files
    for file_ in files:
        with open(file_, "w") as f:
            pass

def delete_create_existing_folders(path):
        try:
            if os.path.isdir(path):
                shutil.rmtree(path)
            if not os.path.isdir(path):
                os.makedirs(path)

        except Exception as e:
            pass

def CreateTemplateFolders(folder_name):
    Path(f"{folder_name}").mkdir(parents=True, exist_ok=True)

def wrap_labels(ax, width, break_long_words=False):
    labels = []
    for label in ax.get_xticklabels():
        text = label.get_text()
        labels.append(
            textwrap.fill(text, width=width, break_long_words=break_long_words)
        )
    ax.set_xticklabels(labels, rotation=0)

def get_file_path(path,filename):
    return os.path.join(
            path, filename
        )

def get_folder_path(*path):
    cwd = os.path.abspath(os.getcwd())
    temp_path = ""
    for i in path:
        cwd = os.path.join(cwd, i)
    return cwd


LOGS_PATH=get_folder_path("logs")
NOTEBOOKS_PATH=get_folder_path("notebooks")
VISUALIZATION_PATH = get_folder_path("reports", "figures")
METRICS_PATH = get_folder_path("reports","metrics")
MODELS_PATH = get_folder_path("models")
FINAL_MODEL_PATH=get_folder_path("models","final")
FINAL_INPUT_FILE_FROM_DB = get_folder_path("data", "final")
DATABASE_FOLDER = get_folder_path("database")
TRAINING_RAW_DATA_FOLDER = get_folder_path("data", "raw","training")
TRAINING_PROCESSED_DATA_FOLDER = get_folder_path("data", "processed","training")
# GOOD_RAW_DATA_FOLDER = return_full_path("data", "processed", "good_raw")
# BAD_RAW_DATA_FOLDER = return_full_path("data", "processed", "bad_raw")
ARCHIVED_RAW_DATA_FOLDER = get_folder_path("data", "archived")
