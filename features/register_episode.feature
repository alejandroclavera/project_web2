Feature: Register episode
  In order to upload a episode,
  As a user
  I want to register a episode together with its name, serie_name, season, number

  Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Register episode
    Given I login as user "user" with password "password"
    When I register episode
       | name            | serie_name    | season   | number |
       |Boda de Haley    | Modern Family | 2        | 20     |
    Then I'm viewing the details page for episode by "user"
       | name            | serie_name    | season   | number |
       |Boda de Haley    | Modern Family | 2        | 20     |
    And There are 1 episode
  
    Scenario: Try to register a episode but not logged in
    Given I'm not logged in
    When I register episode
       | name            | serie_name    | season   | number |
       |Boda de Haley    | Modern Family | 2        | 20     |
    Then I'm redirected to the login form
    And There are 0 episode