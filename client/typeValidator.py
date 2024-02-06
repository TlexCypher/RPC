class TypeValidator:

    @classmethod
    def is_float_number(candidate_str):
        try:
            float(candidate_str)
            return True
        except ValueError:
            return False

    @classmethod
    def is_int_number(candidate_str):
        try:
            int(candidate_str)
            return True
        except ValueError:
            return False

    @classmethod
    def is_string(candidate):
        return isinstance(candidate, str)