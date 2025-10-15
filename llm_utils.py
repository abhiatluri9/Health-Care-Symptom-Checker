def get_symptom_analysis(symptom_text: str):
    symptom_text = symptom_text.lower().strip()

    if not symptom_text:
        return {
            "conditions": ["No symptoms provided."],
            "recommendations": ["Please select symptoms or describe them in the textbox."],
            "disclaimer": "This tool is for educational purposes only. Please consult a licensed healthcare professional for diagnosis and treatment."
        }

    responses = []

    symptom_map = {
        "fever": {
            "conditions": [
                "Condition: Viral Fever",
                "Condition: Typhoid (if prolonged)",
                "Condition: Dengue (if accompanied by body pain or rash)"
            ],
            "recommendations": [
                "Medication: Paracetamol 500mg every 6 hours as needed",
                "Hydration: Drink 2–3 liters of water daily",
                "Monitoring: Track temperature every 4 hours",
                "Consultation: Visit a doctor if fever persists beyond 3 days or exceeds 102°F"
            ]
        },
        "stomach pain": {
            "conditions": [
                "Condition: Constipation",
                "Condition: Gastroenteritis",
                "Condition: Acid Reflux",
                "Condition: Irritable Bowel Syndrome (IBS)"
            ],
            "recommendations": [
                "Medication: Antacids (e.g., omeprazole) or mild laxatives (e.g., lactulose)",
                "Diet: Avoid spicy, oily, and dairy-heavy foods",
                "Hydration: Warm water and fiber-rich meals",
                "Consultation: Seek medical advice if pain is severe or persistent"
            ]
        },
        "abdominal pain": "stomach pain",  # alias
        "loose motion": {
            "conditions": [
                "Condition: Acute Gastroenteritis",
                "Condition: Food Poisoning",
                "Condition: Viral Diarrhea"
            ],
            "recommendations": [
                "Medication: Oral Rehydration Salts (ORS), racecadotril, or loperamide (if advised)",
                "Diet: Bland foods like rice, bananas, toast",
                "Hydration: Frequent sips of ORS or electrolyte drinks",
                "Consultation: Visit a doctor if symptoms last more than 2 days or include blood"
            ]
        },
        "diarrhea": "loose motion",  # alias
        "headache": {
            "conditions": [
                "Condition: Tension Headache",
                "Condition: Migraine",
                "Condition: Sinusitis (if facial pressure or nasal congestion)"
            ],
            "recommendations": [
                "Medication: Paracetamol or ibuprofen",
                "Rest: Avoid screen time and bright lights",
                "Hydration: Drink water regularly",
                "Consultation: Seek medical advice if headaches are frequent or severe"
            ]
        },
        "vomiting": {
            "conditions": [
                "Condition: Gastritis",
                "Condition: Food Poisoning",
                "Condition: Viral Infection"
            ],
            "recommendations": [
                "Medication: Ondansetron or domperidone (as prescribed)",
                "Diet: Avoid solid food until vomiting stops; start with clear liquids",
                "Hydration: Small sips of water or ORS",
                "Consultation: Visit a doctor if vomiting persists or includes blood"
            ]
        },
        "nausea": "vomiting",  # alias
        "cold": {
            "conditions": [
                "Condition: Common Cold",
                "Condition: Upper Respiratory Tract Infection",
                "Condition: Allergic Rhinitis"
            ],
            "recommendations": [
                "Medication: Cetirizine for allergies, paracetamol for fever",
                "Home Remedies: Steam inhalation, warm salt water gargles",
                "Hydration: Drink warm fluids like soup or herbal tea",
                "Consultation: Seek medical advice if cough lasts more than 7 days"
            ]
        },
        "cough": "cold",  # alias
        "sore throat": "cold"  # alias
    }

    matched_conditions = []
    matched_recommendations = []

    for key, value in symptom_map.items():
        if key in symptom_text:
            if isinstance(value, str):  # alias
                value = symptom_map[value]
            matched_conditions.extend(value["conditions"])
            matched_recommendations.extend(value["recommendations"])

    if not matched_conditions:
        return {
            "conditions": ["Condition: Unable to determine specific cause"],
            "recommendations": [
                "Recommendation: Please provide more detailed symptoms",
                "Recommendation: Consider visiting a healthcare provider for evaluation"
            ],
            "disclaimer": "This tool is for educational purposes only. Please consult a licensed healthcare professional for diagnosis and treatment."
        }

    return {
        "conditions": list(set(matched_conditions)),
        "recommendations": list(set(matched_recommendations)),
        "disclaimer": "This tool is for educational purposes only. Please consult a licensed healthcare professional for diagnosis and treatment."
    }
