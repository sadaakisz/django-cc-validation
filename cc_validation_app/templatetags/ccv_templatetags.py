from django import template
register = template.Library()

components_dir = "cc_validation_app/components/"

@register.inclusion_tag(components_dir + "head.html", takes_context=True)
def head(context, title):
    request = context.get("request")

    return {
        "title": title,
    }

@register.inclusion_tag(components_dir + "header.html", takes_context=True)
def header(context, top_left_icon):
    request = context.get("request")

    return {
        "top_left_icon": top_left_icon,
    }

@register.inclusion_tag(components_dir + "index_card.html", takes_context=True)
def index_card(context):
    request = context.get("request")
    return {
        "card": context["card"],
    }
