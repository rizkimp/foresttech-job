import os
import time
import asyncio
from behave import *
from locators import *
from playwright.sync_api import sync_playwright

@when(u'enter invalid email')
def step_impl(context):
    context.page.fill(locator.input_code,'+65')
    context.page.fill(locator.input_phone,'1111111111')
    context.page.click(locator.info_code)
    context.page.fill(locator.input_email,'tamanyanghijau@gmail.')
    context.page.click(locator.button_next)
    time.sleep(3)
    
@then(u'invalid email warning appears')
def step_impl(context):
    context.page.locator(locator.notif_invalid_email)