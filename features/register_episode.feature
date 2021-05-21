Feature: Register episode
  In order to upload a episode,
  As a user
  I want to register a episode together with its name, serie_name, season, number

  Background: There is a registered user
    Given Exists a user "user" with password "password"
    And Exists serie registered by "user"
      | serie_name      | category | year   |
      | Modern Family  | Comedy    | 2000   |
      | Walking Dead   | Terror    | 2008   |

  Scenario: Register episode
    Given I login as user "user" with password "password"
    When I register episode at serie "Modern Family"
       | name            |  season   | number |
       |Boda de Haley    |  2        | 20     |
    Then I view the details for episode "Boda de Haley"
       | name            | season   | number |
       |Boda de Haley    | 2        | 20     |
    And There are 1 episodes
  
    Scenario: Try to register a episode but not logged in
    Given I'm not logged in
    When I register episode at serie "Modern Family"
       | name            | season   | number |
       |Boda de Haley    | 2        | 20     |
    Then I'm redirected to the login form
    And There are 0 episodes