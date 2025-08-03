import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.enums import ParseMode

TOKEN = "7949632155:AAFpJNIFZXRF5S-fayIKPJLC0xa60j-CrHg"
ADMIN_PASSWORD = "shirinsuv"

bot = Bot(token=TOKEN)
dp = Dispatcher()

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📅 Dars Jadvali"), KeyboardButton(text="🧑‍🏫 O'qituvchilar")],
        [KeyboardButton(text="🧑‍🎓 Guruhlar"), KeyboardButton(text="📞 Aloqa uchun")],
    ],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "🏫 <b>Shirinsuv Xususiy Maktabiga Xush Kelibsiz!</b>\n\n"
        "Iltimos, quyidagilardan birini tanlang:",
        reply_markup=main_kb,
        parse_mode=ParseMode.HTML
    )

@dp.message(lambda msg: msg.text == "📅 Dars Jadvali")
async def timetable(message: types.Message):
    await message.answer(
        "🗓 <b>Dars Jadvali</b>\n\n"
        "<b>Dushanba - Shanba:</b>\n"
        "• 08:30 – 16:30 — Matematika (abituriyent)\n"
        "• 08:30 – 16:30 — Fizika (abituriyent)\n\n"
        "<b>Yakshanba:</b>\n"
        "• 10:00 – 12:00 — Takrorlash",
        parse_mode=ParseMode.HTML
    )

@dp.message(lambda msg: msg.text == "🧑‍🏫 O'qituvchilar")
async def teachers(message: types.Message):
    await message.answer(
        "👩‍🏫 <b>Ustozlar ro'yxati</b>\n\n"
        "• <b>Iqboljon</b> — Matematika\n"
        "• <b>Oybek</b> — Fizika\n"
        "• <b>--------</b> — Ingliz tili",
        parse_mode=ParseMode.HTML
    )

@dp.message(lambda msg: msg.text == "🧑‍🎓 Guruhlar")
async def groups(message: types.Message):
    await message.answer(
        "👥 <b>Hozirgi guruhlar:</b>\n\n"
        "1. Matematika (kichik)\n"
        "2. Matematika (abituriyent)\n"
        "3. Ingliz tili (kichik)\n"
        "4. Ingliz tili (abituriyent)\n"
        "5. Fizika (abituriyent)",
        parse_mode=ParseMode.HTML
    )

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@dp.message(lambda msg: msg.text == "📞 Aloqa uchun")
async def contacts(message: types.Message):
    contact_buttons = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="📘 Facebook", url="https://facebook.com/shirinsuv_maktabi"),
            InlineKeyboardButton(text="📸 Instagram", url="https://instagram.com/shirinsuv_maktabi")
        ],
        [
            InlineKeyboardButton(text="📍 Manzilni ko‘rish (Google Maps)", url="https://maps.app.goo.gl/s1Cna6XsXy8KHyvo8")
        ]
    ])

    await message.answer(
        "📍 <b>Bizga murojaat qiling:</b>\n\n"
        "🏠 <b>Manzil:</b> Fargʻona viloyati, Bag'dod tumani, Irğoli qishlogʻi, Shirinsuv Maktabi\n"
        "📞 <b>Telefon:</b> <a href='tel:+998908571171'>+998 90 857 11 71</a>\n"
        "✉️ <b>Email:</b> <a href='mailto:info@learningcenter.com'>info@learningcenter.com</a>\n\n"
        "🔗 <b>Ijtimoiy tarmoqlar:</b>",
        parse_mode=ParseMode.HTML,
        reply_markup=contact_buttons
    )

# Admin password check flow
@dp.message(Command("adminsh"))
async def broadcast_start(message: types.Message):
    await message.answer("🔐 <b>Iltimos, admin parolini kiriting:</b>", parse_mode=ParseMode.HTML)

@dp.message(lambda msg: msg.reply_to_message and "admin parolini" in msg.reply_to_message.text.lower())
async def check_password(message: types.Message):
    if message.text == ADMIN_PASSWORD:
        await message.answer("✅ Parol to'g'ri. Endi e'lon yuboring.\n"
                             "Xabarni yozing va bu xabarga javoban yuboring.")
    else:
        await message.answer("❌ Noto'g'ri parol!")

@dp.message(lambda msg: msg.reply_to_message and "e'lon yuboring" in msg.reply_to_message.text.lower())
async def send_broadcast(message: types.Message):
    await message.answer("📢 <b>Admin E'loni:</b>\n" + message.text, parse_mode=ParseMode.HTML)
    await message.answer("✅ E'lon muvaffaqiyatli yuborildi!", reply_markup=main_kb)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
