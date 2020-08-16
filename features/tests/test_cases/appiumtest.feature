@ios
Feature: Blog
    A site where you can publish your articles.

@p1
Scenario: Check the smiley display
    Given User is on Application home page
    When User login with 'default_user'
    Then User should see the smiley

