from bot.services.orm import OrmData, calculate_all


def test_calculate_all():
    data = OrmData(weight=100, reps=5)
    res = calculate_all(data)
    assert res['brzycki'] > 100
    assert res['epley'] > 100
    assert res['lombardi'] > 100
