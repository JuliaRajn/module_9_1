def apply_all_func(int_list, *functions):
  """
  Применяет к списку int_list все переданные функции и
  возвращает словарь с результатами.

  Args:
    int_list: Список чисел.
    *functions: Неограниченное кол-во функций, работающих со списками чисел.

  Returns:
    Словарь, где ключом является название функции,
    а значением - результат её работы со списком int_list.
  """
  results = {}
  for func in functions:
    results[func.__name__] = func(int_list)
  return results

# Пример использования:
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
