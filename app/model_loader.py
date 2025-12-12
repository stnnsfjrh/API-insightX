import joblib
import json
import os
from app.config import Config

model = None
label_encoder = None
target_labels = None

def load_model():
    global model, label_encoder, target_labels

    if model is None:
        if not os.path.exists(Config.MODEL_PATH):
            raise FileNotFoundError(f"Model not found at {Config.MODEL_PATH}")
        model = joblib.load(Config.MODEL_PATH)

    if label_encoder is None:
        if not os.path.exists(Config.LABEL_ENCODER_PATH):
            raise FileNotFoundError(f"Label Encoder not found at {Config.LABEL_ENCODER_PATH}")
        label_encoder = joblib.load(Config.LABEL_ENCODER_PATH)

    if target_labels is None:
        if not os.path.exists(Config.TARGET_LABELS_PATH):
            raise FileNotFoundError(f"Target label mapping file not found at {Config.TARGET_LABELS_PATH}")
        with open(Config.TARGET_LABELS_PATH, "r") as f:
            target_labels = json.load(f)

    return model, label_encoder, target_labels
