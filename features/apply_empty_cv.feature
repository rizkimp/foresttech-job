Feature: apply empty cv
    Scenario: apply empty cv
        Given visit forest technology career page
        Then scroll to available vacancies
        And click qa engineer
        When click apply
        Then enter full name
        And enter email
        And enter phone number
        And click button next
        When apply empty cv
        Then can not upload empty cv