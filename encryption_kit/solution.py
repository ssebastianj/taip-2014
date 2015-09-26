# -*- coding: utf-8 -*-

import string


def encrypt(strg, passes, indices):
    encrypted_string = strg

    for i, j, k, l in indices:
        begin_part = encrypted_string[:i-1]

        first_part = replace(reverse(encrypted_string[i-1:j]))
        second_part = replace(reverse(encrypted_string[k-1:l]))

        middle_part = encrypted_string[j:k-1]
        ending_part = encrypted_string[l:]

        encrypted_string = '{}{}{}{}{}'.format(
            begin_part,
            second_part,
            middle_part,
            first_part,
            ending_part)

    return encrypted_string


def partition(strg, i, j, k, l):
    return (strg[i-1:j], strg[k-1:l])


def reverse(strg):
    return strg[::-1]


def replace_char(character):
    return string.ascii_lowercase[1 + string.ascii_lowercase.index(character) - len(string.ascii_lowercase)]


def replace(strg):
    return ''.join((replace_char(c) for c in strg))
