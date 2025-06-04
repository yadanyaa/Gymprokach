from pydantic import BaseModel

class UserData(BaseModel):
    gender: str
    age: int
    height: float
    weight: float
    activity: float = 1.2


def mifflin_st_jeor(data: UserData) -> float:
    if data.gender.lower().startswith('m'):
        bmr = 10 * data.weight + 6.25 * data.height - 5 * data.age + 5
    else:
        bmr = 10 * data.weight + 6.25 * data.height - 5 * data.age - 161
    return bmr


def daily_calories(data: UserData) -> float:
    return mifflin_st_jeor(data) * data.activity


def macros(calories: float) -> dict:
    protein = 0.3 * calories / 4
    fat = 0.3 * calories / 9
    carbs = 0.4 * calories / 4
    return {"protein": round(protein), "fat": round(fat), "carbs": round(carbs)}


def plan(data: UserData) -> dict:
    maint = daily_calories(data)
    deficit = maint * 0.85
    surplus = maint * 1.1
    return {
        "maintenance": round(maint),
        "deficit": round(deficit),
        "surplus": round(surplus),
        "macros": {
            "maintenance": macros(maint),
            "deficit": macros(deficit),
            "surplus": macros(surplus),
        },
    }
