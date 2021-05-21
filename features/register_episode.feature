Feature: Register Episode
  In order to upload a Episode of a Serie
  As a user
  I want to register a serie together with its name, serie_name, season, number.

  Background: There is a registered user and Serie
    Given Exists a user "user" with password "password"
    And Exists a Serie registered by "user"
      | serie_name         |
      | Modern Family      |

  Scenario: Register episode 
    Given I login as user "user" with password "password"
    When I register dish at restaurant "Modern Family"
      | name            | season  | number|
      | Boda con Haley  | 1       | 20    |
    Then I'm viewing the details page for dish at restaurant "The Tavern" by "user"
      | name            | serie_name    | season  | number|
      | Boda con Haley  | Modern Family | 1       | 20    |
    And There are 1 dishes

 