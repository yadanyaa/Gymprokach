plans = {
    "novice": {
        "M": "Novice 3-day Full-Body Linear Progression",
        "F": "Novice 3-day Full-Body with glute focus",
    },
    "intermediate": {
        "M": "Intermediate 4-day Upper/Lower with auto-RPE",
        "F": "Intermediate 4-day Upper/Lower with glute-core",
    },
    "advanced": {
        "M": "Advanced 6-day DUP PHS (Power-Hypertrophy-Strength)",
        "F": "Advanced 6-day DUP PHS with glute emphasis",
    },
}


def generate(level: str, gender: str) -> str:
    level = level.lower()
    gender = gender.upper()
    return plans.get(level, {}).get(gender, "Plan not found")
