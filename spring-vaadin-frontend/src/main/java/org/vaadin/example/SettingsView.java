package org.vaadin.example;

import org.vaadin.example.security.Roles;

import com.vaadin.flow.component.html.H2;
import com.vaadin.flow.component.orderedlayout.VerticalLayout;
import com.vaadin.flow.router.Route;

import jakarta.annotation.security.RolesAllowed;

@Route(value = "settings", layout = MainView.class)
@RolesAllowed(value= {Roles.ADMIN, Roles.USER})
public class SettingsView extends VerticalLayout {
    public SettingsView() {
        add(new H2("Einstellungen"));
    }
}