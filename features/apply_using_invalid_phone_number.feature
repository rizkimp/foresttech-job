Feature: apply using invalid phone number
    Scenario: apply using invalid phone number
        Given visit forest technology career page
        Then scroll to available vacancies
        And click qa engineer
        When click apply
        Then enter full name
        And enter email
        When enter invalid phone number
        Then invalid phone number warning appears