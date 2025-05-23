package org.vaadin.example;

import java.time.Instant;
import java.util.ArrayList;
import java.util.List;

import org.vaadin.example.cache.BackendCache;
import org.vaadin.example.entity.CondolenceEntry;
import org.vaadin.example.entity.Person;
import org.vaadin.example.security.Roles;

import com.vaadin.flow.component.UI;
import com.vaadin.flow.component.button.Button;
import com.vaadin.flow.component.button.ButtonVariant;
import com.vaadin.flow.component.html.H2;
import com.vaadin.flow.component.html.Image;
import com.vaadin.flow.component.notification.Notification;
import com.vaadin.flow.component.orderedlayout.VerticalLayout;
import com.vaadin.flow.component.textfield.TextArea;
import com.vaadin.flow.component.textfield.TextField;
import com.vaadin.flow.component.upload.Upload;
import com.vaadin.flow.component.upload.receivers.MultiFileMemoryBuffer;
import com.vaadin.flow.router.BeforeEvent;
import com.vaadin.flow.router.HasUrlParameter;
import com.vaadin.flow.router.Route;
import com.vaadin.flow.server.StreamResource;

import jakarta.annotation.security.RolesAllowed;

@Route(value = "addCondolence", layout = MainView.class)
@RolesAllowed({Roles.ADMIN, Roles.USER})
public class AddNewCondolenceView extends VerticalLayout implements HasUrlParameter<Long> {

	private Long param;
	private Image data;
	private String mime;
	
	public AddNewCondolenceView() {
		setPadding(true);
        setWidth("400px");
        setAlignItems(Alignment.START);

        H2 title = new H2("Neue Kondolenz verfassen");

        // Formularfelder
        TextField nameField = new TextField("Name");
        TextArea textArea = new TextArea();
        
        MultiFileMemoryBuffer buffer = new MultiFileMemoryBuffer();
        Upload upload = new Upload(buffer);
        upload.setMaxFileSize(Integer.MAX_VALUE);
        
        upload.addSucceededListener(event -> {
        	String filename = event.getFileName();
        	
        	StreamResource resource = new StreamResource(filename, () -> buffer.getInputStream(filename));
        	this.data = new Image(resource, "Bild");
        	this.mime = event.getMIMEType();
        	
        	System.out.println(filename + "uploaded");
        });

        // Speichern-Button
        Button saveButton = new Button("Hinzufügen");
        saveButton.addThemeVariants(ButtonVariant.LUMO_PRIMARY);
        
        saveButton.addClickListener(e -> {
            String name = nameField.getValue();
            String message = textArea.getValue();
            
            CondolenceEntry entry = new CondolenceEntry(name, Instant.now(), message);
            entry.setAttachement(data);
            Person person = BackendCache.getPersonCache().get(param);
            if (person == null) {
            	System.out.println("No Person for you!");
            }
            List<CondolenceEntry> list = BackendCache.getCondolenceCache().get(person);
            if (list == null) {
            	list = new ArrayList<>();
            	BackendCache.getCondolenceCache().put(person, list);
            }
            list.add(entry);
            
            Notification.show("Eintrag gespeichert: " + entry.getName() + " (" + entry.getMessage() + ")");

            // Felder leeren oder zur nächsten Seite navigieren
            nameField.clear();
            UI.getCurrent().navigate("entry/" + param);
        });

        add(title, nameField, textArea, upload, saveButton);
	}

	@Override
	public void setParameter(BeforeEvent event, Long parameter) {
		this.param = parameter;
	}
}
