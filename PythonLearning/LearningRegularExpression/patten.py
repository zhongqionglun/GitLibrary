# -*-coding:UTF-8-*-
import re

"""
auth:zhongqionglun
time:
description:该文档显示通过函数模板来动态生产正则表达式匹配规则
"""

patterns = (('[sxz]$', '$', 'es'),
            ('[^aeioudgkprt]h$', '$', 'es'),
            ('(qu|[^aeiou])y$', 'y$', 'ies'),
            ('$', '$', 's')
            )


def plural(noun):
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)


def build_match_and_apply_fuctons(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)

    def apply_rule(word):
        return re.sub(search, replace, word)

    return (matches_rule, apply_rule)


rules = [build_match_and_apply_fuctons(pattern, search, replace) for (pattern, search, replace) in patterns]

