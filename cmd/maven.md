`mvn --batch-mode validate dependency:list -DincludeScope=test -DoutputAbsoluteArtifactFilename=true`

returns

```log
[INFO]    com.google.protobuf:protobuf-java:jar:3.19.6:compile:/Users/.../.m2/repository/com/google/protobuf/protobuf-java/3.19.6/protobuf-java-3.19.6.jar -- module com.google.protobuf [auto]
[INFO]    org.openjdk.jmh:jmh-generator-annprocess:jar:1.21:provided:/Users/.../.m2/repository/org/openjdk/jmh/jmh-generator-annprocess/1.21/jmh-generator-annprocess-1.21.jar -- module jmh.generator.annprocess (auto)
[INFO]    org.apache.commons:commons-math3:jar:3.2:test:/Users/.../.m2/repository/org/apache/commons/commons-math3/3.2/commons-math3-3.2.jar -- module commons.math3 (auto)
[INFO]    org.hamcrest:hamcrest-all:jar:1.3:test:/Users/.../.m2/repository/org/hamcrest/hamcrest-all/1.3/hamcrest-all-1.3.jar -- module hamcrest.all (auto)
```

--> which you can parse to get a list of dependencies and their absolute path
-DincludeScope=compile
-DincludeScope=test
