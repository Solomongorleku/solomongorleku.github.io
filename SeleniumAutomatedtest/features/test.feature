Feature: Add New User

  Scenario: Adding new user to the user list
    Given launch chrome browser
    When open the data test app
    And fill first name
    And fill middle name
    And fill last name
    And fill phone number
    And fill date of birth
    And fill address
    And click add new user
    Then new user should be added to the user list
    Then close browser