package dev.revature.poms;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class WikiHomePage {
    private WebDriver driver;
    private By searchBar = By.id("searchInput");
    private By searchButton = By.className("pure-button");

    public WikiHomePage(WebDriver driver){
        this.driver = driver;
        // the PageFactory handles finding and assigning web elements to the properties we declared below
        PageFactory.initElements(driver,this);
    }

    // the FindBy annotation is how we tell the PageFactory what selector and value to look for
    // the actual finding of the element is abstracted away with this methodology
    @FindBy(id = "js-link-box-en")
    public WebElement english;

    @FindBy(css = "div[lang='es']")
    public WebElement spanish;

    @FindBy(xpath = "/html/body/div[2]/div[8]/a")
    public WebElement italian;

    public void sendKeysToSearchBar(String keys){
        driver.findElement(searchBar).sendKeys(keys);
    }

    public void clickSearchButton(){
        driver.findElement(searchButton).click();
    }


}
