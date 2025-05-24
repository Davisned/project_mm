package org.vaadin.example;

import static org.vaadin.example.security.Roles.ADMIN;
import static org.vaadin.example.security.Roles.USER;

import java.util.Collection;
import java.util.Collections;
import java.util.List;

import org.vaadin.example.cache.BackendCache;
import org.vaadin.example.entity.Person;

import com.vaadin.flow.component.UI;
import com.vaadin.flow.component.button.Button;
import com.vaadin.flow.component.button.ButtonVariant;
import com.vaadin.flow.component.grid.Grid;
import com.vaadin.flow.component.html.H2;
import com.vaadin.flow.component.orderedlayout.FlexComponent;
import com.vaadin.flow.component.orderedlayout.HorizontalLayout;
import com.vaadin.flow.component.orderedlayout.VerticalLayout;
import com.vaadin.flow.router.Route;

import jakarta.annotation.security.RolesAllowed;

@Route(value = "dashboard", layout = MainView.class)
@RolesAllowed(value = { ADMIN, USER })
public class DashboardView extends VerticalLayout {
	
	public DashboardView() {
		add(new H2("Decedents"));
		
		Button addButton = new Button("Add");
        addButton.addThemeVariants(ButtonVariant.LUMO_PRIMARY);
		addButton.addClickListener(event -> {
			UI.getCurrent().navigate(AddNewPersonView.class);
		});
		HorizontalLayout layout = new HorizontalLayout(addButton);
		layout.setWidthFull();
		layout.setJustifyContentMode(FlexComponent.JustifyContentMode.END);
		
		add(layout, getPersonGrid(BackendCache.getPersonCache().values()));
	}
	
	private Grid<Person> getPersonGrid(Collection<Person> persons) {
		Grid<Person> grid = new Grid<>(Person.class);
		grid.setItems(persons);
		grid.setColumns("id", "name", "age");
		grid.addItemClickListener(event -> {
			Person item = event.getItem();
			UI.getCurrent().navigate("entry/" + String.valueOf(item.getId()));
		});
		return grid;
	}
}
