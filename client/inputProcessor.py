from client.methodValidator import MethodValidator

class InputProcessor:

    @classmethod
    def get_inputs():
        print('Method Name ?: ', end='')
        method = MethodValidator.get_method()
        print('Params ?: ', end='')
        params = input().split() 
        print('Params Types ?: ', end='')
        params_type = input().split()
        return [method, params, params_type]

    @classmethod
    def __get_method():
        valid_method = MethodValidator.get_valid_methods()

        while True:
            is_method_valid = False

            method = input()

            for valid in valid_method:
                if valid == method:
                    is_method_valid = True
                    break
            
            if is_method_valid:
                return method
            else:
                print("You didn't enter the valid method name. You should enter valid method name again.")
