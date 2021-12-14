1. create user stories
2. write acceptance criteria based off of user stories
3. create wireframe that includes every element needed to complete acceptance criteria
4. create feature file/s
5. create steps package
    - it needs to be called steps: when you use the behave command your code will look for this package to get the steps for completing the feature file steps
6. run behave on the feature file
    - this will fail, of course, but it will also generate code stubs you can use to implement your steps when you are read
    - take these code stubs and paste them into a module inside your steps package
        - ideally you would paste them inside a module that is named similarly or has an obvious connection to the feature file it is for
7. Acquire a driver for your chosen browser if you do not have one and place it somewhere inside your project
8. Create your page object models
    - you only need a POM for web pages that you need to directly interact with (interacting with elements, things like clicking on links or entering text into an input element)
9. create your environment.py module
    - it needs to be named correctly, or it will not run its setup and teardown methods
    - make sure to add your driver and any poms to your context object that is passed into the before_all method
        - by doing this you make sure the context object has the driver and pom objects it needs to implement your steps
    - setup any "waits" you need in this before_all method
    - make sure to call context.driver(or whatever you are calling it).quit() in the after_all method
        - if you don't do this you will have a driver running in the background until you force quit it or turn off your computer
10. implement your acceptance criteria steps
    - make sure you use the context object that is being passed into the methods
    - intellisense will probably not work during this time, so you just need to be careful with your spelling
11. run your E2E test using the behave command and adjust as needed!

Please note, these steps assume your application is complete and ready to test.