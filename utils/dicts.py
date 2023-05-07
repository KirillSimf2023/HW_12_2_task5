# Описание функционала функции
# Функция возвращает значение из словаря по переданному ключу,
# если ключ существует. В ином случае возвращается значение default.
# Примеры работы:
# >>> data = {"vcs": "mercurial"}
# >>> get_val(data, "vcs")
# 'mercurial'
# >>> get_val(data, "vcs", "git")
# 'mercurial'
# >>> data = {}
# >>> get_val({}, "vcs", "git")
# 'git'
# >>> get_val({}, "vcs", "bazaar")
# 'bazaar'


def get_val(collection: dict, key: str, default='git'):
    """
    Функция возвращает значение из словаря по переданному ключу,
    если ключ существует.
    В ином случае возвращается значение default.
    :param collection: Исходный словарь.
    :param key: Ключь извлекаемого элемента.
    :param default: значение по-умолчанию.
    :return: значение из словаря по переданному ключу или значение по-умолчанию.
    """

    if len(collection) == 0:
        return default

    if key not in collection.keys():
        return default

    return collection[key]


