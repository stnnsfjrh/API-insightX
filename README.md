<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/b999ba1b-0252-42ba-925e-c90212bcbf69" />

cara mencoba sistem rekomendasi menggunakan Postman:
1. masuk ke Postman
2. buat colection baru
3. tambahkan request post pada colection
4. masukkan link https://api-insightx-production.up.railway.app/predict
5. pindah ke bagian body>>Raw
6. masukkan script JSON dan bebas untuk angka setiap variabel kecuali pada "plan_type" hanya boleh di isi dengan Perpaid(bayar, lalu pakai) dan Postpaid(pakai, bayar nanti)
   {
    "plan_type": "Prepaid",
    "device_brand": "Realme",
    "avg_data_usage_gb": 0.51,
    "pct_video_usage": 0,
    "avg_call_duration": 7.98,
    "sms_freq": 0,
    "monthly_spend": 12,
    "topup_freq":0 ,
    "travel_score": 0,
    "complaint_count": 0
  }
7. setelah mengisi setiap valiable, selanjutnya klik send.
9. akan muncul output top 3 rekomendasi beserta probabilitas setiap label.
   {
    "input": {
        "avg_call_duration": 7.98,
        "avg_data_usage_gb": 0.51,
        "complaint_count": 0,
        "device_brand": "Realme",
        "monthly_spend": 12,
        "pct_video_usage": 0,
        "plan_type": "Prepaid",
        "sms_freq": 0,
        "topup_freq": 0,
        "travel_score": 0
    },
    "probabilities": [
        {
            "code": 0,
            "label": "Budget Offer",
            "probability": 3.751490658032708e-05
        },
        {
            "code": 1,
            "label": "Family Plan",
            "probability": 4.260566129232757e-05
        },
        {
            "code": 2,
            "label": "Unlimited Data",
            "probability": 6.396647950168699e-05
        },
        {
            "code": 3,
            "label": "General Offer",
            "probability": 0.0026187330950051546
        },
        {
            "code": 4,
            "label": "Youth Promo",
            "probability": 0.9959027171134949
        },
        {
            "code": 5,
            "label": "Premium Plus",
            "probability": 0.00012453780800569803
        },
        {
            "code": 6,
            "label": "Roaming Package",
            "probability": 4.387765147839673e-05
        },
        {
            "code": 7,
            "label": "Combo Offer",
            "probability": 0.001116892439313233
        },
        {
            "code": 8,
            "label": "Video Streaming Pack",
            "probability": 4.914358942187391e-05
        }
    ],
    "top_3_recommendations": [
        {
            "code": 4,
            "label": "Youth Promo",
            "probability": 0.9959027171134949
        },
        {
            "code": 3,
            "label": "General Offer",
            "probability": 0.0026187330950051546
        },
        {
            "code": 7,
            "label": "Combo Offer",
            "probability": 0.001116892439313233
        }
    ]
}
