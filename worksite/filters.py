class EqualFilter:

    def __call__(self, field, value):
        return {
            field: value
        }
