"""Utile for factory_boy and custom fakers."""


import factory


def show_all_possible_fakers(print_variants=True):
    """Display name all providers of fakers with examples for the Factory Boy."""

    all_formatters = list()
    for attribute in dir(factory.Faker._get_faker()):
        try:
            flag = False
            if not attribute.startswith('_'):
                flag = True
                factory.Faker(attribute).generate([])
        except:
            pass
        else:
            if flag:
                all_formatters.append(attribute)

    line = '-' * 80
    for formatter in all_formatters:
        print(line)
        print('factory.Faker({0})'.format(formatter))

        if print_variants is True:
            print(line)
            for i in range(10):
                output = factory.Faker(formatter).generate([])
                output = str(output)[:100]
                print('\t{0}'.format(output))
