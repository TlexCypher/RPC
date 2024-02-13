from typeValidator import TypeValidator

class MethodValidator:
    
    @classmethod
    def get_valid_methods(cls):
        return ['floor', 'nroot', 'reverse', 'validAnagram', 'sort']

    @classmethod
    def is_valid_comb(cls, method, params, param_types):
        valid_methods = MethodValidator.get_valid_methods()
        if method not in valid_methods:
            return False

        if method == 'floor':
            return MethodValidator.__is_valid_comb_floor_helper(params, param_types)

        elif method == 'nroot':
            return MethodValidator.__is_valid_comb_nroot_helper(params, param_types)
        
        elif method == 'reverse':
            return MethodValidator.__is_valid_comb_reverse_helper(params, param_types)
        
        elif method == 'validAnagram':
            return MethodValidator.__is_valid_comb_valid_anagram_helper(params, param_types)
        else:
            return MethodValidator.__is_valid_comb_sort_helper(params, param_types)

    @classmethod
    def __is_valid_comb_floor_helper(cls, params, param_types):
        floor_params_number = 1
        floor_param_types = ['double']

        if len(params) != floor_params_number:
            return False
        
        if not TypeValidator.is_float_number(params[0]):
            return False

        if not (param_types == floor_param_types):
            return False
            
        return True

    @classmethod
    def __is_valid_comb_nroot_helper(cls, params, param_types):
        nroot_params_number = 2
        nroot_param_types = ['int', 'int']

        if len(params) != nroot_params_number:
            return False

        if not (TypeValidator.is_int_number(params[0]) or TypeValidator.is_int_number(params[1])):
            return False

        if not (param_types == nroot_param_types):
            return False
        return True

    @classmethod
    def __is_valid_comb_reverse_helper(cls, params, param_types):
        reverse_params_number = 1
        reverse_param_types = ['string']

        if len(params) != reverse_params_number:
            return False

        if not TypeValidator.is_string(params[0]):
            return False

        if not (param_types == reverse_param_types):
            return False
            
        return True

    @classmethod        
    def __is_valid_comb_valid_anagram_helper(cls, params, param_types):
        print(params)
        print(param_types)
        anagram_params_number = 2
        anagram_param_types = ['string', 'string']

        if len(param_types) != anagram_params_number:
            return False

        if not (TypeValidator.is_string(params[0]) or TypeValidator.is_string([params[1]])):
            return False

        if not (anagram_param_types == param_types):
            return False

        return True

    @classmethod
    def __is_valid_comb_sort_helper(cls, params, param_types):
        sort_param_types = ['string[]']

        for param in params:
            if not TypeValidator.is_string(param):
                return False
        
        if not (sort_param_types == param_types):
            return False

        return True