from zope.interface import Interface

import zope.schema


class IBatch(Interface):
    """A batch splits up a large number of items over multiple pages"""

    size = zope.schema.Int(title="The amount of items in the batch")

    firstpage = zope.schema.Int(title="The number of the first page (always 1)")

    lastpage = zope.schema.Int(title="The number of the last page")

    items_not_on_page = zope.schema.List(
        title="All items that are in the batch but not on the current page"
    )

    multiple_pages = zope.schema.Bool(
        title="Boolean indicating whether there are multiple pages or not"
    )

    has_next = zope.schema.Bool(
        title="Indicator for whether there is a page after the current one"
    )

    has_previous = zope.schema.Bool(
        title="Indicator for whether there is a page after the current one"
    )

    previouspage = zope.schema.Int(title="The number of the previous page")

    nextpage = zope.schema.Int(title="The number of the nextpage page")

    next_item_count = zope.schema.Int(title="The number of items on the next page")

    navlist = zope.schema.List(
        title="List of page numbers to be used as a navigation list"
    )

    show_link_to_first = zope.schema.Bool(title="First page not in the navigation list")

    show_link_to_last = zope.schema.Bool(title="Last page not in the navigation list")

    second_page_not_in_navlist = zope.schema.Bool(
        title="Second page not in the navigation list"
    )

    before_last_page_not_in_navlist = zope.schema.Bool(
        title="Before last page not in the navigation list"
    )

    islastpage = zope.schema.Bool(
        title="Boolean indicating whether the current page is the last page"
    )

    previous_pages = zope.schema.List(
        title="All previous pages that are in the navlist"
    )

    next_pages = zope.schema.List(title="All previous pages that are in the navlist")
