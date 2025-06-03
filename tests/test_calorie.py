from bot.services.calorie import UserData, mifflin_st_jeor, plan


def test_mifflin_st_jeor_male():
    data = UserData(gender='M', age=30, height=180, weight=80)
    assert int(mifflin_st_jeor(data)) == 1780


def test_plan_deficit():
    data = UserData(gender='F', age=25, height=165, weight=60, activity=1.4)
    result = plan(data)
    assert result['deficit'] < result['maintenance']
