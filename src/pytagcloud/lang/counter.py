# -*- coding: utf-8 -*-
import re
from pytagcloud.lang.stopwords import get_stop_words
from operator import itemgetter


def get_tag_counts(text):
    """
    Search tags in a given text.
    """
    words = map(lambda x: x.lower(), re.findall(r'[\w-]+', text, re.UNICODE))
    stop_words = get_stop_words()
    counted = {}
    for word in words:
        if len(word) > 1 and word not in stop_words:
            if word in counted:
                counted[word] += 1
            else:
                counted[word] = 1
    return sorted(counted.iteritems(), key=itemgetter(1), reverse=True)
