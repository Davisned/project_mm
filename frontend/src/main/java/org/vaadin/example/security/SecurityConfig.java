package org.vaadin.example.security;

import org.slf4j.LoggerFactory;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.provisioning.InMemoryUserDetailsManager;
import org.springframework.security.provisioning.UserDetailsManager;
import org.vaadin.example.LoginView;

import com.vaadin.flow.spring.security.VaadinWebSecurity;

@EnableWebSecurity
@Configuration
class SecurityConfig extends VaadinWebSecurity {

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        super.configure(http); 
        setLoginView(http, LoginView.class);
    }

    @Bean
    public UserDetailsManager userDetailsManager() {
        LoggerFactory.getLogger(SecurityConfig.class)
            .warn("NOT FOR PRODUCITON: Using in-memory user details manager!"); 

        var user = User.withUsername("user")
                .password("{noop}user")
                .roles(Roles.USER)
                .build();
        var admin = User.withUsername("admin")
                .password("{noop}admin")
                .roles(Roles.ADMIN)
                .build();
        return new InMemoryUserDetailsManager(user, admin);
    }
}
