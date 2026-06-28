"""
Recommendation service for HeartSense AI.
"""


class RecommendationService:

    def generate(self, patient: dict, prediction: int):

        if prediction == 1:
            return {
                "calories": 1800,
                "diet": [
                    "Oatmeal with berries",
                    "Grilled fish",
                    "Steamed vegetables",
                    "Brown rice",
                    "Mixed nuts"
                ],
                "exercise": "30 minutes brisk walking daily",
                "water_intake": "2.5 L/day",
                "lifestyle": [
                    "Reduce sodium intake",
                    "Avoid smoking",
                    "Limit saturated fats",
                    "Sleep 7-8 hours",
                    "Monitor blood pressure regularly"
                ]
            }

        return {
            "calories": 2200,
            "diet": [
                "Whole grains",
                "Fresh fruits",
                "Lean chicken",
                "Vegetable salad"
            ],
            "exercise": "45 minutes moderate exercise",
            "water_intake": "3 L/day",
            "lifestyle": [
                "Maintain healthy weight",
                "Exercise regularly",
                "Annual health check-up"
            ]
        }