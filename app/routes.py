from flask import Blueprint, request, jsonify
from app.utils import validate_and_build_df
from app.model_loader import load_model
from app.config import Config

bp = Blueprint("api", __name__)

@bp.route("/", methods=["GET"])
def home():
    return jsonify({"message": "API InsightX is running"})


@bp.route("/health", methods=["GET", "POST"])
def health():
    try:
        load_model()
        return jsonify({"status": "ok", "model": "loaded"})
    except Exception as e:
        return jsonify({"status": "error", "detail": str(e)}), 500


@bp.route("/predict", methods=["POST"])
def predict():
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 400

    payload = request.get_json()
    df, error = validate_and_build_df(payload)

    if error:
        return jsonify({"error": error}), 400

    try:
        model, label_encoder, target_labels = load_model()

        # Predict encoded label
        encoded_pred = model.predict(df)[0]

        # Convert encoded label → original text
        decoded_label = target_labels.get(str(encoded_pred), "UNKNOWN")

        # Probabilities
        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(df)[0]
            class_ids = model.classes_

            all_prob = {
                str(c): {
                    "code": int(c),
                    "label": target_labels[str(c)],
                    "probability": float(p)
                }
                for c, p in zip(class_ids, proba)
            }
        else:
            all_prob = {}

        return jsonify({
            "input": payload,
            "recommended_offer_code": int(encoded_pred),
            "recommended_offer_label": decoded_label,
            "probabilities": all_prob
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
