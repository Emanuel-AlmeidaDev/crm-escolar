from django import template

register = template.Library()


class PageNumber(object):
    def __init__(self, number, current):
        if number is not None:
            self.number = number + 1
        else:
            self.number = number

        self.current = current + 1

    def is_current(self):
        return self.number == self.current

    def is_filler(self):
        return self.number is None


@register.simple_tag
def get_pagination_links(paginator, page_obj, on_each_side=1, on_ends=1):
    page_num = page_obj.number - 1

    if paginator.num_pages <= (on_each_side + on_ends) * 2:
        page_range = range(paginator.num_pages)
    else:
        page_range = []
        if page_num > (on_each_side + on_ends):
            page_range.extend(range(0, on_ends))
            page_range.extend(range(page_num - on_each_side, page_num + 1))
        else:
            page_range.extend(range(0, page_num + 1))
        if page_num < (paginator.num_pages - on_each_side - on_ends - 1):
            page_range.extend(range(page_num + 1, page_num + on_each_side + 1))
            page_range.extend(range(paginator.num_pages -
                              on_ends, paginator.num_pages))
        else:
            page_range.extend(range(page_num + 1, paginator.num_pages))

    return map(lambda x: PageNumber(x, page_num), page_range)
