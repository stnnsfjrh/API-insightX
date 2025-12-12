class Config:
    EXPECTED_FEATURES = [
        "plan_type",
        "device_brand",
        "avg_data_usage_gb",
        "pct_video_usage",
        "avg_call_duration",
        "sms_freq",
        "monthly_spend",
        "topup_freq",
        "travel_score",
        "complaint_count"
    ]

    MODEL_PATH = "model/xgboost_telco_model.joblib"
    LABEL_ENCODER_PATH = "model/label_encoder.joblib"
    TARGET_LABELS_PATH = "data/target_labels.json"
