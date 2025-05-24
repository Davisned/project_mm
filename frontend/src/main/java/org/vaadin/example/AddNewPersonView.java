package org.vaadin.example;

import org.vaadin.example.cache.BackendCache;
import org.vaadin.example.entity.Person;
import org.vaadin.example.security.Roles;

import com.vaadin.flow.component.UI;
import com.vaadin.flow.component.button.Button;
import com.vaadin.flow.component.button.ButtonVariant;
import com.vaadin.flow.component.html.H2;
import com.vaadin.flow.component.notification.Notification;
import com.vaadin.flow.component.orderedlayout.VerticalLayout;
import com.vaadin.flow.component.textfield.IntegerField;
import com.vaadin.flow.component.textfield.TextField;
import com.vaadin.flow.router.Route;

import jakarta.annotation.security.RolesAllowed;

@Route(value = "person/new", layout = MainView.class)
@RolesAllowed(value = { Roles.ADMIN, Roles.USER })
public class AddNewPersonView extends VerticalLayout {

	public AddNewPersonView() {
		setPadding(true);
        setWidth("400px");
        setAlignItems(Alignment.START);

        H2 title = new H2("Neue Person hinzufügen");

        // Formularfelder
        TextField nameField = new TextField("Name");
        IntegerField alterField = new IntegerField("Alter");
        alterField.setMin(0);
        alterField.setMax(150);

        // Speichern-Button
        Button saveButton = new Button("Speichern");
        saveButton.addThemeVariants(ButtonVariant.LUMO_PRIMARY);
        
        saveButton.addClickListener(e -> {
            String name = nameField.getValue();
            Integer alter = alterField.getValue();

            if (name.isEmpty() || alter == null) {
                Notification.show("Bitte Name und Alter eingeben", 3000, Notification.Position.MIDDLE);
                return;
            }

            Person newPerson = new Person(name, alter);
            BackendCache.getPersonCache().put(newPerson.getId(), newPerson);
            Notification.show("Person gespeichert: " + newPerson.getName() + " (" + newPerson.getAge() + ")");

            // Felder leeren oder zur nächsten Seite navigieren
            nameField.clear();
            alterField.clear();
            UI.getCurrent().navigate(DashboardView.class);
        });

        add(title, nameField, alterField, saveButton);
	}
}
