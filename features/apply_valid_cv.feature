Feature: apply valid cv
    Scenario: apply valid cv
        Given visit forest technology career page
        Then scroll to available vacancies
        And click qa engineer
        When click apply
        Then enter full name
        And enter email
        And enter phone number
        And click button next
        And upload valid cv
        And click button next
        And enter cover letter
        When click button Submit
        Then success apply valid cv  