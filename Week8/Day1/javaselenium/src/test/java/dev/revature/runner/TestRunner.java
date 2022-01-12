package dev.revature.runner;

import dev.revature.poms.WikiHomePage;
import io.cucumber.junit.Cucumber;
import io.cucumber.junit.CucumberOptions;
import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.runner.RunWith;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.io.File;
import java.util.concurrent.TimeUnit;

// this lets us use the Cucumber testing framework with Junit
@RunWith(Cucumber.class)
// the features section tells our application where to find the feature files: it looks inside the resources folder for them by default
// glue tells the application where the steps are located. Ending on a package will run all test classes found inside, ending on
// a class file will only use steps from that class
// to run your E2E test you run this TestRunner class
// needs to be called TestRunner, any other name and the test will fail
// to order your tests you can list the feature files in the order you wish to run them (note that it is ideal to have your
// E2E tests pass regardless of the order of execution)
@CucumberOptions(features = {"src/test/resources/features/scenarioOutlineExample.feature", "src/test/resources/features/wikiSteps.feature"}, glue = "dev/revature/steps", plugin = {"pretty", "html:src/test/resources/reports/html-reports.html"})
public class TestRunner{
    public static WebDriver driver;
    public static WikiHomePage wikiHomePage;
    // the explicit wait can be used when you need to wait for a single element
    public static WebDriverWait explicitWait;

    // use BeforeClass to set up your E2E tests
    @BeforeClass
    public static void setup(){
        // these two lines set up the chrome driver for use: line one gives the location, line two informs our app it is a chrome driver
        File file = new File("src/test/resources/chromedriver.exe");
        System.setProperty("webdriver.chrome.driver", file.getAbsolutePath());
        driver = new ChromeDriver();
        wikiHomePage = new WikiHomePage(driver);
        System.out.println("setup complete!");
        // this determines the time of the explicit wait
        driver.manage().timeouts().implicitlyWait(1, TimeUnit.SECONDS);
        // this determines the time of the implicit wait
        explicitWait = new WebDriverWait(driver, 1);
    }

    // use AfterClass to teardown your E2E tests
    @AfterClass
    public static void teardown(){
        // make sure to quite the driver at the end
        driver.quit();
        System.out.println("teardown complete!");
    }
}
