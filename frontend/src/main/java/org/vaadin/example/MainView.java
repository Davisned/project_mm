package org.vaadin.example;

import static org.vaadin.example.security.Roles.ADMIN;
import static org.vaadin.example.security.Roles.USER;

import com.vaadin.flow.component.applayout.AppLayout;
import com.vaadin.flow.component.html.H1;
import com.vaadin.flow.component.orderedlayout.FlexComponent.Alignment;
import com.vaadin.flow.component.orderedlayout.HorizontalLayout;
import com.vaadin.flow.component.orderedlayout.VerticalLayout;
import com.vaadin.flow.router.Route;
import com.vaadin.flow.router.RouterLink;
import com.vaadin.flow.spring.security.AuthenticationContext;

import jakarta.annotation.security.RolesAllowed;

/**
 * A sample Vaadin view class.
 * <p>
 * To implement a Vaadin view just extend any Vaadin component and use @Route
 * annotation to announce it in a URL as a Spring managed bean.
 * <p>
 * A new instance of this class is created for every new user and every browser
 * tab/window.
 * <p>
 * The main view contains a text field for getting the user name and a button
 * that shows a greeting message in a notification.
 */
@Route("")
@RolesAllowed(value = {ADMIN, USER})
public class MainView extends AppLayout {

    public MainView(AuthenticationContext authenticationContext) {
        createHeader();
        createDrawer();
    }

    private void createHeader() {
        H1 logo = new H1("Hopeject");
        logo.addClassNames("text-l", "m-m");

        HorizontalLayout header = new HorizontalLayout(logo);
        header.setDefaultVerticalComponentAlignment(Alignment.CENTER);
        header.setWidthFull();
        header.addClassNames("py-0", "px-m");

        addToNavbar(header);
    }

    private void createDrawer() {
        RouterLink dashboardLink = new RouterLink("Dashboard", DashboardView.class);
        RouterLink settingsLink = new RouterLink("Einstellungen", SettingsView.class);
        RouterLink loginLink = new RouterLink("Login", LoginView.class);
        RouterLink logoutLink = new RouterLink("Logout", LogoutView.class);
        
        addToDrawer(new VerticalLayout(
            dashboardLink,
            settingsLink,
            logoutLink
        ));
    }
}
