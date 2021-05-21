Feature: Register Movie
  In order to upload a serie,
  As a user
  I want to register a serie together with its serieName, serieCategory, serieYear

  Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Register serie
    Given I login as user "user" with password "password"
    When I register serie
      | serieName      | serieCategory | serieYear   |
      | Modern Family  | Comedy        | 2000        |
    Then I'm viewing the details page for serie by "user"
      | serieName      | serieCategory | serieYear   |
      | Modern Family  | Comedy        | 2000        |
    And There are 1 serie
  
    Scenario: Try to register a serie but not logged in
    Given I'm not logged in
    When I register serie
      | serieName      | serieCategory | serieYear   |
      | Modern Family  | Comedy        | 2000        |
    Then I'm redirected to the login form
    And There are 0 serie