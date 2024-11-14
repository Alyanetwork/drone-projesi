# src/modules/ai_control/behavior_analysis.py

class BehaviorAnalysis:
    def __init__(self):
        pass

    def analyze_behavior(self, person_features):
        # Örneğin, ellerde silah olup olmadığını kontrol etmek, tehlikeli davranışları belirlemek
        if person_features.get("weapon", False):
            return "Tehdit Tespit Edildi: Terörist Olabilir."
        return "Sivil Tespit Edildi."

    def detect_threat_level(self, detected_objects):
        for obj in detected_objects:
            if obj == "silah" or obj == "bıçak":
                return "Yüksek Tehdit"
        return "Düşük Tehdit"
