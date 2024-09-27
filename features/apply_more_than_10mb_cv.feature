Feature: apply more than 10mb cv
    Scenario: apply more than 10mb cv
        Given visit forest technology career page
        Then scroll to available vacancies
        And click qa engineer
        When click apply
        Then enter full name
        And enter email
        And enter phone number
        And click button next
        When upload more than 10mb cv
        Then can not upload more than 10mb cv 