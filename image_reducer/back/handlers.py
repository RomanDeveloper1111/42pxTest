import os
import uuid


def upload_to(instance, filename, width, height):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4().hex}_{width}x{height}.{ext}'
    return os.path.join('', filename)