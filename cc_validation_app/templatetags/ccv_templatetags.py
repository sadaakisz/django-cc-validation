from django import template
register = template.Library()

components_dir = "cc_validation_app/components/"

@register.inclusion_tag(components_dir + "head.html", takes_context=True)
def head(context, title, context_id=""):
    request = context.get("request")

    return {
        "title": title,
        "context_id": context_id,
    }

@register.inclusion_tag(components_dir + "header.html", takes_context=True)
def header(context, top_left_icon, href_url="cc_validation_app:index"):
    request = context.get("request")

    return {
        "top_left_icon": top_left_icon,
        "href_url": href_url,
    }

@register.inclusion_tag(components_dir + "index_card.html", takes_context=True)
def index_card(context):
    request = context.get("request")
    return {
        "card": context["card"],
    }
