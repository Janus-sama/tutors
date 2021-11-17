def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = [
        '.webm', '.mkv', '.flv', '.vob', '.ogv', '.ogg',
        '.drc', '.avi', '.MTS', '.M2TS', '.TS', '.mov',
        '.qt', '.wmv', '.yuv', '.rm', '.rmvb', '.viv',
        '.asf', '.amv', '.mp4', '.m4p', '.m4v', '.mpg',
        '.mp2', '.mpeg', '.mpe', '.mpv', '.svi', '.3gp',
        '.3g2', '.f4v', '.f4p', '.f4a', '.f4b', '.roq',
        '.nsv'
    ]
    if not ext.lower() in valid_extensions:
        raise ValidationError(
            'Unsupported file extension!' /
            'Convert to mp4 video format'
        )
