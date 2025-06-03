from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.services.calorie import UserData, plan
from bot.services.orm import OrmData, calculate_all
from bot.services.program import generate

router = Router()
user_state: dict[int, UserData] = {}

@router.message(Command("ping"))
async def ping(message: types.Message) -> None:
    await message.answer("pong")

@router.message(Command("start"))
async def start(message: types.Message) -> None:
    text = (
        "Привет! Я фитнес-бот. Пройдите анкету командой /survey "
        "и получите доступ к калькулятору калорий и тренировочным планам."
    )
    await message.answer(text)

@router.message(Command("survey"))
async def survey(message: types.Message) -> None:
    await message.answer(
        "Отправьте данные в формате: пол М/Ж, возраст, рост, вес, активность 1.2-2.0\n"
        "Например: M 30 180 80 1.55"
    )

@router.message(lambda m: len(m.text.split()) == 5 and m.text.split()[0] in {"M", "F"})
async def save_survey(message: types.Message) -> None:
    gender, age, height, weight, act = message.text.split()
    user_state[message.from_user.id] = UserData(
        gender=gender,
        age=int(age),
        height=float(height),
        weight=float(weight),
        activity=float(act),
    )
    menu = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="\U0001F4CA Мои калории", callback_data="calories")],
        [InlineKeyboardButton(text="\U0001F4AA Мой план", callback_data="program")],
        [InlineKeyboardButton(text="\u2699\uFE0F Настройки", callback_data="settings")],
    ])
    await message.answer("Данные сохранены!", reply_markup=menu)

@router.callback_query(lambda c: c.data == "calories")
async def cb_calories(query: types.CallbackQuery) -> None:
    user = user_state.get(query.from_user.id)
    if not user:
        await query.message.answer("Сначала пройдите анкету /survey")
        return
    result = plan(user)
    text = (
        f"Суточные калории: {result['maintenance']}\n"
        f"Дефицит -15%: {result['deficit']}\n"
        f"Профицит +10%: {result['surplus']}"
    )
    await query.message.answer(text)

@router.callback_query(lambda c: c.data == "program")
async def cb_program(query: types.CallbackQuery) -> None:
    user = user_state.get(query.from_user.id)
    if not user:
        await query.message.answer("Сначала пройдите анкету /survey")
        return
    plan_text = generate("novice", user.gender)
    await query.message.answer(plan_text)

@router.callback_query(lambda c: c.data == "settings")
async def cb_settings(query: types.CallbackQuery) -> None:
    await query.message.answer("Настройки пока недоступны")

@router.message(Command("orm"))
async def orm_cmd(message: types.Message) -> None:
    await message.answer("Введите вес и количество повторов: 100 5")

@router.message(lambda m: len(m.text.split()) == 2 and m.text.split()[0].isdigit())
async def orm_calc(message: types.Message) -> None:
    weight, reps = map(float, message.text.split())
    data = OrmData(weight=weight, reps=int(reps))
    result = calculate_all(data)
    await message.answer("\n".join(f"{k}: {v}" for k, v in result.items()))

@router.message(Command("nutrition"))
async def nutrition(message: types.Message) -> None:
    await message.answer("Пример меню будет доступно позже")

@router.message(Command("tracker"))
async def tracker(message: types.Message) -> None:
    await message.answer("Запись результатов пока не реализована")

@router.message(Command("summary"))
async def summary(message: types.Message) -> None:
    await message.answer("Отчёт за неделю недоступен")

@router.message(Command("stretch"))
async def stretch(message: types.Message) -> None:
    await message.answer("Случайная разминка: data/stretch1.gif")

@router.message(Command("challenge"))
async def challenge(message: types.Message) -> None:
    await message.answer("Таблица лидеров скоро появится")

@router.message(Command("mindset"))
async def mindset(message: types.Message) -> None:
    await message.answer("Аудио медитации пока нет")

@router.message(Command("settings"))
async def settings_cmd(message: types.Message) -> None:
    await message.answer("Настройки в разработке")

@router.message(Command("broadcast"))
async def broadcast(message: types.Message) -> None:
    await message.answer("Рассылка недоступна")
