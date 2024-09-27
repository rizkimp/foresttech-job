import os
import time
import asyncio
from behave import *
from locators import *
from playwright.sync_api import sync_playwright

@when(u'apply empty cv')
def step_impl(context):
    context.page.click(locator.button_next)
    time.sleep(3)
    
@then(u'can not upload empty cv')
def step_impl(context):
    context.page.locator(locator.notif_not_upload_files)