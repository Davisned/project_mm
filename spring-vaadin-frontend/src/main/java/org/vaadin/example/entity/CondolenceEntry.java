package org.vaadin.example.entity;

import java.time.Instant;

import com.vaadin.flow.component.html.Image;

/**
 * Simple POJO to be used in the vaadin components.
 */
public class CondolenceEntry {

	private String name;
	private Instant time;
	private String message;
	private Image attachement;
	private String mime;

	public CondolenceEntry(String name, Instant time, String message) {
		this.name = name;
		this.time = time;
		this.message = message;
	}

	public String getName() {
		return name;
	}

	public Instant getTime() {
		return time;
	}

	public String getMessage() {
		return message;
	}
	
	public void setMime(String mime) {
		this.mime = mime;
	}
	
	public String getMime() {
		return mime;
	}
	
	public Image getAttachement() {
		return attachement;
	}
	
	public void setAttachement(Image attachement) {
		this.attachement = attachement;
	}
}
