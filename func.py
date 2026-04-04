from email.mime import image

import qrcode
import qrcode.constants
from qrcode.image.styledpil import StyledPilImage as styled_qr
from qrcode.image.styles.colormasks import SolidFillColorMask as solid_fill
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer as R

def QrCodeGenerator(data, logo, output):
    qr = qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(
        image_factory=styled_qr,
        module_drawer=R(),
        embeded_image_path=logo,
        color_mask=solid_fill(back_color="white", front_color="black"),
    )
    img.save(output)