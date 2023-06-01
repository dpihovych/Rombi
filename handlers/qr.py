from aiogram import types, Router
from aiogram.filters import Command
from aiogram.types import FSInputFile
import qrcode

router = Router()


@router.message(Command('qr'))
async def send_text_based_qr(message: types.Message):
    qr = qrcode.QRCode(version=1,
                       error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=20,
                       border=2)

    qr.add_data(message.text)
    qr.make(fit=True)

    img = qr.make_image(fill_color='black', back_color='white')
    img.save('photo.png')
    img = FSInputFile('photo.png')

    await message.reply_photo(img, caption=f'<b>✅ Ваш QR-Code успішно згенеровано</b>')
