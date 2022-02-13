class LoadFromFile:

    @staticmethod
    def begin(file_name):
        try:
            with open(file_name, "r") as file:
                for line in file:
                    for creature in line.strip():
                        match creature:
                            case 'B':
                                pass
        except FileNotFoundError:
            print('ERROR. No such file or directory:', file_name)
