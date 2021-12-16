main_dict = {'test': 'test_value',
            'europe': 'eur',
            'dollar': 'usd',
            'ruble': 'rub'}



mein_keys = list(main_dict.keys())


for i in mein_keys:
    main_dict[i + str(len(i))] = main_dict.pop(i)

print(main_dict)