Feature: apply using invalid email
    Scenario: apply using invalid email
        Given visit forest technology career page
        Then scroll to available vacancies
        And click qa engineer
        When click apply
        Then enter full name
        When enter invalid email
        Then invalid email warning appears