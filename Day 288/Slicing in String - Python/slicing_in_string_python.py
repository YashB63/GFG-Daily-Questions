def join_middle(bound_by, tag_name):
    x=len(bound_by)//2
    return bound_by[0 :x ] + tag_name + bound_by[x: ]