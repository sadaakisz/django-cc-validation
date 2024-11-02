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

@register.inclusion_tag(components_dir + "main_button.html", takes_context=True)
def main_button(context, icon, text, text_color, href_url, position="", size="", bg_color="", rounded=""):
    request = context.get("request")
    if not position: position = "fixed mx-auto inset-x-0 bottom-8"
    if not size: size = "h-16 w-40"
    if not bg_color: bg_color = "bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500"
    if not rounded: rounded = "rounded-full"
    return {
        "icon": icon,
        "text": text,
        "text_color": text_color,
        "href_url": href_url,
        "position": position,
        "size": size,
        "bg_color": bg_color,
        "rounded": rounded,
    }

@register.inclusion_tag(components_dir + "main_button_with_pk.html", takes_context=True)
def main_button_with_pk(context, icon, text, text_color, href_url, pk, position="", size="", bg_color="", rounded=""):
    request = context.get("request")
    if not position: position = "fixed mx-auto inset-x-0 bottom-8"
    if not size: size = "h-16 w-40"
    if not bg_color: bg_color = "bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500"
    if not rounded: rounded = "rounded-full"
    return {
        "icon": icon,
        "text": text,
        "text_color": text_color,
        "href_url": href_url,
        "pk": pk,
        "position": position,
        "size": size,
        "bg_color": bg_color,
        "rounded": rounded,
    }