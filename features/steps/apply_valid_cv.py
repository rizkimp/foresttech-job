import os
import time
import asyncio
from behave import *
from locators import *
from playwright.sync_api import sync_playwright

@given(u'visit forest technology career page')
def step_impl(context):
    context.page.goto('https://theforest.ai/careers')
    time.sleep(10)

@then(u'scroll to available vacancies')
def step_impl(context):
    available_vacancies = locator.vacancies
    element = context.page.query_selector(available_vacancies)
    context.page.evaluate('(element) => element.scrollIntoView()', element)

@then(u'click qa engineer')
def step_impl(context):
    context.page.click(locator.qa_engineer)
    time.sleep(3)

@when(u'click apply')
def step_impl(context):
    context.page.click(locator.button_apply)
    time.sleep(3)

@then(u'enter full name')
def step_impl(context):
    context.page.fill(locator.input_name,'test')

@then(u'enter email')
def step_impl(context):
    context.page.fill(locator.input_email,'test@test.com')

@then(u'enter phone number')
def step_impl(context):
    context.page.fill(locator.input_code,'+65')
    context.page.fill(locator.input_phone,'1111111111')
    context.page.click(locator.info_code)
    time.sleep(1)

@then(u'click button next')
def step_impl(context):
    context.page.click(locator.button_next)
    time.sleep(1)

@then(u'upload valid cv')
def step_impl(context):
    context.page.set_input_files(locator.input_cv,'features/steps/assets/test.pdf')
    time.sleep(5)
    context.page.locator(locator.cv_uploaded)

@then(u'enter cover letter')
def step_impl(context):
    context.page.fill(locator.input_cover_letter,'test')
    time.sleep(3)

@when(u'click button Submit')
def step_impl(context):
    context.page.click(locator.button_submit)
    time.sleep(3)

@then(u'success apply valid cv')
def step_impl(context):
    context.page.locator(locator.notif_application_sent)