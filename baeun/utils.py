def queryset_to_list(qs):
    return [dict(q) for q in qs]
