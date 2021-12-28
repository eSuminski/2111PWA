## Maven Life Cycle
These are the phases of a Maven build life cycle
1. Validate => project is correct and all necessary information is available
2. Compile => compiles project source code
3. Test => tests all compiled code
4. Package => packages all compiled code to WAR/JAR file
5. Integration => performs all integration tests on WAR/JAR
6. Verify => runs checks on the results of integration tests
7. Install => installs WAR/JAR to local repository
8. Deploy => copies final WAR/JAR to the remote repository