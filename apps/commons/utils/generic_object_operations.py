import re

from django.utils.text import slugify


class GenericObjectOperations:
    """
    All the generic object related operations.
    """

    @staticmethod
    def convert_string_to_character_list(word):
        """
        Convert string to character list.

        Example:
            "ABC" => ['A','B','C']

        :param word: (str)
        :return: (list)
        """
        list1 = []
        list1[:0] = word
        return list1

    @staticmethod
    def format_string_for_path(word):
        """
        Format string so it can be used in a url path.

        Example:
            "AllTime" => "all-time"

        :param word: (str)
        :return: (str)
        """
        variable_list = GenericObjectOperations \
            .convert_string_to_character_list(word=word)
        new_word = ""
        for counter, word in enumerate(variable_list):
            word = str(word)
            if counter != 0:
                if word == word.upper():
                    if word.isalpha():
                        new_word += "-" + word
                    else:
                        new_word += "-"
                else:
                    new_word += word
            else:
                new_word += word

        return slugify(new_word)

    @staticmethod
    def format_class_name(text, separator="_"):
        text_list = re.findall('[A-Z][^A-Z]*', text)
        text = str(separator.join(text_list)).lower()
        return text
