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

# 👉 Tambahan GET supaya tidak error 405 saat dibuka di browser
@bp.route("/predict", methods=["GET"])
def predict_get():
    return jsonify({
        "message": "Use POST with JSON body to access this endpoint",
        "note": "This endpoint only processes predictions via POST",
        "example": {
            "method": "POST",
            "url": "/predict",
            "body_format": "application/json"
        }
    })


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
        decoded_label = target_labels.get(str(encoded_pred), "UNKNOWN")

        # Probabilities
        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(df)[0]
            class_ids = model.classes_

            # Buat list of dict berisi code-label-probability
            prob_list = [
                {
                    "code": int(c),
                    "label": target_labels[str(c)],
                    "probability": float(p)
                }
                for c, p in zip(class_ids, proba)
            ]

            # Sort dari probabilitas tertinggi → ambil Top 3
            top3 = sorted(prob_list, key=lambda x: x["probability"], reverse=True)[:3]

        else:
            prob_list = []
            top3 = []

        return jsonify({
            "input": payload,
            "probabilities": prob_list,
            "top_3_recommendations": top3
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
