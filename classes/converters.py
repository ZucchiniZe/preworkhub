from .models import Subject


class SubjectConverter:
    regex = '|'.join(map(lambda tup: tup[0], Subject.CLASS_CHOICES))

    @staticmethod
    def to_python(value):
        return value

    @staticmethod
    def to_url(value):
        return value
