`mvn --batch-mode validate dependency:list -DincludeScope=test -DoutputAbsoluteArtifactFilename=true`

returns

```log
[INFO]    com.google.protobuf:protobuf-java:jar:3.19.6:compile:/Users/FJ19WK/.m2/repository/com/google/protobuf/protobuf-java/3.19.6/protobuf-java-3.19.6.jar -- module com.google.protobuf [auto]
[INFO]    org.openjdk.jmh:jmh-generator-annprocess:jar:1.21:provided:/Users/FJ19WK/.m2/repository/org/openjdk/jmh/jmh-generator-annprocess/1.21/jmh-generator-annprocess-1.21.jar -- module jmh.generator.annprocess (auto)
[INFO]    org.apache.commons:commons-math3:jar:3.2:test:/Users/FJ19WK/.m2/repository/org/apache/commons/commons-math3/3.2/commons-math3-3.2.jar -- module commons.math3 (auto)
[INFO]    org.hamcrest:hamcrest-all:jar:1.3:test:/Users/FJ19WK/.m2/repository/org/hamcrest/hamcrest-all/1.3/hamcrest-all-1.3.jar -- module hamcrest.all (auto)
[INFO]    org.openjdk.jmh:jmh-core:jar:1.21:test:/Users/FJ19WK/.m2/repository/org/openjdk/jmh/jmh-core/1.21/jmh-core-1.21.jar -- module jmh.core (auto)
[INFO]    org.hamcrest:hamcrest-core:jar:1.3:test:/Users/FJ19WK/.m2/repository/org/hamcrest/hamcrest-core/1.3/hamcrest-core-1.3.jar -- module hamcrest.core (auto)
[INFO]    junit:junit:jar:4.13.1:test:/Users/FJ19WK/.m2/repository/junit/junit/4.13.1/junit-4.13.1.jar -- module junit [auto]
[INFO]    net.sf.jopt-simple:jopt-simple:jar:4.6:test:/Users/FJ19WK/.m2/repository/net/sf/jopt-simple/jopt-simple/4.6/jopt-simple-4.6.jar -- module jopt.simple (auto)
[INFO]    com.google.code.gson:gson:jar:2.8.9:compile:/Users/FJ19WK/.m2/repository/com/google/code/gson/gson/2.8.9/gson-2.8.9.jar -- module com.google.gson
```

--> which you can parse to get a list of dependencies and their absolute path
-DincludeScope=compile
-DincludeScope=test
