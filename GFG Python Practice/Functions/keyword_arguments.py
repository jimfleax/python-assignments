# Keyword Arguments
def print_info(**kwargs):
    for k, v in kwargs.items():
        print(f'{k}: {v}')
print_info(name='Bob', age=25)
