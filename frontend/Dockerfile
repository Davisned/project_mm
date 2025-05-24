FROM maven:3-openjdk-17-slim

WORKDIR /app

COPY pom.xml .

RUN mvn dependency:resolve dependency:resolve-sources -B

RUN mvn vaadin:prepare-frontend -B || true

COPY . .

ENV VAADIN_DEVELOPMENT_MODE=true
ENV SPRING_DEVTOOLS_RESTART_ENABLED=true

# Better performance??
# RUN mvn compile -B

CMD ["mvn", "spring-boot:run", "-Dspring-boot.run.jvmArguments=-Xdebug -Xrunjdwp:transport=dt_socket,server=y,suspend=n,address=5005 -Dvaadin.productionMode=false"]
