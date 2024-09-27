import os
import time
import asyncio
from behave import *
from locators import *
from playwright.sync_api import sync_playwright

@when(u'upload more than 10mb cv')
def step_impl(context):
    context.page.set_input_files(locator.input_cv,'features/steps/assets/15mb.pdf')
    time.sleep(5)
    
@then(u'can not upload more than 10mb cv')
def step_impl(context):
    context.page.locator(locator.file_too_large)