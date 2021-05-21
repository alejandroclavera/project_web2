Feature: Delete Serie
  In order to keep updated my previous registers about serie
  As a user
  I want to delete a serie register I created

  Background: There are registered users and a serie by one of them
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists serie registered by "user1"
      | serie_name           | category | year   |
      | Modern Family        | Comedy   | 2000   |
      | The Big bang theory  | Comedy   | 2000   |

  Scenario: Delete owned serie registry
    Given I login as user "user1" with password "password"
    When I delete the serie with name "Modern Family"
    Then There are 1 serie

  Scenario: Try to delete serie but not logged in
    Given I'm not logged in
    When I view the details for serie "Modern Family"
    Then There is no "delete" link available

  Scenario: Force delete serie but not the owner permission exception
    Given I login as user "user2" with password "password"
    When I delete the serie with name "Modern Family"
    Then There is no "serie" link available

