from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

import datetime
import asyncio
import json
import os
from pathlib import Path

from data.fact import get_fact
from keyboards import reply

router = Router()

# Словарь для хранения времени последнего запроса факта
user_last_request = {}

# Словарь для хранения количества просмотренных фактов
user_fact_counts = {}

# Папка для хранения данных пользователей
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)


@router.message(F.text.lower() == 'хочу факт')
async def show_fact(message: Message):
    user_id = message.from_user.username

    await message.answer('Подготавливаю интересный факт...')
    await asyncio.sleep(1)  # Имитация задержки
    global fact
    fact = get_fact()
    if fact:
        await message.answer(f'А вот и интересный факт:\n\n<b>{fact}</b>', reply_markup=reply.save)
        await update_fact_count(user_id)  # Обновляем счетчик фактов
    else:
        await message.answer("Не удалось получить факт.")


@router.message(F.text.lower() == 'сохранить факт')
async def save_fact_in_json(message: Message):
    user_id = message.from_user.username
    filepath = DATA_DIR / f"{user_id}.json"
    bookmarks = {}

    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            try:
                bookmarks = json.load(f)
            except json.JSONDecodeError:
                bookmarks = {}

    # Получаем последний факт
    if not fact:
        await message.answer("Не удалось получить факт для сохранения.")
        return

    # Добавляем новый факт
    new_bookmark_id = len(bookmarks) + 1
    bookmarks[new_bookmark_id] = fact

    # Сохраняем обновленные данные
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(bookmarks, f, ensure_ascii=False, indent=4)

    await message.answer('Факт сохранен в закладках', reply_markup=reply.main)


@router.message(F.text.lower() == 'закладки')
async def show_bookmarks(message: Message):
    user_id = message.from_user.username
    filepath = DATA_DIR / f"{user_id}.json"

    if not os.path.exists(filepath):
        await message.answer("У вас пока нет сохраненных закладок.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        try:
            bookmarks = json.load(f)
        except json.JSONDecodeError:
            await message.answer("Ошибка при чтении закладок.")
            return

    if not bookmarks:
        await message.answer('У вас нет закладок.')
        return

    # Формируем сообщение с закладками
    bookmarks_text = "\n\n".join([f"{key}. {value}" for key, value in bookmarks.items()])
    await message.answer(f"Ваши закладки:\n\n{bookmarks_text}")


async def update_fact_count(user_id: str):
    """
    Обновляет счетчик просмотренных фактов для пользователя.
    """
    global user_fact_counts

    if user_id in user_fact_counts:
        user_fact_counts[user_id] += 1
    else:
        user_fact_counts[user_id] = 1

    filepath = DATA_DIR / "fact_count.json"

    # Загружаем текущие данные
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            try:
                fact_counts = json.load(f)
            except json.JSONDecodeError:
                fact_counts = {}
    else:
        fact_counts = {}

    # Обновляем данные
    fact_counts[str(user_id)] = user_fact_counts[user_id]

    # Сохраняем обновленные данные
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(fact_counts, f, ensure_ascii=False, indent=4)


@router.message(F.text.lower() == 'рейтинг')
async def show_rating(message: Message):
    filepath = DATA_DIR / "fact_count.json"

    if not os.path.exists(filepath):
        await message.answer("Рейтинг пока недоступен.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        try:
            fact_counts = json.load(f)
        except json.JSONDecodeError:
            await message.answer("Ошибка при чтении рейтинга.")
            return

    # Формируем сообщение с рейтингом
    sorted_rating = sorted(fact_counts.items(), key=lambda item: item[1], reverse=True)
    rating_text = "\n".join([f"Пользователь {user}: {count} фактов" for user, count in sorted_rating])
    await message.answer(f"Рейтинг:\n\n{rating_text}", reply_markup=reply.main)