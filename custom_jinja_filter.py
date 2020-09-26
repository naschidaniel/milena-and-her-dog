#!/usr/bin/python

def milena_custom_filter(text):
    """A function to replace the custom tags in the markdown templates"""
    text = text.replace("[start-milena-img-show]",'<div id="img-slideshow" class="img-slideshow flex justify-center">')
    text = text.replace("[end-milena-img-show]","</div>")
    return text