# Agile
Agile is a development mindset that is tech agnostic: you can use this mindset with any programming language. There are four core tenants of Agile Software Development:

1. Individuals and Interaction over processes and tools
    - colloboration is key
2. Working software over comprehensive documentation
    - it is better to have an actual product than fancy notes for a broken piece of software
3. Customer collaboration over contract negotiation
    - customers don't know what they want: this system of development allows us to adjust on the fly to customer wishes
4. Responding to change over following a plan
    - short sprints are prefered over long contract periods

# Scrum
Scrum is an iterative way of doing software development. It is a system that easily promotes an agile mindset for development. There are four roles in a Scrum:

- Stakeholder
    - the product is for this entity. It could be a person, company, etc.
- Product Holder
    - representative of the stake holder
    - go-to person when you have questions, updates, etc.
- Scrum Leader
    - person in charge of the scrum team 
        - think lead developer
    - their primary goal is to help the team work at a high level
        - they provide encouragement
        - they help with debugging
        - they interact with the product holder
        - they help with inner-team communications
        - etc.
- team member (scrummling)
    - developers
    - devops
    - business analysts

### Scrum Process
Mosts scrums last two-three weeks. A single iteration of a Scrum project is called a sprint. Sprints each have their own "ceremonies" that go along with the development cycle:
1. User Story Grooming
    - first event of the sprint
    - User stories and acceptance criteria are created in this ceremony
    - story pointing happens after the user stories and acceptance criteria are written
        - this is where difficutly ratings are assigned to user stories and their acceptance criteria
    - User stories are then assigned to teams/individuals based upon their difficutly rating and developer skills.
2. Daily Standup
    - it is a daily check-in with your team
        - talk about progress
        - talk about blockers
        - offer each other help with blockers
3. Sprint Retrospective
    - this is the last ceremony of a sprint
        - discuss what went well
        - discuss what didn't go well
        - plan for next sprint
            - any userstories that were not completed this sprint?
            - any need project requirements?
            - etc.
### Standard Development Life Cycle
There is no one true SDLC, but there is a pattern of development that most companies will follow. As long as you are familiar with these five steps you will be able to see them in just about any company specific SDLC:

1. Determine Software Requirements
    - this is where user stories would be written
    - determine what is important for the client
        - does this code need to be fast?
        - does this application need to look nice?
        - does this application need to be easy to use?
        - etc.
2. Design the software
    - create your interfaces (abstract classes in Python)
    - determine client-side techs
        - are we going to use Angular?
        - are we going to use plain JavaScript?
        - etc.
3. Develop/Test
    - TDD
        - create tests
        - write code to pass tests
4. Deploy
    - package your software
        - deploy application to AWS
        - create executable file
        - etc.
5. Monitor/Maintanence
    - keep track of the applicaiton
        - check logs
        - check web traffic
        - etc.

### Continuous Integration
Continuous Integration is the practice of updating and maintaining a single repository of code. You can have divergant branches of code that are constantly being merged into the main, but there is one main branch that is considered the "production" branch of code.