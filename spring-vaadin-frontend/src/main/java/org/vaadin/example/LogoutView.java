package org.vaadin.example;

//import com.vaadin.flow.component.button.Button;
import com.vaadin.flow.component.html.Main;
import com.vaadin.flow.router.Route;
import com.vaadin.flow.spring.security.AuthenticationContext;

import jakarta.annotation.security.PermitAll;

@Route("logout")
@PermitAll
public class LogoutView extends Main {

	public LogoutView(AuthenticationContext authenticationContext) { 
		authenticationContext.logout();
//        add(new Button("Logout", event -> authenticationContext.logout()));
    }
}
