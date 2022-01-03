package dev.revature.steps;

import dev.revature.runner.TestRunner;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.support.ui.ExpectedConditions;

import java.util.concurrent.TimeUnit;

public class WikiSteps {
    @Given("The user is on the wikipedia home page")
    public void the_user_is_on_the_wikipedia_home_page() {
        TestRunner.driver.get("https://www.wikipedia.org/");
    }
    @When("The English user clicks on the english link")
    public void the_english_user_clicks_on_the_english_link() {
        // use the ExpectedConditions class to determine what your explicit wait is actually waiting for
        TestRunner.explicitWait.until(ExpectedConditions.elementToBeClickable(TestRunner.wikiHomePage.english));
        TestRunner.wikiHomePage.english.click();
    }
    @Then("The English user should be redirected to the english home page")
    public void the_english_user_should_be_redirected_to_the_english_home_page() {
//        TimeUnit.SECONDS.sleep(2); calls Thread.sleep() under the hood, needs a try catch block with InteruptedException catch
//        REALLY BAD way of pausing your test: only use if desperate
        String title = TestRunner.driver.getTitle();
        Assert.assertEquals(title, "Wikipedia, the free encyclopedia");
    }
    @When("The Spanish user clicks on the spanish link")
    public void the_spanish_user_clicks_on_the_spanish_link() {
        TestRunner.wikiHomePage.spanish.click();
    }
    @Then("The Spanish user should be redirected to the spanish home page")
    public void the_spanish_user_should_be_redirected_to_the_spanish_home_page() {
        String title = TestRunner.driver.getTitle();
        Assert.assertEquals(title, "Wikipedia, la enciclopedia libre");
    }
    @When("The Italian user clicks on the italian link")
    public void the_italian_user_clicks_on_the_italian_link() {
        TestRunner.wikiHomePage.italian.click();
    }
    @Then("The Italian user should be redirected to the italian home page")
    public void the_italian_user_should_be_redirected_to_the_italian_home_page() {
        String title = TestRunner.driver.getTitle();
        Assert.assertEquals(title, "Wikipedia, l'enciclopedia libera");
    }
}
