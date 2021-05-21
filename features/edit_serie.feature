Feature: Edit Movie
  In order to keep updated my previous registers about serie
  As a user
  I want to edit a serie register I created

  Background: There are registered users and a serie by one of them
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists serie registered by "user1"
      | serieName      | serieCategory | serieYear   |
      | Modern Family  | Comedy        | 2000        |

  Scenario: Edit owned serie registry country
    Given I login as user "user1" with password "password"
    When I edit the serie with name "Modern Family"
      | serie_category |
      | Terror         |
    Then I'm viewing the details page for serie by "user1"
      | serieName      | serieCategory | serieYear   |
      | Modern Family  | Terror        | 2000        |
    And There are 1 serie

  Scenario: Try to edit serie but not logged in
    Given I'm not logged in
    When I view the details for serie "Modern Family"
    Then There is no "edit" link available

  Scenario: Force edit serie but not the owner permission exception
    Given I login as user "user2" with password "password"
    When I edit the serie with name "Modern Family"
      | serie_category |
      | Terror         |
    Then Server responds with page containing "403 Forbidden"
    When I view the details for serie "Modern Family"
    Then I'm viewing the details page for serie by "user1"
      | serieName      | serieCategory | serieYear   |
      | Modern Family  | Comedy        | 2000        |
