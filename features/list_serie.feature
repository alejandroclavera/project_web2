Feature: List Series
  In order to keep myself up to date about serie registered in my series
  As a user
  I want to list the 3 registered series

  Background: There are 3 registered series by same user
    Given Exists a user "user" with password "password"
    And Exists series registered by "user"
      | serieName      | serieCategory | serieYear   |
      | Modern Family  | Comedy        | 2000        |
      | Walking Dead   | Terror        | 2008        |

  Scenario: List the series
    When I list serie
    Then I'm viewing a list containing
      | serieName      |
      | Modern Family  |
      | Walking Dead   |
    And The list contains 2 series
