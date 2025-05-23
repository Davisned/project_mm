package org.vaadin.example;

import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

import org.vaadin.example.cache.BackendCache;
import org.vaadin.example.entity.CondolenceEntry;
import org.vaadin.example.security.Roles;

import com.vaadin.flow.component.UI;
import com.vaadin.flow.component.button.Button;
import com.vaadin.flow.component.button.ButtonVariant;
import com.vaadin.flow.component.messages.MessageList;
import com.vaadin.flow.component.messages.MessageListItem;
import com.vaadin.flow.component.orderedlayout.VerticalLayout;
import com.vaadin.flow.router.BeforeEvent;
import com.vaadin.flow.router.HasUrlParameter;
import com.vaadin.flow.router.Route;

import jakarta.annotation.security.RolesAllowed;

@Route(value = "entry", layout = MainView.class)
@RolesAllowed(value = { Roles.ADMIN, Roles.USER })
public class EntryView extends VerticalLayout implements HasUrlParameter<Long> {

	private Long currentEntryId;
	private MessageList list = new MessageList();
	
	public EntryView() {
		List<CondolenceEntry> entries = BackendCache.resolveFromPersonId(currentEntryId);
		
		list.setItems(entries.stream().map(entry -> {
			return new MessageListItem(entry.getMessage(), entry.getTime(), entry.getName());
		}).collect(Collectors.toList()));
		
		Button btn = new Button("Add");
        btn.addThemeVariants(ButtonVariant.LUMO_PRIMARY);
		btn.addClickListener(event -> {
			UI.getCurrent().navigate("addCondolence/" + currentEntryId);
		});
		
		add(list, btn);
	}

	@Override
	public void setParameter(BeforeEvent event, Long entryId) {
		this.currentEntryId = entryId;
		list.setItems(Collections.emptyList());
		List<CondolenceEntry> entries = BackendCache.resolveFromPersonId(currentEntryId);
		list.setItems(entries.stream().map(entry -> {
			return new MessageListItem(entry.getMessage(), entry.getTime(), entry.getName());
		}).collect(Collectors.toList()));
	}
}
