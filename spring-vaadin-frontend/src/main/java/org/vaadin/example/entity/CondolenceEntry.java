package org.vaadin.example.entity;

import java.time.Instant;

/**
 * Simple POJO to be used in the vaadin components.
 */
public class CondolenceEntry {

	private String name;
	private Instant time;
	private String message;

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
}
