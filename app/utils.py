import pandas as pd
from app.config import Config

def validate_and_build_df(payload):
    missing = []

    for f in Config.EXPECTED_FEATURES:
        if f not in payload:
            missing.append(f)

    if missing:
        return None, f"Missing required fields: {missing}"

    df = pd.DataFrame([payload[f] for f in Config.EXPECTED_FEATURES]).T
    df.columns = Config.EXPECTED_FEATURES

    return df, None
