Feature: View Serie
  In order to know about Serie
  As a user,
  I want to view the serie details.

  Background: There is one serie with 2 serie
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists serie registered by "user1"
      | serieName      | serieCategory | serieYear   |
      | Modern Family  | Comedy        | 2000        |
    And Exists serie registered by "user2"
      | serieName      | serieCategory | serieYear   |
      | Walking Dead   | Terror        | 2008        |


  Scenario: View details for added serie
    Given I login as user "user1" with password "password"
    When I view the details for serie "Modern Family"
    Then I'm viewing serie details including
      | serieName      | serieCategory | serieYear   |
      | Modern Family  | Comedy        | 2000        |
